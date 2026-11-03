#!/usr/bin/env python3
"""Synchronize AIDR-SPECIFICATION.md (ground truth) into index.html.

Zero-dependency Python 3 script that validates AIDR-SPECIFICATION.md against
structural and stylistic rules, then updates all marked regions of index.html
(Tab 1 full specification, Tab 2 Ideation/Execution level buttons, header/footer
metadata, and the JavaScript SPEC_DATA object driving generated disclosures).

Usage:
  python sync_spec.py           # Validate spec and update index.html in-place
  python sync_spec.py --check   # Dry-run check (exit 0 if synced, 1 otherwise)
  python sync_spec.py --watch   # Watch AIDR-SPECIFICATION.md and auto-sync
"""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
import re
import sys
import time
from typing import Any


DEFAULT_SPEC_FILENAME = "AIDR-SPECIFICATION.md"
DEFAULT_HTML_FILENAME = "index.html"

REQUIRED_META_KEYS = (
    "Version",
    "Status",
    "Author",
    "Date",
    "Specification License",
    "Templates, Badges & Header Tags License",
)

# Default initial selected levels rendered into static HTML before JS runs
DEFAULT_SELECTED_IDEATIONS = {0, 1}
DEFAULT_SELECTED_EXECUTIONS = {0, 3}


class SpecValidationError(Exception):
    """Raised when AIDR-SPECIFICATION.md or index.html fails validation."""


def validate_stylistic_rules(spec_text: str) -> None:
    """Enforce strict fail-fast stylistic invariants on AIDR-SPECIFICATION.md."""
    violations: list[str] = []
    checks: list[tuple[re.Pattern[str], str]] = [
        (
            re.compile(r"\u2014|&mdash;", re.IGNORECASE),
            "Em-dash detected (forbidden by specification style rules)",
        ),
        (
            re.compile(r"\u2013|&ndash;", re.IGNORECASE),
            "En-dash detected (forbidden by specification style rules)",
        ),
        (
            re.compile(r"\bax(?:is|es)\b", re.IGNORECASE),
            "Deprecated term 'axis'/'axes' detected (use 'categories' or 'levels')",
        ),
        (
            re.compile(r"\b5\s*(?:[x\u00d7]|&times;)\s*5\b", re.IGNORECASE),
            "Deprecated '5x5' matrix reference detected",
        ),
        (
            re.compile(r"\bAIDE\b"),
            "Legacy acronym 'AIDE' detected (use 'AIDR')",
        ),
    ]

    for idx, line in enumerate(spec_text.splitlines(), start=1):
        for pattern, message in checks:
            if pattern.search(line):
                snippet = line.strip()
                if len(snippet) > 90:
                    snippet = snippet[:87] + "..."
                violations.append(f"  Line {idx}: {message}: {snippet}")

    if violations:
        joined = "\n".join(violations)
        raise SpecValidationError(
            f"Stylistic validation failed in specification:\n{joined}"
        )


def split_top_level_sections(spec_text: str) -> list[list[str]]:
    """Split Markdown lines on top-level '---' dividers outside fenced code blocks."""
    sections: list[list[str]] = []
    current: list[str] = []
    in_fence = False
    fence_char = ""
    fence_len = 0

    for line in spec_text.splitlines():
        fence_match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence_match:
            ticks = fence_match.group(1)
            rest = fence_match.group(2).strip()
            if not in_fence:
                in_fence = True
                fence_char = ticks[0]
                fence_len = len(ticks)
            elif ticks[0] == fence_char and len(ticks) >= fence_len and not rest:
                in_fence = False
                fence_char = ""
                fence_len = 0
            current.append(line)
            continue

        if not in_fence and re.match(r"^\s*-{3,}\s*$", line):
            sections.append(current)
            current = []
        else:
            current.append(line)

    if in_fence:
        raise SpecValidationError("Unclosed fenced code block in specification.")

    sections.append(current)
    # Remove trailing empty section if file ends with ---
    while len(sections) > 1 and all(not ln.strip() for ln in sections[-1]):
        sections.pop()

    if len(sections) < 2:
        raise SpecValidationError(
            "Specification must contain a top metadata section and at least one "
            "body section separated by '---'."
        )
    return sections


