"""
Generate MTP radial grid SVGs: octant hue interpolation over a checkerboard canvas.

Neutrals are warm paper (yang) and deep ink (ying). The SVG has no separate
full-viewport background element: opaque checkerboard cells cover the whole
bitmap.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import math
import sys

# --- Layout reference (18-cell design); radii scale with grid size ------------
REF_GRID = 18
REF_INNER = 6.0
REF_OUTER = 10.0

RGB = tuple[int, int, int]
Palette = tuple[RGB, ...]


# --- Color tokens -------------------------------------------------------------
BG_YANG = (255, 252, 240)
BG_YING = (16, 15, 15)

INNER_PALETTE: Palette = (
    (135, 154, 57),    # Green (Grow)
    (208, 162, 21),    # Yellow (Open)
    (209, 77, 65),     # Red (Power)
    (206, 93, 151),    # Magenta (Return)
    (255, 252, 240),   # White (Focus)
    (139, 126, 200),   # Purple (Close)
    (67, 133, 190),    # Blue (Flow)
    (58, 169, 159),    # Cyan (Enter)
)

OUTER_PALETTE: Palette = (
    (61, 76, 7),       # Green (Wither)
    (102, 77, 1),      # Yellow (Still)
    (108, 32, 28),     # Red (Void)
    (100, 31, 70),     # Magenta (Surge)
    (16, 15, 15),      # White (Haze)
    (60, 42, 98),      # Purple (Fade)
    (22, 59, 102),     # Blue (Abyss)
    (22, 79, 74),      # Cyan (Drift)
)


@dataclass(frozen=True)
class GridTheme:
    name: str
    checkerboard_light: RGB
    checkerboard_dark: RGB
    checkerboard_opacity: float
    inner_palette: Palette
    outer_palette: Palette


@dataclass(frozen=True)
class GridPreset:
    name: str
    size: int
    cell_px: int
    center: float


DEFAULT_THEME = GridTheme(
    name="main",
    checkerboard_light=BG_YANG,
    checkerboard_dark=BG_YING,
    checkerboard_opacity=1.0,
    inner_palette=INNER_PALETTE,
    outer_palette=OUTER_PALETTE,
)

DEFAULT_PRESET = GridPreset(name="19x19 lines", size=18, cell_px=16, center=9.0)
GRID_28x28_PRESET = GridPreset(name="28x28 lines", size=27, cell_px=16, center=13.5)
GRID_37x37_PRESET = GridPreset(name="37x37 lines", size=36, cell_px=16, center=18.0)
GRID_10x10_PRESET = GridPreset(name="10x10 lines", size=9, cell_px=9, center=4.5)


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def smoothstep(t: float) -> float:
    t = clamp01(t)
    return t * t * (3.0 - 2.0 * t)


def mix_rgb(c1: RGB, c2: RGB, t: float) -> RGB:
    return tuple(int(round(lerp(c1[i], c2[i], t))) for i in range(3))


def scaled_radii(grid_cells: int) -> tuple[float, float]:
    scale = grid_cells / float(REF_GRID)
    return REF_INNER * scale, REF_OUTER * scale


def hue_blend(dx: float, dy: float) -> tuple[int, float]:
    angle = math.atan2(dy, dx)
    angle_norm = (angle + math.pi) / (2.0 * math.pi)
    sector = angle_norm * 8.0
    index = int(sector) % 8
    t = sector - int(sector)
    return index, t


def chebyshev_distance(dx: float, dy: float) -> float:
    return max(abs(dx), abs(dy))


def radial_alpha(distance: float, inner_max: float) -> float:
    if inner_max <= 0:
        return 1.0
    return clamp01(distance / inner_max)


def radial_dark_mix(distance: float, inner_max: float, outer_end: float) -> float:
    fade_width = outer_end - inner_max
    if fade_width <= 0:
        raise ValueError("outer_end must be greater than inner_max")

    if distance <= inner_max:
        return 0.0

    t = (distance - inner_max) / fade_width
    t = smoothstep(t)

    # Push slightly harder into the dark palette for clearer contrast.
    return clamp01(t ** 1.15)


def interpolated_palette_color(
    palette: Palette,
    index: int,
    t: float,
) -> RGB:
    return mix_rgb(palette[index], palette[(index + 1) % 8], t)


def compute_cell_style(
    x: int,
    y: int,
    center: float,
    inner_max: float,
    outer_end: float,
    theme: GridTheme,
) -> tuple[RGB, float]:
    dx = (x + 0.5) - center
    dy = (y + 0.5) - center

    index, hue_t = hue_blend(dx, dy)

    inner_color = interpolated_palette_color(theme.inner_palette, index, hue_t)
    outer_color = interpolated_palette_color(theme.outer_palette, index, hue_t)

    distance = chebyshev_distance(dx, dy)

    alpha = radial_alpha(distance, inner_max) if distance <= inner_max else 1.0
    dark_t = radial_dark_mix(distance, inner_max, outer_end)
    color = mix_rgb(inner_color, outer_color, dark_t)

    return color, alpha


def format_rgb(color: RGB) -> str:
    r, g, b = color
    return f"rgb({r}, {g}, {b})"


def render_rect(x: int, y: int, cell_px: int, color: RGB, alpha: float) -> str:
    return (
        f'<rect x="{x * cell_px}" y="{y * cell_px}" width="{cell_px}" height="{cell_px}" '
        f'fill="{format_rgb(color)}" fill-opacity="{alpha:.3f}"/>'
    )


def generate_checkerboard(preset: GridPreset, theme: GridTheme) -> list[str]:
    rects: list[str] = []
    for y in range(preset.size):
        for x in range(preset.size):
            rgb = theme.checkerboard_light if (x + y) % 2 == 0 else theme.checkerboard_dark
            rects.append(render_rect(x, y, preset.cell_px, rgb, theme.checkerboard_opacity))
    return rects


def generate_svg(preset: GridPreset, theme: GridTheme) -> str:
    inner_max, outer_end = scaled_radii(preset.size)

    width = preset.size * preset.cell_px
    height = preset.size * preset.cell_px

    lines: list[str] = [
        f"<svg width='{width}' height='{height}' xmlns='http://www.w3.org/2000/svg'>",
    ]

    lines.extend(generate_checkerboard(preset, theme))

    for y in range(preset.size):
        for x in range(preset.size):
            color, alpha = compute_cell_style(x, y, preset.center, inner_max, outer_end, theme)
            lines.append(render_rect(x, y, preset.cell_px, color, alpha))

    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def select_preset(args: argparse.Namespace) -> GridPreset:
    if args.grid_37x37:
        return GRID_37x37_PRESET
    if args.grid_28x28:
        return GRID_28x28_PRESET
    if args.grid_10x10:
        return GRID_10x10_PRESET
    return DEFAULT_PRESET


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate MTP grid SVG.")
    preset = parser.add_mutually_exclusive_group()

    preset.add_argument(
        "--grid-37x37",
        action="store_true",
        help="37x37 lines (36x36 cells), cell=16px, center=18.0",
    )
    preset.add_argument(
        "--grid-28x28",
        action="store_true",
        help="28x28 lines (27x27 cells), cell=16px, center=13.5",
    )
    preset.add_argument(
        "--grid-10x10",
        action="store_true",
        help="10x10 lines (9x9 cells), cell=9px, center=4.5",
    )

    args = parser.parse_args()
    selected_preset = select_preset(args)

    sys.stdout.write(generate_svg(selected_preset, DEFAULT_THEME))


if __name__ == "__main__":
    main()
