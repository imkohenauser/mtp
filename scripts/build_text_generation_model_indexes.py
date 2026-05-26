#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT / "src" / "content" / "docs"
CASE_INDEX_GLOB = "**/comparisons/text-generation/*/index.md"

MARKER_START = "<!-- AUTO-GENERATED: model-output-indexes:start -->"
MARKER_END = "<!-- AUTO-GENERATED: model-output-indexes:end -->"

EXCLUDED_DIR_NAMES = {
    ".astro",
    "_astro",
    "assets",
    "dist",
    "image",
    "images",
    "node_modules",
    "public",
}

SECTION_ORDER = {
    "baseline": 0,
    "slider": 1,
    "grid": 2,
    "preset": 3,
}

ACRONYMS = {
    "ai": "AI",
    "api": "API",
    "gpt": "GPT",
    "ios": "iOS",
    "macos": "macOS",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, text: str) -> bool:
    if path.exists() and read_text(path) == text:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def is_japanese_case(case_dir: Path) -> bool:
    relative_parts = case_dir.relative_to(DOCS_ROOT).parts
    return bool(relative_parts) and relative_parts[0] == "ja"


def clean_model_name(value: str) -> str:
    without_html = re.sub(r"<[^>]+>", "", value)
    without_markdown = without_html.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", without_markdown).strip()


def readable_name_from_slug(slug: str) -> str:
    words = []
    for raw_word in re.split(r"[_-]+", slug):
        if not raw_word:
            continue
        lowered = raw_word.lower()
        words.append(ACRONYMS.get(lowered, lowered.capitalize()))
    return " ".join(words)


def split_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def extract_markdown_tables(lines: list[str]) -> list[tuple[list[str], list[list[str]]]]:
    tables: list[tuple[list[str], list[list[str]]]] = []
    index = 0

    while index + 1 < len(lines):
        header = split_table_row(lines[index])
        separator = split_table_row(lines[index + 1])
        if header is None or separator is None or not is_separator_row(separator):
            index += 1
            continue

        rows: list[list[str]] = []
        row_index = index + 2
        while row_index < len(lines):
            row = split_table_row(lines[row_index])
            if row is None:
                break
            rows.append(row)
            row_index += 1

        tables.append((header, rows))
        index = row_index

    return tables


def model_names_from_parent(parent_text: str, model_dir_names: list[str]) -> dict[str, str]:
    names: dict[str, str] = {}

    for header, rows in extract_markdown_tables(parent_text.splitlines()):
        for row in rows:
            for cell_index, cell in enumerate(row):
                if cell_index >= len(header):
                    continue
                candidate_name = clean_model_name(header[cell_index])
                if not candidate_name:
                    continue

                for href in re.findall(r"\[[^\]]+\]\(([^)]+)\)", cell):
                    for model_dir_name in model_dir_names:
                        if f"/{model_dir_name}/" in href and model_dir_name not in names:
                            names[model_dir_name] = candidate_name

    for model_dir_name in model_dir_names:
        names.setdefault(model_dir_name, readable_name_from_slug(model_dir_name))

    return names


def parent_link_order(parent_text: str, model_dir_name: str) -> dict[str, int]:
    order: dict[str, int] = {}

    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", parent_text):
        href = match.group(1).split("#", 1)[0].split("?", 1)[0]
        marker = f"/{model_dir_name}/"
        marker_index = href.find(marker)
        if marker_index == -1:
            continue

        suffix = href[marker_index + len(marker) :].strip("/")
        if not suffix:
            continue

        relative_md = f"{suffix}.md"
        order.setdefault(relative_md, len(order))

    return order


def source_sort_key(path: Path, model_dir: Path, parent_order: dict[str, int]) -> tuple[int, int, str]:
    relative = path.relative_to(model_dir).as_posix()
    first_part = path.relative_to(model_dir).parts[0]
    section_key = "baseline" if relative == "baseline.md" else first_part
    parent_index = parent_order.get(relative, 1_000_000)
    return (parent_index, SECTION_ORDER.get(section_key, 4), relative)