def strip_markdown_inline(text: str) -> str:
    """Strip inline Markdown emphasis, code ticks, and links to plain text."""
    out = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    out = re.sub(r"`([^`]+)`", r"\1", out)
    out = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", out)
    out = re.sub(r"<([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})>", r"\1", out)
    out = re.sub(r"\*\*\*(.+?)\*\*\*", r"\1", out)
    out = re.sub(r"\*\*(.+?)\*\*", r"\1", out)
    out = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"\1", out)
    return out.strip()


def render_inline(text: str) -> str:
    """Convert inline Markdown syntax to safe, properly escaped HTML."""
    tokens: list[str] = []

    def stash(html_fragment: str) -> str:
        idx = len(tokens)
        tokens.append(html_fragment)
        return f"\x00TOK{idx}\x00"

    def restore(val: str) -> str:
        # Restore iteratively so nested tokens (e.g. code inside link labels) expand.
        prev = None
        while prev != val and "\x00TOK" in val:
            prev = val
            val = re.sub(
                r"\x00TOK(\d+)\x00",
                lambda m: tokens[int(m.group(1))],
                val,
            )
        return val

    def apply_emphasis(escaped_str: str) -> str:
        s = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", escaped_str)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", s)
        return s

    work = text

    # 1. Inline code spans `...`
    work = re.sub(
        r"`([^`]+)`",
        lambda m: stash(f"<code>{html.escape(m.group(1), quote=False)}</code>"),
        work,
    )

    # 2. Explicit <br> tags
    work = re.sub(
        r"<br\s*/?>",
        lambda _: stash("<br>"),
        work,
        flags=re.IGNORECASE,
    )

    # 3. Email autolinks <user@example.com>
    def replace_email(match: re.Match[str]) -> str:
        addr_attr = html.escape(match.group(1), quote=True)
        addr_text = html.escape(match.group(1), quote=False)
        return stash(f'<a href="mailto:{addr_attr}">{addr_text}</a>')

    work = re.sub(
        r"<([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})>",
        replace_email,
        work,
    )

    # 4. URL autolinks <https://...>
    def replace_autourl(match: re.Match[str]) -> str:
        url_attr = html.escape(match.group(1), quote=True)
        url_text = html.escape(match.group(1), quote=False)
        return stash(
            f'<a href="{url_attr}" target="_blank" rel="noopener">{url_text}</a>'
        )

    work = re.sub(r"<(https?://[^\s>]+)>", replace_autourl, work)

    # 5. Standard Markdown links [label](url)
    def replace_link(match: re.Match[str]) -> str:
        raw_label = match.group(1)
        raw_url = match.group(2).strip()
        url_attr = html.escape(raw_url, quote=True)
        label_html = apply_emphasis(html.escape(raw_label, quote=False))
        ext_attrs = (
            ' target="_blank" rel="noopener"'
            if raw_url.startswith(("http://", "https://"))
            else ""
        )
        return stash(f'<a href="{url_attr}"{ext_attrs}>{label_html}</a>')

    work = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_link, work)

    # 6. Escape remaining raw characters and apply bold/italic + hard line breaks
    work = html.escape(work, quote=False)
    work = apply_emphasis(work)
    work = work.replace("  \n", "<br>\n")

    # 7. Restore all stashed HTML fragments
    return restore(work)


