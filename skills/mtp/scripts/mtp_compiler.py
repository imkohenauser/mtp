"""
MTP compiler: parse `/mtp` argument strings into axis constraints.

Maps grid coordinates (Volcano model, Chebyshev distance) and slider tokens to
axis / polarity / intensity, then pulls matching lines from `nodes/*.md`.
"""

import argparse
import os
import re
import sys
import unicodedata

# --- Grid topology (19×19, 3×3 macro zones) ---------------------------------
# [row_zone][col_zone] → axis color name. Column zones: x 1–6, 7–12, 13–19
# (boundaries 1/7/13/19 attach to the adjacent zone; fine-grained shading uses distance, not this lookup).
GRID_AXES = [
    ["yellow", "red",         "magenta"],
    ["green",  "transparent", "white"  ],
    ["cyan",   "blue",        "purple" ],
]

COL_ZONE_BOUNDS = (6, 12)
ROW_ZONE_BOUNDS = (6, 12)

GRID_COLS = 19
GRID_ROWS = 19
GRID_CENTER_X = 10
GRID_CENTER_Y = 10
MAX_CHEBYSHEV_DISTANCE = 9

# `yellow:50` ≡ Side A/B sliders on that axis (e.g. open / still).
AXIS_COLOR_SLIDERS = {
    "yellow": ("open", "still"),
    "red": ("power", "void"),
    "magenta": ("return", "surge"),
    "green": ("grow", "wither"),
    "transparent": ("helix", "collapse"),
    "white": ("focus", "haze"),
    "cyan": ("enter", "drift"),
    "blue": ("flow", "abyss"),
    "purple": ("close", "fade"),
}

# IMEs often emit Unicode hyphens; fold to ASCII for parsing.
_DASH_NORMALIZATION_TABLE = str.maketrans({
    "‐": "-",
    "‑": "-",
    "‒": "-",
    "–": "-",
    "—": "-",
    "−": "-",
    "ー": "-",
    "ｰ": "-",
    "﹣": "-",
    "－": "-",
})


def normalize_mtp_args(args_str):
    """NFKC + Unicode dash → ASCII `-` for stable token parsing."""
    normalized = unicodedata.normalize("NFKC", args_str)
    return normalized.translate(_DASH_NORMALIZATION_TABLE)


# --- Node map from `nodes/*.md` frontmatter -----------------------------------

def _parse_frontmatter(text):
    """Parse simple `key: value` lines inside the first `--- ... ---` block."""
    fm = {}
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return fm
    for line in match.group(1).splitlines():
        kv = re.match(r"^(\w+)\s*:\s*(.*?)\s*$", line)
        if kv:
            val = kv.group(2)
            if len(val) >= 2 and val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            fm[kv.group(1)] = val
    return fm


def build_node_map(nodes_dir):
    """Return `(node_map, axis_descriptions)` from `*.md` frontmatter in `nodes_dir`."""
    node_map = {}
    axis_descriptions = {}

    for filename in os.listdir(nodes_dir):
        if not filename.lower().endswith(".md"):
            continue
        path = os.path.join(nodes_dir, filename)
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except OSError:
            continue

        fm = _parse_frontmatter(content)
        axis = fm.get("axis", "").lower()
        pos  = fm.get("node_positive", "").lower()
        neg  = fm.get("node_negative", "").lower()
        desc = fm.get("description", "")

        if axis and pos:
            node_map[pos] = {"axis": axis, "polarity": 1}
        if axis and neg:
            node_map[neg] = {"axis": axis, "polarity": -1}
        if axis and desc:
            axis_descriptions[axis] = desc

    return node_map, axis_descriptions


def load_presets(references_dir):
    """Load `references/presets.yaml` as `{ name -> expansion }` (line-based, no PyYAML)."""
    path = os.path.join(references_dir, "presets.yaml")
    presets = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                kv = re.match(r'^([\w-]+)\s*:\s*"?(.+?)"?\s*$', line)
                if kv:
                    presets[kv.group(1).lower()] = kv.group(2)
    except OSError:
        pass
    return presets