def discover_source_pages(model_dir: Path, parent_text: str) -> list[Path]:
    parent_order = parent_link_order(parent_text, model_dir.name)
    pages = []

    for path in model_dir.rglob("*.md"):
        if path.name == "index.md":
            continue
        relative_parts = path.relative_to(model_dir).parts
        if any(part.startswith(".") or part in EXCLUDED_DIR_NAMES for part in relative_parts):
            continue
        pages.append(path)

    return sorted(pages, key=lambda path: source_sort_key(path, model_dir, parent_order))


def discover_model_dirs(case_dir: Path, parent_text: str) -> list[Path]:
    candidates = []

    for child in case_dir.iterdir():
        if not child.is_dir():
            continue
        if child.name.startswith(".") or child.name in EXCLUDED_DIR_NAMES:
            continue
        if discover_source_pages(child, parent_text):
            candidates.append(child)

    def sort_key(model_dir: Path) -> tuple[int, str]:
        index = parent_text.find(f"/{model_dir.name}/")
        if index == -1:
            index = 1_000_000
        return (index, model_dir.name)

    return sorted(candidates, key=sort_key)


def is_fence_line(line: str) -> tuple[str, int] | None:
    match = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
    if not match:
        return None
    marker = match.group(1)
    return marker[0], len(marker)


def extract_output_section(path: Path, is_japanese: bool) -> str | None:
    lines = read_text(path).splitlines()
    heading_names = ("出力", "Output") if is_japanese else ("Output", "出力")
    heading_pattern = re.compile(r"^##\s+(" + "|".join(re.escape(name) for name in heading_names) + r")\s*$")

    fence: tuple[str, int] | None = None

    for line_index, line in enumerate(lines):
        fence_marker = is_fence_line(line)
        if fence_marker is not None:
            if fence is None:
                fence = fence_marker
            else:
                fence_char, fence_length = fence
                marker_char, marker_length = fence_marker
                if marker_char == fence_char and marker_length >= fence_length:
                    fence = None
            continue

        if fence is None and heading_pattern.fullmatch(line.strip()):
            output = "\n".join(lines[line_index + 1 :]).strip()
            return f"{output}\n" if output else ""

    return None


def extract_input_section_lines(lines: list[str], is_japanese: bool) -> list[str] | None:
    input_names = ("入力", "Input") if is_japanese else ("Input", "入力")
    output_names = ("出力", "Output") if is_japanese else ("Output", "出力")
    input_pattern = re.compile(r"^##\s+(" + "|".join(re.escape(name) for name in input_names) + r")\s*$")
    output_pattern = re.compile(r"^##\s+(" + "|".join(re.escape(name) for name in output_names) + r")\s*$")

    fence: tuple[str, int] | None = None
    input_start: int | None = None

    for line_index, line in enumerate(lines):
        fence_marker = is_fence_line(line)
        if fence_marker is not None:
            if fence is None:
                fence = fence_marker
            else:
                fence_char, fence_length = fence
                marker_char, marker_length = fence_marker
                if marker_char == fence_char and marker_length >= fence_length:
                    fence = None
            continue

        if fence is not None:
            continue

        stripped = line.strip()
        if input_start is None and input_pattern.fullmatch(stripped):
            input_start = line_index + 1
            continue

        if input_start is not None and output_pattern.fullmatch(stripped):
            return lines[input_start:line_index]

    return None