def parse_header_chunk(lines: list[str]) -> dict[str, Any]:
    """Parse Chunk 0 (# H1 title and **Key:** Value metadata lines)."""
    raw_h1: str | None = None
    meta_items: list[tuple[str, str]] = []
    meta_map: dict[str, str] = {}
    extra_lines: list[str] = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if raw_h1 is None and stripped.startswith("# "):
            raw_h1 = stripped[2:].strip()
            continue

        meta_match = re.match(r"^\*\*([^*]+?):\*\*\s*(.+?)\s*$", stripped)
        if meta_match:
            key = meta_match.group(1).strip()
            val = meta_match.group(2).strip()
            meta_items.append((key, val))
            meta_map[key] = val
            continue

        extra_lines.append(line)

    if not raw_h1:
        raise SpecValidationError(
            "Top section of specification must begin with a '# ' H1 heading."
        )

    missing_keys = [k for k in REQUIRED_META_KEYS if not meta_map.get(k)]
    if missing_keys:
        raise SpecValidationError(
            "Missing required header metadata field(s) in specification: "
            + ", ".join(missing_keys)
        )

    display_h1 = re.sub(
        r",\s*Specification\b.*$", "", raw_h1, flags=re.IGNORECASE
    ).strip()
    if ":" in display_h1:
        acronym, full_name = [part.strip() for part in display_h1.split(":", 1)]
    else:
        acronym = "AIDR"
        full_name = display_h1

    return {
        "raw_h1": raw_h1,
        "display_h1": display_h1,
        "acronym": acronym,
        "full_name": full_name,
        "meta_items": meta_items,
        "meta_map": meta_map,
        "extra_lines": extra_lines,
    }


def split_pipe_row(line: str) -> list[str]:
    """Split a Markdown pipe-table row into trimmed cell strings."""
    inner = line.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|") and not inner.endswith(r"\|"):
        inner = inner[:-1]
    cells = re.split(r"(?<!\\)\|", inner)
    return [c.replace(r"\|", "|").strip() for c in cells]


def is_table_separator(line: str) -> bool:
    """Return True if line is a GFM pipe-table alignment/separator row."""
    return bool(
        re.match(
            r"^\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*:?-{3,}:?\s*\|?\s*$",
            line,
        )
    )


def match_list_item(line: str) -> tuple[str, int, int, str] | None:
    """Match an unordered or ordered list item line.

    Returns (list_type, indent, content_indent, first_line_content) or None.
    """
    ul_match = re.match(r"^(\s*)([-*])\s+(.*)$", line)
    if ul_match:
        indent = len(ul_match.group(1))
        content_indent = indent + len(ul_match.group(2)) + 1
        # Account for extra spaces after marker
        prefix_match = re.match(r"^(\s*[-*]\s+)", line)
        if prefix_match:
            content_indent = len(prefix_match.group(1))
        return ("ul", indent, content_indent, ul_match.group(3))

    ol_match = re.match(r"^(\s*)(\d+\.)\s+(.*)$", line)
    if ol_match:
        indent = len(ol_match.group(1))
        prefix_match = re.match(r"^(\s*\d+\.\s+)", line)
        content_indent = (
            len(prefix_match.group(1))
            if prefix_match
            else indent + len(ol_match.group(2)) + 1
        )
        return ("ol", indent, content_indent, ol_match.group(3))

    return None


def is_block_start(lines: list[str], idx: int) -> bool:
    """Return True if lines[idx] begins a non-paragraph Markdown block."""
    line = lines[idx]
    stripped = line.strip()
    if not stripped:
        return True
    if re.match(r"^\s*(`{3,}|~{3,})", line):
        return True
    if re.match(r"^\s*#{1,6}\s+", line):
        return True
    if re.match(r"^\s*>\s?", line):
        return True
    if re.match(r"^\s*-{3,}\s*$", line):
        return True
    if match_list_item(line) is not None:
        return True
    if (
        "|" in line
        and idx + 1 < len(lines)
        and is_table_separator(lines[idx + 1])
    ):
        return True
    return False


def indent_block(html_text: str, spaces: int) -> str:
    """Indent non-empty lines of an HTML block except inside <pre>...</pre>."""
    pad = " " * spaces
    out: list[str] = []
    in_pre = False
    for line in html_text.splitlines():
        if not in_pre:
            out.append((pad + line) if line else "")
            if "<pre>" in line and "</pre>" not in line:
                in_pre = True
        else:
            out.append(line)
            if "</pre>" in line:
                in_pre = False
    return "\n".join(out)