def expand_presets(args_str, presets):
    """Replace preset-name tokens with their expansions."""
    normalized_args = normalize_mtp_args(args_str)
    tokens = normalized_args.replace(",", " ").split()
    expanded = []
    for token in tokens:
        token_lower = token.lower()
        if token_lower in presets:
            expanded.append(presets[token_lower])
        elif token_lower.startswith("preset:"):
            name = token.split(":", 1)[1]
            sys.stderr.write(
                f"Warning: 'preset:' syntax is no longer supported ('{name}'). "
                f"Use preset names directly: {', '.join(sorted(presets.keys()))}\n"
            )
        else:
            expanded.append(token)
    return " ".join(expanded)


# --- Parse tokens (grid `A-10`, sliders `power:70`, color aliases) ------------

def _grid_zone(i: int, bounds: tuple[int, int]) -> int:
    if i <= bounds[0]:
        return 0
    return 1 if i <= bounds[1] else 2


def parse_grid(grid_str, emit_warnings=True):
    """Parse `G-10`-style coordinates → `(axis, polarity, intensity)`; Volcano + Chebyshev from J-10."""
    normalized_grid = normalize_mtp_args(grid_str)
    match = re.fullmatch(r"([A-Sa-s])-(\d+)", normalized_grid)
    if not match:
        return None

    col_char = match.group(1).upper()
    x = ord(col_char) - ord("A") + 1
    y = int(match.group(2))

    if not (1 <= x <= GRID_COLS and 1 <= y <= GRID_ROWS):
        if emit_warnings:
            sys.stderr.write(
                f"Warning: Grid coordinate '{grid_str}' is out of range "
                f"(columns A-S, rows 1-19).\n"
            )
        return None

    gz_x = _grid_zone(x, COL_ZONE_BOUNDS)
    gz_y = _grid_zone(y, ROW_ZONE_BOUNDS)
    axis = GRID_AXES[gz_y][gz_x]

    distance = max(abs(x - GRID_CENTER_X), abs(y - GRID_CENTER_Y))

    # Volcano: 0..6 → 0..+100; 6..9 → +100..−100 (Chebyshev from center)
    if distance <= 6:
        intensity_signed = (distance / 6.0) * 100
    else:
        intensity_signed = 100 - 200 * ((distance - 6.0) / (MAX_CHEBYSHEV_DISTANCE - 6))

    polarity = 1 if intensity_signed >= 0 else -1
    intensity = min(100, int(round(abs(intensity_signed))))

    return axis, polarity, intensity


def _parse_slider_command(node, val_str, node_map):
    """Return `(parsed_tuple, None, None)`, `(None, 'neutral', None)`, or `(None, None, reason)`."""
    if not re.fullmatch(r"-?\d+", val_str):
        return None, None, "invalid numeric value"

    val = int(val_str)
    if node in AXIS_COLOR_SLIDERS:
        pos_n, neg_n = AXIS_COLOR_SLIDERS[node]
        node = pos_n if val >= 0 else neg_n
        val = abs(val)

    if node not in node_map:
        return None, None, "unknown node"

    axis = node_map[node]["axis"]
    intensity = min(100, abs(val))
    if intensity == 0:
        return None, "neutral", None

    polarity = node_map[node]["polarity"] * (1 if val >= 0 else -1)
    return (axis, polarity, intensity), None, None


