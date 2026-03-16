"""Markdown rendering and checkbox parsing."""
import re
import markdown as md


# Markdown renderer with extensions
_md = md.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"])


def render_markdown(content: str) -> str:
    """Render markdown content to HTML."""
    if not content or not content.strip():
        return '<p class="empty-file">This file is empty.</p>'

    _md.reset()
    return _md.convert(content)


def render_with_checkboxes(content: str, file_path: str) -> str:
    """
    Render markdown to HTML, then replace checkbox patterns with
    interactive HTML checkboxes. Skips checkboxes inside code blocks.
    """
    if not content or not content.strip():
        return '<p class="empty-file">This file is empty.</p>'

    # First, identify fenced code block line ranges
    code_block_lines = _find_code_block_ranges(content)

    # Parse checkboxes from raw content (before markdown rendering)
    lines = content.split('\n')
    checkboxes = []
    checkbox_pattern = re.compile(r'^(\s*)-\s+\[([ xX])\]\s+(.*)')

    for i, line in enumerate(lines):
        if i in code_block_lines:
            continue
        match = checkbox_pattern.match(line)
        if match:
            indent, state, text = match.groups()
            checked = state.lower() == 'x'
            checkboxes.append({
                'line_num': i,
                'checked': checked,
                'text': text.strip(),
                'original_line': line,
            })

    # Render the markdown
    _md.reset()
    html = _md.convert(content)

    # Post-process: replace rendered checkbox list items with interactive versions
    # The python-markdown library renders `- [ ] text` as `<li>[ ] text</li>`
    # and `- [x] text` as `<li>[x] text</li>` (or [X])
    for cb in checkboxes:
        checked_attr = 'checked' if cb['checked'] else ''
        state_char = '[x]' if cb['checked'] else '[ ]'
        state_char_upper = '[X]' if cb['checked'] else '[ ]'

        # Escape special chars in original text for use in JSON
        safe_text = (cb['text']
                     .replace('\\', '\\\\')
                     .replace('"', '&quot;')
                     .replace("'", "&#39;"))

        # Render the checkbox text as inline markdown
        inline_html = render_inline(cb['text'])

        replacement_inner = (
            f'<li class="checkbox-item" id="cb-{cb["line_num"]}">'
            f'<label class="checkbox-task">'
            f'<input type="checkbox" {checked_attr} '
            f'hx-post="/api/toggle-checkbox" '
            f'hx-vals=\'{{"file_path": "{file_path}", "line_num": {cb["line_num"]}, "original_text": "{safe_text}"}}\' '
            f'hx-target="#cb-{cb["line_num"]}" '
            f'hx-swap="outerHTML" />'
            f'<span>{inline_html}</span>'
            f'</label></li>'
        )

        # Try to find and replace the rendered list item
        # python-markdown renders checkboxes as: <li>[ ] text</li> or <li>[x] text</li>
        # We need to match the rendered version of the text (which may contain <strong>, etc.)
        rendered_text = _md.reset().convert(cb['text']).strip()
        # Remove wrapping <p> tags from the rendered text
        rendered_text = re.sub(r'^<p>(.*)</p>$', r'\1', rendered_text, flags=re.DOTALL)

        # Build patterns to match the rendered list item
        # python-markdown can render checkboxes in two forms:
        #   1. <li>[ ] text</li>                     (tight list)
        #   2. <li>\n<p>[ ] text</p>\n</li>          (loose list, blank lines between items)
        replaced = False
        for sc in [state_char, state_char_upper]:
            escaped_sc = re.escape(sc)
            escaped_text = re.escape(rendered_text)
            # Pattern 1: tight list (no <p> wrapper)
            pattern_tight = re.compile(
                r'<li>\s*' + escaped_sc + r'\s*' + escaped_text + r'\s*</li>',
                re.IGNORECASE | re.DOTALL
            )
            html, count = pattern_tight.subn(replacement_inner, html, count=1)
            if count > 0:
                replaced = True
                break
            # Pattern 2: loose list (<p> wrapper)
            pattern_loose = re.compile(
                r'<li>\s*<p>\s*' + escaped_sc + r'\s*' + escaped_text + r'\s*</p>\s*</li>',
                re.IGNORECASE | re.DOTALL
            )
            html, count = pattern_loose.subn(replacement_inner, html, count=1)
            if count > 0:
                replaced = True
                break

    return html


def render_inline(text: str) -> str:
    """Render inline markdown (bold, italic, code) without wrapping in <p>."""
    _md.reset()
    html = _md.convert(text)
    # Remove wrapping <p> tags
    html = re.sub(r'^<p>(.*)</p>$', r'\1', html.strip(), flags=re.DOTALL)
    return html


def _find_code_block_ranges(content: str) -> set[int]:
    """Find line numbers that are inside fenced code blocks."""
    lines = content.split('\n')
    in_code_block = False
    code_lines = set()
    fence_pattern = re.compile(r'^(`{3,}|~{3,})')

    for i, line in enumerate(lines):
        if fence_pattern.match(line.strip()):
            if in_code_block:
                code_lines.add(i)
                in_code_block = False
            else:
                in_code_block = True
                code_lines.add(i)
        elif in_code_block:
            code_lines.add(i)

    return code_lines


def toggle_checkbox(content: str, line_num: int, original_text: str) -> str:
    """
    Toggle a checkbox on a specific line in the content.
    Uses line_num as primary locator, falls back to content matching.
    Returns the modified content.
    """
    lines = content.split('\n')
    checkbox_pattern = re.compile(r'^(\s*-\s+\[)([ xX])(\]\s+.*)')

    # Primary: try the specified line number
    if 0 <= line_num < len(lines):
        match = checkbox_pattern.match(lines[line_num])
        if match and original_text in lines[line_num]:
            lines[line_num] = _toggle_line(lines[line_num], match)
            return '\n'.join(lines)

    # Fallback: search by content
    candidates = []
    for i, line in enumerate(lines):
        match = checkbox_pattern.match(line)
        if match and original_text in line:
            candidates.append((i, abs(i - line_num), match))

    if not candidates:
        raise ValueError(f"Checkbox not found: '{original_text}'. Please refresh the page.")

    # Pick the candidate closest to the original line number
    candidates.sort(key=lambda c: c[1])
    best_idx, _, best_match = candidates[0]
    lines[best_idx] = _toggle_line(lines[best_idx], best_match)
    return '\n'.join(lines)


def _toggle_line(line: str, match: re.Match) -> str:
    """Toggle a checkbox line between checked and unchecked."""
    prefix, state, suffix = match.groups()
    new_state = ' ' if state.lower() == 'x' else 'x'
    return f"{prefix}{new_state}{suffix}"