def render_blocks(
    lines: list[str],
    level_collector: dict[str, dict[int, dict[str, str]]] | None = None,
    in_list_item: bool = False,
) -> str:
    """Render a list of Markdown lines to semantic HTML blocks."""
    blocks: list[tuple[str, str]] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # 1. Fenced code block
        fence_match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence_match:
            ticks = fence_match.group(1)
            fence_char = ticks[0]
            fence_len = len(ticks)
            code_lines: list[str] = []
            i += 1
            while i < n:
                close_match = re.match(r"^\s*(`{3,}|~{3,})\s*$", lines[i])
                if (
                    close_match
                    and close_match.group(1)[0] == fence_char
                    and len(close_match.group(1)) >= fence_len
                ):
                    i += 1
                    break
                code_lines.append(lines[i])
                i += 1
            escaped_code = html.escape("\n".join(code_lines), quote=False)
            blocks.append(("pre", f"<pre><code>{escaped_code}</code></pre>"))
            continue

        # 2. Headings (# through ####)
        heading_match = re.match(r"^\s*(#{1,6})\s+(.+?)\s*$", line)
        if heading_match:
            hashes = len(heading_match.group(1))
            content_html = render_inline(heading_match.group(2))
            tag_level = min(max(hashes, 2), 4)
            if tag_level == 2:
                blocks.append(("h2", f"<h2><span>{content_html}</span></h2>"))
            else:
                blocks.append((f"h{tag_level}", f"<h{tag_level}>{content_html}</h{tag_level}>"))
            i += 1
            continue

        # 3. GFM Pipe Table
        if "|" in line and i + 1 < n and is_table_separator(lines[i + 1]):
            headers = split_pipe_row(line)
            i += 2  # Skip header and separator rows
            body_rows: list[list[str]] = []
            while i < n and lines[i].strip() and "|" in lines[i]:
                body_rows.append(split_pipe_row(lines[i]))
                i += 1

            th_cells = "\n".join(
                f"      <th>{render_inline(h)}</th>" for h in headers
            )
            tr_html_list: list[str] = []
            for row in body_rows:
                # Pad or trim row to match header count
                padded = row + [""] * max(0, len(headers) - len(row))
                clean_first = re.sub(r"[*`\s]", "", padded[0])
                lvl_match = re.match(r"^([IE])([0-4])$", clean_first)

                if lvl_match and level_collector is not None:
                    cat_letter = lvl_match.group(1)
                    lvl_num = int(lvl_match.group(2))
                    if len(padded) < 4:
                        raise SpecValidationError(
                            f"Table row for {clean_first} must have at least 4 columns "
                            "(Level, Title, Definition, Examples)."
                        )
                    plain_title = strip_markdown_inline(padded[1])
                    raw_def_cell = padded[2].strip()
                    norm_def_md = re.sub(
                        r"\s*<br\s*/?>\s*", " ", raw_def_cell, flags=re.IGNORECASE
                    ).strip()
                    html_def = render_inline(raw_def_cell)
                    raw_examples = padded[3].strip()

                    if not plain_title or not norm_def_md or not raw_examples:
                        raise SpecValidationError(
                            f"Table row for {clean_first} contains an empty Title, "
                            "Definition, or Examples cell."
                        )

                    bucket = level_collector[cat_letter]
                    if lvl_num in bucket:
                        raise SpecValidationError(
                            f"Duplicate level definition row found for {clean_first}."
                        )
                    bucket[lvl_num] = {
                        "code": clean_first,
                        "title": plain_title,
                        "definition_md": norm_def_md,
                        "definition_html": html_def,
                    }

                td_parts: list[str] = []
                for col_idx, cell_val in enumerate(padded[: len(headers)]):
                    if col_idx == 0 and lvl_match:
                        code_str = f"{lvl_match.group(1)}{lvl_match.group(2)}"
                        digit_str = lvl_match.group(2)
                        td_parts.append(
                            f'      <td><span class="lvl-badge b-{digit_str}">'
                            f"{code_str}</span></td>"
                        )
                    else:
                        td_parts.append(f"      <td>{render_inline(cell_val)}</td>")
                tr_html_list.append("    <tr>\n" + "\n".join(td_parts) + "\n    </tr>")

            tbody_inner = "\n".join(tr_html_list)
            table_html = (
                '<table class="spec-table">\n'
                "  <thead>\n"
                "    <tr>\n"
                f"{th_cells}\n"
                "    </tr>\n"
                "  </thead>\n"
                "  <tbody>\n"
                f"{tbody_inner}\n"
                "  </tbody>\n"
                "</table>"
            )
            blocks.append(("table", table_html))
            continue

        # 4. Blockquote
        if re.match(r"^\s*>\s?", line):
            quote_lines: list[str] = []
            while i < n and re.match(r"^\s*>\s?", lines[i]):
                quote_lines.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            inner_quote = render_blocks(quote_lines, level_collector=level_collector)
            blocks.append(
                ("blockquote", f"<blockquote>\n{indent_block(inner_quote, 2)}\n</blockquote>")
            )
            continue

        # 5. Lists (ul / ol) with indented continuations and nested sublists
        first_item = match_list_item(line)
        if first_item is not None:
            list_type, base_indent, _, _ = first_item
            items_html: list[str] = []

            while i < n:
                curr_match = match_list_item(lines[i])
                if (
                    curr_match is None
                    or curr_match[0] != list_type
                    or curr_match[1] != base_indent
                ):
                    break

                _, _, content_indent, first_content = curr_match
                item_lines: list[str] = [first_content]
                i += 1

                while i < n:
                    next_line = lines[i]
                    if not next_line.strip():
                        # Peek ahead to next non-blank line
                        peek = i + 1
                        while peek < n and not lines[peek].strip():
                            peek += 1
                        if peek < n:
                            peek_indent = len(lines[peek]) - len(lines[peek].lstrip(" "))
                            if peek_indent >= content_indent:
                                item_lines.append("")
                                i += 1
                                continue
                        break

                    line_indent = len(next_line) - len(next_line.lstrip(" "))
                    if line_indent >= content_indent:
                        item_lines.append(next_line[content_indent:])
                        i += 1
                    else:
                        break

                # Skip blank lines between sibling items of the same list
                peek = i
                while peek < n and not lines[peek].strip():
                    peek += 1
                if peek < n:
                    sibling = match_list_item(lines[peek])
                    if (
                        sibling is not None
                        and sibling[0] == list_type
                        and sibling[1] == base_indent
                    ):
                        i = peek

                rendered_item = render_blocks(
                    item_lines,
                    level_collector=level_collector,
                    in_list_item=True,
                )
                if "\n" in rendered_item:
                    items_html.append(
                        f"  <li>\n{indent_block(rendered_item, 4)}\n  </li>"
                    )
                else:
                    items_html.append(f"  <li>{rendered_item}</li>")

            list_body = "\n".join(items_html)
            blocks.append((list_type, f"<{list_type}>\n{list_body}\n</{list_type}>"))
            continue

        # 6. Paragraph
        para_lines: list[str] = [line.strip()]
        i += 1
        while i < n and not is_block_start(lines, i):
            para_lines.append(lines[i].strip())
            i += 1
        # Preserve trailing double-space hard breaks if present on source lines
        para_inline = render_inline(" ".join(para_lines))
        blocks.append(("p", para_inline))

    # Format paragraphs depending on whether this is a compact list item
    para_count = sum(1 for kind, _ in blocks if kind == "p")
    rendered_parts: list[str] = []
    for kind, content in blocks:
        if kind == "p":
            if in_list_item and para_count == 1:
                rendered_parts.append(content)
            else:
                rendered_parts.append(f"<p>{content}</p>")
        else:
            rendered_parts.append(content)

    return "\n".join(rendered_parts)