def extract_fixed_prompt(path: Path, is_japanese: bool) -> str | None:
    if not path.exists():
        return None

    lines = read_text(path).splitlines()
    input_lines = extract_input_section_lines(lines, is_japanese)
    if not input_lines:
        return None

    prompt_labels = ("プロンプト", "Prompt") if is_japanese else ("Prompt", "プロンプト")
    prompt_label_pattern = re.compile(
        r"^\*\*(" + "|".join(re.escape(label) for label in prompt_labels) + r")\*\*\s*$"
    )

    label_index: int | None = None
    for line_index, line in enumerate(input_lines):
        if prompt_label_pattern.fullmatch(line.strip()):
            label_index = line_index
            break

    if label_index is None:
        return None

    fence: tuple[str, int] | None = None
    for line_index in range(label_index + 1, len(input_lines)):
        line = input_lines[line_index]
        fence_marker = is_fence_line(line)
        if fence_marker is not None:
            if fence is None:
                fence = fence_marker
                prompt_start = line_index + 1
            else:
                fence_char, fence_length = fence
                marker_char, marker_length = fence_marker
                if marker_char == fence_char and marker_length >= fence_length:
                    prompt_body = "\n".join(input_lines[prompt_start:line_index]).rstrip()
                    return f"{prompt_body}\n" if prompt_body else ""
                fence = None

    return None


def section_title(source_path: Path, model_dir: Path) -> str:
    relative_without_suffix = source_path.relative_to(model_dir).with_suffix("")
    return " / ".join(relative_without_suffix.parts)


def render_missing_output_notice(is_japanese: bool) -> str:
    if is_japanese:
        return "> このソースファイルでは出力セクションが見つかりませんでした。"
    return "> Output section was not found in this source file."


def render_missing_prompt_notice(is_japanese: bool) -> str:
    if is_japanese:
        return "> `baseline.md` から固定プロンプトを取得できませんでした。"
    return "> Fixed prompt could not be extracted from `baseline.md`."


def format_prompt_block(prompt_body: str) -> str:
    return "```markdown\n" + prompt_body.rstrip() + "\n```"