def parse_arguments(args_str, node_map):
    """Classify tokens into `parsed`, `invalid`, and `neutral` lists."""
    normalized_args = normalize_mtp_args(args_str)
    commands = normalized_args.replace(",", " ").split()
    parsed = []
    invalid = []
    neutral = []

    for cmd in commands:
        cmd_lower = cmd.lower()

        if ":" in cmd_lower:
            node, val_str = cmd_lower.split(":", 1)

            # `D:16` → treat as `D-16`
            if re.fullmatch(r"[a-s]", node):
                if not re.fullmatch(r"\d+", val_str):
                    invalid.append((cmd, "invalid grid token"))
                    continue

                grid_result = parse_grid(cmd_lower.replace(":", "-", 1), emit_warnings=False)
                if grid_result:
                    _axis, _pol, intensity = grid_result
                    if intensity >= 1:
                        parsed.append(grid_result)
                    else:
                        neutral.append(cmd)
                else:
                    invalid.append((cmd, "invalid grid token"))
                continue

            if node in AXIS_COLOR_SLIDERS or node in node_map:
                parsed_command, neutral_marker, invalid_reason = _parse_slider_command(
                    node, val_str, node_map
                )
                if parsed_command:
                    parsed.append(parsed_command)
                elif neutral_marker:
                    neutral.append(cmd)
                else:
                    invalid.append((cmd, invalid_reason))
                continue

            if re.fullmatch(r"-?\d+", val_str):
                invalid.append((cmd, "unknown node"))
            else:
                invalid.append((cmd, "invalid token"))
            continue

        elif "-" in cmd_lower and any(c.isalpha() for c in cmd_lower):
            if re.fullmatch(r"[a-s]-\d+", cmd_lower):
                grid_result = parse_grid(cmd_lower, emit_warnings=False)
                if grid_result:
                    _axis, _pol, intensity = grid_result
                    if intensity >= 1:
                        parsed.append(grid_result)
                    else:
                        neutral.append(cmd)
                else:
                    invalid.append((cmd, "invalid grid token"))
            else:
                invalid.append((cmd, "invalid grid token"))
            continue

        else:
            invalid.append((cmd, "invalid token"))

    return parsed, invalid, neutral


def resolve_conflicts(parsed_commands):
    """Last token per axis wins; order follows last appearance."""
    resolved_by_axis = {}

    for axis, polarity, intensity in parsed_commands:
        if axis in resolved_by_axis:
            del resolved_by_axis[axis]
        resolved_by_axis[axis] = (axis, polarity, intensity)

    return list(resolved_by_axis.values())


# --- Constraint lines from `nodes/{AXIS}.md` ----------------------------------

def extract_constraints(axis, polarity, intensity, nodes_dir):
    """Collect bullet lines under the matching Side and Low/Mid/High sections."""
    file_path = os.path.join(nodes_dir, f"{axis.upper()}.md")

    if not os.path.exists(file_path):
        return []

    target_side = "Side A" if polarity > 0 else "Side B"

    active_levels = ["low"]
    if intensity >= 31:
        active_levels.append("mid")
    if intensity >= 71:
        active_levels.append("high")

    extracted_lines = []
    in_target_side = False
    current_level = None

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()

            if stripped.startswith("##") and "Side" in stripped:
                in_target_side = target_side in stripped
                current_level = None
                continue

            if not in_target_side:
                continue

            level_match = re.match(r"###\s+(Low|Mid|High)", stripped, re.IGNORECASE)
            if level_match:
                current_level = level_match.group(1).lower()
                continue

            if current_level in active_levels:
                if stripped and stripped != "---" and not stripped.startswith("#"):
                    extracted_lines.append(stripped)

    return extracted_lines


# --- CLI (help, list, mtp_node_shot stdout) ------------------------------------

def load_help_text(references_dir, filename):
    """Read `references_dir/filename` or a short missing-file fallback."""
    path = os.path.join(references_dir, filename)
    try:
        with open(path, encoding="utf-8") as f:
            return f.read().rstrip("\n")
    except OSError:
        return f"Help file not found: {filename}"


def _print_mtp_constraint_preamble():
    """Preamble inside `<mtp_node_shot>` before constraint blocks."""
    print(
        "Apply the following exploration and structure rules as internal parameters for the next output only. "
        "The constraint-application process must not be mentioned in the reply (e.g. \"I will output in this tone\" or \"Following the constraints\")."
    )
    print()


def _format_mtp_stderr_summary(parsed_commands):
    """Single-line stderr summary of resolved axes."""
    parts = []
    for axis, polarity, intensity in parsed_commands:
        direction = "+" if polarity > 0 else "-"
        parts.append(f"{axis}{direction} {intensity}")
    return "MTP: " + "; ".join(parts)


def _write_invalid_token_warnings(invalid_tokens):
    """Emit one stderr warning per invalid token."""
    for token, reason in invalid_tokens:
        sys.stderr.write(f"Warning: Ignored token '{token}' ({reason}).\n")


def _print_presets_table(presets):
    print("---\nAvailable presets\n---\n")
    for name, expansion in sorted(presets.items()):
        print(f"  {name:<16} → {expansion}")