def parse_and_compile_spec(spec_text: str) -> dict[str, Any]:
    """Validate AIDR-SPECIFICATION.md and compile all synced HTML & JS fragments."""
    validate_stylistic_rules(spec_text)
    sections = split_top_level_sections(spec_text)
    header_info = parse_header_chunk(sections[0])

    level_collector: dict[str, dict[int, dict[str, str]]] = {"I": {}, "E": {}}

    # Build .meta-grid HTML from all header metadata entries
    meta_items_html: list[str] = []
    for key, val in header_info["meta_items"]:
        key_html = render_inline(key)
        val_html = render_inline(val)
        meta_items_html.append(
            '        <div class="meta-item">\n'
            f"          <strong>{key_html}</strong>\n"
            f"          <span>{val_html}</span>\n"
            "        </div>"
        )
    meta_grid_html = (
        '      <div class="meta-grid">\n'
        + "\n".join(meta_items_html)
        + "\n      </div>"
    )

    extra_preamble_html = ""
    if header_info["extra_lines"]:
        rendered_extra = render_blocks(
            header_info["extra_lines"], level_collector=level_collector
        )
        if rendered_extra:
            extra_preamble_html = "\n" + indent_block(rendered_extra, 6)

    # Render each '---'-delimited body section into its own .card container
    cards_html: list[str] = []
    for sec_idx, sec_lines in enumerate(sections[1:]):
        body_html = render_blocks(sec_lines, level_collector=level_collector)
        if not body_html.strip():
            continue
        indented_body = indent_block(body_html, 6)
        if sec_idx == 0:
            card_html = (
                '    <div class="card">\n'
                f"{meta_grid_html}{extra_preamble_html}\n\n"
                f"{indented_body}\n"
                "    </div>"
            )
        else:
            card_html = f'    <div class="card">\n{indented_body}\n    </div>'
        cards_html.append(card_html)

    # Structural validation of Ideation (I0..I4) and Execution (E0..E4) tables
    expected_levels = {0, 1, 2, 3, 4}
    for prefix, label in (("I", "Ideation"), ("E", "Execution")):
        found = set(level_collector[prefix].keys())
        missing = sorted(expected_levels - found)
        if missing:
            missing_codes = ", ".join(f"{prefix}{m}" for m in missing)
            raise SpecValidationError(
                f"Specification {label} table is missing required level row(s): "
                f"{missing_codes}"
            )

    ideation_rows = [level_collector["I"][n] for n in range(5)]
    execution_rows = [level_collector["E"][n] for n in range(5)]

    # Build Tab 2 Section 1 option cards (#ideation-options and #execution-options)
    def build_option_cards(
        rows: list[dict[str, str]],
        toggle_fn: str,
        default_selected: set[int],
    ) -> str:
        option_blocks: list[str] = []
        for lvl_idx, row in enumerate(rows):
            sel_cls = " selected" if lvl_idx in default_selected else ""
            title_html = html.escape(row["title"], quote=False)
            def_html = row["definition_html"]
            code_html = html.escape(row["code"], quote=False)
            option_blocks.append(
                f'            <div class="level-option{sel_cls}" data-level="{lvl_idx}" '
                f'onclick="{toggle_fn}({lvl_idx})">\n'
                f'              <span class="lvl-badge b-{lvl_idx}">{code_html}</span>\n'
                '              <div class="level-info">\n'
                f"                <strong>{title_html}</strong>\n"
                f"                <span>{def_html}</span>\n"
                "              </div>\n"
                "            </div>"
            )
        return "\n".join(option_blocks)

    ideation_options_html = build_option_cards(
        ideation_rows, "toggleIdeation", DEFAULT_SELECTED_IDEATIONS
    )
    execution_options_html = build_option_cards(
        execution_rows, "toggleExecution", DEFAULT_SELECTED_EXECUTIONS
    )

    # Header, Title, Tab 1 button, and Footer fragments
    acronym = header_info["acronym"]
    full_name = header_info["full_name"]
    display_h1 = header_info["display_h1"]
    meta_map = header_info["meta_map"]
    version = strip_markdown_inline(meta_map["Version"])

    head_title_html = (
        f"  <title>{html.escape(acronym, quote=False)} "
        f"v{html.escape(version, quote=False)}: "
        f"{html.escape(full_name, quote=False)}</title>"
    )
    version_pill_html = (
        f'      <span class="version-pill">'
        f"{html.escape(acronym, quote=False)} Standard "
        f"v{html.escape(version, quote=False)}</span>"
    )
    header_h1_html = f"    <h1>{html.escape(display_h1, quote=False)}</h1>"
    tab1_btn_html = (
        '      <button class="tab-btn active" onclick="switchTab(\'spec\', this)">'
        f"Full v{html.escape(version, quote=False)} Specification</button>"
    )

    author_html = render_inline(meta_map["Author"])
    spec_license_html = render_inline(meta_map["Specification License"])
    templates_license_html = render_inline(
        meta_map["Templates, Badges & Header Tags License"]
    )
    footer_html = (
        "    <p>\n"
        f"      <strong>{html.escape(acronym, quote=False)} Specification "
        f"v{html.escape(version, quote=False)}</strong> by {author_html} "
        f"is licensed under {spec_license_html}.<br>\n"
        "      All generated badges, disclosure snippets, and metadata header tags "
        f"are dedicated to the public domain under {templates_license_html}.\n"
        "    </p>"
    )

    # JavaScript SPEC_DATA constant
    spec_data_obj = {
        "acronym": acronym,
        "fullName": full_name,
        "version": version,
        "ideationTitles": [r["title"] for r in ideation_rows],
        "executionTitles": [r["title"] for r in execution_rows],
        "ideationDefinitions": [r["definition_md"] for r in ideation_rows],
        "executionDefinitions": [r["definition_md"] for r in execution_rows],
    }
    json_lines = (
        json.dumps(spec_data_obj, indent=2, ensure_ascii=False)
        .replace("</", r"<\/")
        .splitlines()
    )
    indented_json = "\n".join(
        (f"  {ln}" if idx > 0 else ln) for idx, ln in enumerate(json_lines)
    )
    spec_data_js = f"  const SPEC_DATA = {indented_json};"

    return {
        "HEAD-TITLE": head_title_html,
        "VERSION-PILL": version_pill_html,
        "HEADER-H1": header_h1_html,
        "TAB1-BTN": tab1_btn_html,
        "TAB-SPEC": "\n\n".join(cards_html),
        "IDEATION-OPTIONS": ideation_options_html,
        "EXECUTION-OPTIONS": execution_options_html,
        "FOOTER": footer_html,
        "SPEC-DATA": spec_data_js,
    }