def render_model_index(case_dir: Path, model_dir: Path, model_name: str, pages: list[Path], is_japanese: bool) -> str:
    if is_japanese:
        suffix = "統合出力"
        description = f"この比較に含まれる {model_name} の出力部分を統合した AI 分析用ページです。"
        intro = "このページは、個別比較ページの `## 出力` セクションのみをモデル別に統合したものです。"
        comparison_page = "比較ページ"
        model_directory = "モデルディレクトリ"
        fixed_prompt_heading = "固定プロンプト"
        output_listing_heading = "出力一覧"
    else:
        suffix = "Integrated output"
        description = "A model-level integrated page containing only the output sections from this comparison."
        intro = "This page combines only the `## Output` sections from the individual result pages for this model."
        comparison_page = "Comparison page"
        model_directory = "Model directory"
        fixed_prompt_heading = "Fixed prompt"
        output_listing_heading = "Output listing"

    title = f"{model_name} | {suffix}"
    lines = [
        "---",
        f"title: {yaml_string(title)}",
        f"description: {yaml_string(description)}",
        "lastUpdated: true",
        "---",
        "",
        intro,
        "",
        f"- {comparison_page}: `../index.md`",
        f"- {model_directory}: `{model_dir.name}`",
        "",
        "---",
        "",
        f"## {fixed_prompt_heading}",
        "",
    ]

    fixed_prompt = extract_fixed_prompt(model_dir / "baseline.md", is_japanese)
    if fixed_prompt is not None:
        lines.append(format_prompt_block(fixed_prompt))
    else:
        lines.append(render_missing_prompt_notice(is_japanese))

    lines.extend(
        [
            "",
            "---",
            "",
            f"## {output_listing_heading}",
            "",
        ]
    )

    for page in pages:
        relative_source = page.relative_to(model_dir).as_posix()
        extracted_output = extract_output_section(page, is_japanese)
        lines.extend(
            [
                f"### {section_title(page, model_dir)}",
                "",
                f"Source: `{relative_source}`",
                "",
                "<!-- extracted output follows -->",
                "",
                (extracted_output.rstrip() if extracted_output is not None else render_missing_output_notice(is_japanese)),
                "",
                "---",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def escape_table_cell(value: str) -> str:
    return value.replace("|", r"\|")


def route_for(case_dir: Path, model_dir: Path) -> str:
    case_route = case_dir.relative_to(DOCS_ROOT).as_posix()
    return f"/{case_route}/{model_dir.name}/"


def render_parent_link_block(
    case_dir: Path,
    model_dirs: list[Path],
    model_names: dict[str, str],
    is_japanese: bool,
) -> str:
    if is_japanese:
        heading = "### モデル別統合出力"
        description = "各モデルの出力部分だけを統合した、AI 分析用ページです。"
        link_text = "統合出力"
    else:
        heading = "### Integrated outputs by model"
        description = (
            "These pages combine only the output sections for each model, making them easier "
            "to inspect manually or analyze with an AI assistant."
        )
        link_text = "Integrated output"

    headers = [escape_table_cell(model_names[model_dir.name]) for model_dir in model_dirs]
    links = [f"[{link_text}]({route_for(case_dir, model_dir)})" for model_dir in model_dirs]

    lines = [
        MARKER_START,
        heading,
        "",
        description,
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
        "| " + " | ".join(links) + " |",
    ]

    lines.append(MARKER_END)
    return "\n".join(lines)


def parent_link_block_pattern() -> re.Pattern[str]:
    return re.compile(
        re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
        re.DOTALL,
    )


def remove_parent_link_block(parent_text: str) -> str:
    return parent_link_block_pattern().sub("", parent_text)


def insert_or_replace_parent_link_block(parent_text: str, block: str, is_japanese: bool) -> str:
    marker_pattern = parent_link_block_pattern()
    if marker_pattern.search(parent_text):
        return marker_pattern.sub(block, parent_text)

    baseline_heading = "ベースライン" if is_japanese else "Baseline"
    baseline_match = re.search(rf"^###\s+{re.escape(baseline_heading)}\s*$", parent_text, re.MULTILINE)
    if baseline_match:
        return (
            parent_text[: baseline_match.start()].rstrip()
            + "\n\n"
            + block
            + "\n\n"
            + parent_text[baseline_match.start() :].lstrip("\n")
        )

    return parent_text.rstrip() + "\n\n" + block + "\n"


def process_case(case_index: Path) -> tuple[int, int, int]:
    case_dir = case_index.parent
    is_japanese = is_japanese_case(case_dir)
    parent_text = read_text(case_index)
    parent_source_text = remove_parent_link_block(parent_text)
    model_dirs = discover_model_dirs(case_dir, parent_source_text)
    model_names = model_names_from_parent(parent_source_text, [model_dir.name for model_dir in model_dirs])

    model_indexes_changed = 0
    missing_outputs = 0

    for model_dir in model_dirs:
        pages = discover_source_pages(model_dir, parent_source_text)
        for page in pages:
            if extract_output_section(page, is_japanese) is None:
                missing_outputs += 1

        model_index = render_model_index(
            case_dir=case_dir,
            model_dir=model_dir,
            model_name=model_names[model_dir.name],
            pages=pages,
            is_japanese=is_japanese,
        )
        if write_if_changed(model_dir / "index.md", model_index):
            model_indexes_changed += 1

    parent_block = render_parent_link_block(case_dir, model_dirs, model_names, is_japanese)
    new_parent_text = insert_or_replace_parent_link_block(parent_text, parent_block, is_japanese)
    parent_changed = 1 if write_if_changed(case_index, new_parent_text) else 0

    return model_indexes_changed, parent_changed, missing_outputs


def main() -> None:
    case_indexes = sorted(DOCS_ROOT.glob(CASE_INDEX_GLOB))
    model_indexes_changed = 0
    parent_indexes_changed = 0
    missing_outputs = 0

    for case_index in case_indexes:
        changed_models, changed_parent, missing = process_case(case_index)
        model_indexes_changed += changed_models
        parent_indexes_changed += changed_parent
        missing_outputs += missing

    print(
        "Processed "
        f"{len(case_indexes)} comparison cases; "
        f"{model_indexes_changed} model index files changed; "
        f"{parent_indexes_changed} parent index files changed; "
        f"{missing_outputs} source files without output sections."
    )


if __name__ == "__main__":
    main()