def print_list(node_map, axis_descriptions):
    print("---\nAvailable nodes\n---\n\nSliders — Side A / Center / Side B\n")
    axis_order = ["yellow", "red", "magenta", "green", "transparent", "white", "cyan", "blue", "purple"]
    axis_nodes = {}
    for node_name, info in node_map.items():
        axis = info["axis"]
        if axis not in axis_nodes:
            axis_nodes[axis] = {"pos": None, "neg": None}
        if info["polarity"] == 1:
            axis_nodes[axis]["pos"] = node_name.capitalize()
        else:
            axis_nodes[axis]["neg"] = node_name.capitalize()

    for axis in axis_order:
        nodes = axis_nodes.get(axis, {})
        neg = nodes.get("neg", "?")
        pos = nodes.get("pos", "?")
        center = axis.capitalize()
        print(f"  {neg:>8}(-1) ── {center:<13} (0) ── {pos:<8}(+1)")

    print(
        "\nAxis colors: yellow, red, magenta, green, transparent, white, cyan, blue, purple\n"
        "             (same as Side A/B node sliders; e.g. mtp yellow:70 = mtp open:70)\n"
        "             Type 'mtp help sliders' for details\n\n"
        "Grid: A–S × 1–19  (e.g. mtp G-10)\n"
        "      Type 'mtp help grid' for full grid reference\n\n"
        "Presets: 'mtp <preset-name>'  (e.g. mtp synthesizer)\n"
        "         Type 'mtp list presets' for available presets"
    )


def main():
    argparser = argparse.ArgumentParser(description="MTP compiler", add_help=False)
    argparser.add_argument(
        "--args", required=True,
        help="Raw /mtp arguments (e.g., 'power:30 flow:10', 'D:16 A:1', or 'G-10')",
    )
    cli_args = argparser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    nodes_dir = os.path.normpath(os.path.join(script_dir, "..", "nodes"))
    references_dir = os.path.normpath(os.path.join(script_dir, "..", "references"))

    node_map, axis_descriptions = build_node_map(nodes_dir)
    presets = load_presets(references_dir)

    args_stripped = " ".join(cli_args.args.strip().lower().split())
    if args_stripped in ("help", "--help", "-h"):
        print(load_help_text(references_dir, "help_main.txt"))
        sys.exit(0)
    if args_stripped == "help sliders":
        print(load_help_text(references_dir, "help_sliders.txt"))
        sys.exit(0)
    if args_stripped == "help grid":
        print(load_help_text(references_dir, "help_grid.txt"))
        sys.exit(0)
    if args_stripped == "help presets":
        _print_presets_table(presets)
        print("\nUsage: mtp <preset-name>  (e.g. mtp synthesizer)\n"
              "Explicit grid (same expansion as synthesizer): mtp D:16 A:1")
        sys.exit(0)
    if args_stripped == "list":
        print_list(node_map, axis_descriptions)
        sys.exit(0)
    if args_stripped == "list presets":
        _print_presets_table(presets)
        sys.exit(0)

    expanded_args = expand_presets(cli_args.args, presets)

    parsed_commands, invalid_tokens, neutral_tokens = parse_arguments(expanded_args, node_map)
    resolved_commands = resolve_conflicts(parsed_commands)

    _write_invalid_token_warnings(invalid_tokens)

    if resolved_commands:
        sys.stderr.write(_format_mtp_stderr_summary(resolved_commands) + "\n")
    elif not neutral_tokens and not invalid_tokens:
        sys.stderr.write(
            f"Warning: No valid MTP commands recognized in '{cli_args.args}'. Falling back to unconstrained output.\n"
        )

    if not resolved_commands:
        print("<mtp_node_shot>\n\n</mtp_node_shot>")
        sys.exit(0)

    print("<mtp_node_shot>")
    _print_mtp_constraint_preamble()

    for axis, polarity, intensity in resolved_commands:
        direction = "positive" if polarity > 0 else "negative"
        print(f'<constraints axis="{axis}" direction="{direction}" intensity="{intensity}">')

        constraints = extract_constraints(axis, polarity, intensity, nodes_dir)
        for constraint in constraints:
            print(f"  {constraint}")

        print("</constraints>\n")

    print("</mtp_node_shot>")


if __name__ == "__main__":
    main()