def replace_synced_region(
    doc_text: str,
    marker_name: str,
    replacement_body: str,
    comment_style: str = "html",
) -> str:
    """Replace content between SYNC:<marker_name>:START and END markers."""
    if comment_style == "html":
        start_tag = f"<!-- SYNC:{marker_name}:START -->"
        end_tag = f"<!-- SYNC:{marker_name}:END -->"
    elif comment_style == "js":
        start_tag = f"/* SYNC:{marker_name}:START */"
        end_tag = f"/* SYNC:{marker_name}:END */"
    else:
        raise ValueError(f"Unsupported comment style: {comment_style}")

    start_count = doc_text.count(start_tag)
    end_count = doc_text.count(end_tag)
    if start_count != 1 or end_count != 1:
        raise SpecValidationError(
            f"Expected exactly 1 pair of {start_tag} / {end_tag} markers in "
            f"target HTML, found start={start_count}, end={end_count}."
        )

    pattern = re.compile(
        r"(^[ \t]*" + re.escape(start_tag) + r"[ \t]*\n)"
        r"(.*?)"
        r"(^[ \t]*" + re.escape(end_tag) + r"[ \t]*$)",
        re.DOTALL | re.MULTILINE,
    )
    match = pattern.search(doc_text)
    if not match:
        raise SpecValidationError(
            f"Marker block {marker_name} is malformed or out of order in target HTML."
        )

    return (
        doc_text[: match.start()]
        + match.group(1)
        + replacement_body
        + "\n"
        + match.group(3)
        + doc_text[match.end() :]
    )


def build_synced_html(spec_text: str, html_text: str) -> str:
    """Return updated index.html string synchronized with spec_text."""
    fragments = parse_and_compile_spec(spec_text)
    updated = html_text

    html_markers = (
        "HEAD-TITLE",
        "VERSION-PILL",
        "HEADER-H1",
        "TAB1-BTN",
        "TAB-SPEC",
        "IDEATION-OPTIONS",
        "EXECUTION-OPTIONS",
        "FOOTER",
    )
    for name in html_markers:
        updated = replace_synced_region(updated, name, fragments[name], "html")

    updated = replace_synced_region(updated, "SPEC-DATA", fragments["SPEC-DATA"], "js")
    return updated


def sync_once(spec_path: Path, html_path: Path, check_only: bool = False) -> bool:
    """Perform a single validation + sync pass.

    Returns True if html_path was modified (or needed modification in --check mode),
    False if html_path was already completely in sync.
    """
    if not spec_path.is_file():
        raise SpecValidationError(f"Specification file not found: {spec_path}")
    if not html_path.is_file():
        raise SpecValidationError(f"Target HTML file not found: {html_path}")

    raw_spec = spec_path.read_bytes().decode("utf-8")
    raw_html = html_path.read_bytes().decode("utf-8")

    eol = "\r\n" if "\r\n" in raw_html else "\n"
    norm_spec = raw_spec.replace("\r\n", "\n")
    norm_html = raw_html.replace("\r\n", "\n")

    synced_norm_html = build_synced_html(norm_spec, norm_html)
    synced_raw_html = (
        synced_norm_html.replace("\n", "\r\n") if eol == "\r\n" else synced_norm_html
    )

    changed = synced_raw_html != raw_html
    if check_only:
        return changed

    if changed:
        tmp_path = html_path.with_suffix(html_path.suffix + ".tmp")
        tmp_path.write_bytes(synced_raw_html.encode("utf-8"))
        tmp_path.replace(html_path)

    return changed


def watch_loop(spec_path: Path, html_path: Path, interval: float = 0.5) -> int:
    """Watch spec_path for saves and automatically sync into html_path."""
    print(f"Watching {spec_path.name} for changes (Ctrl+C to stop)...")
    last_mtime: int | None = None

    while True:
        try:
            stat = spec_path.stat()
            mtime_ns = stat.st_mtime_ns
            if last_mtime is None or mtime_ns != last_mtime:
                last_mtime = mtime_ns
                ts = time.strftime("%H:%M:%S")
                try:
                    changed = sync_once(spec_path, html_path, check_only=False)
                    status = "updated" if changed else "already in sync"
                    print(f"[{ts}] Synced {spec_path.name} -> {html_path.name} ({status}).")
                except SpecValidationError as exc:
                    print(f"[{ts}] ERROR: {exc}", file=sys.stderr)
            time.sleep(interval)
        except KeyboardInterrupt:
            print("\nStopped watching.")
            return 0


def main(argv: list[str] | None = None) -> int:
    base_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description=(
            "Validate AIDR-SPECIFICATION.md and synchronize all specification "
            "prose, level definitions, and metadata into index.html."
        )
    )
    parser.add_argument(
        "--spec",
        type=Path,
        default=base_dir / DEFAULT_SPEC_FILENAME,
        help=f"Path to ground-truth Markdown file (default: {DEFAULT_SPEC_FILENAME})",
    )
    parser.add_argument(
        "--html",
        type=Path,
        default=base_dir / DEFAULT_HTML_FILENAME,
        help=f"Path to target HTML file (default: {DEFAULT_HTML_FILENAME})",
    )
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        "--check",
        action="store_true",
        help="Validate spec and verify index.html is already in sync without modifying files.",
    )
    mode_group.add_argument(
        "--watch",
        action="store_true",
        help="Continuously watch the specification file and sync automatically on save.",
    )

    args = parser.parse_args(argv)

    if args.watch:
        return watch_loop(args.spec, args.html)

    try:
        changed = sync_once(args.spec, args.html, check_only=args.check)
    except SpecValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.check:
        if changed:
            print(
                f"OUT OF SYNC: {args.html.name} differs from {args.spec.name}. "
                "Run 'python sync_spec.py' (or 'sync.bat') to update.",
                file=sys.stderr,
            )
            return 1
        print(f"OK: {args.html.name} is valid and in sync with {args.spec.name}.")
        return 0

    if changed:
        print(f"UPDATED: Synchronized {args.spec.name} -> {args.html.name}.")
    else:
        print(f"NO CHANGES: {args.html.name} is already in sync with {args.spec.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
