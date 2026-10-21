#!/usr/bin/env python3
"""Offline, read-only checks for this handbook (Python 3.10+, standard library).

Run: python3 scripts/check_docs.py [--root /path/to/repository]

Checks Markdown links/images, GitHub-style heading anchors, explicit HTML IDs,
fenced blocks, strict JSON examples, and SVG XML/accessibility metadata. It
does not execute examples, install dependencies, contact URLs, or alter files.
It is a focused documentation checker, not a complete CommonMark renderer.

To document a deliberately incomplete JSON example, immediately precede its
fence with: <!-- docs-check: skip-json: explain the placeholder here -->
Alternatively use a fence label such as `json pseudocode` or `json placeholder`.
Valid JSON is always checked; malformed JSON is skipped only when explicitly
marked. Plain [bracketed text] is not treated as an undefined reference link.
"""

from __future__ import annotations

import argparse
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import string
import sys
import unicodedata
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field


EXCLUDED_DIRS = {
    ".git", "node_modules", ".qa", "authoring", "__pycache__",
    ".venv", "venv", ".cache", ".pytest_cache", "dist", "build",
}
MARKDOWN_SUFFIXES = {".md", ".markdown"}
FENCE_OPEN = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
REF_DEF = re.compile(r"^ {0,3}\[([^\]\n]+)\]:[ \t]*(.*)$")
ATX_HEADING = re.compile(r"^ {0,3}#{1,6}(?:[ \t]+|$)(.*)$")
SETEXT = re.compile(r"^ {0,3}(?:=+|-+)[ \t]*$")
SKIP_JSON = re.compile(r"<!--\s*docs-check:\s*skip-json:\s*(.*?)\s*-->", re.I)
PSEUDOCODE = re.compile(r"\b(?:pseudocode|placeholder|template)\b|伪代码|占位", re.I)
ESCAPE = re.compile(r"\\([" + re.escape(string.punctuation) + r"])")


def blank(text: str) -> str:
    """Mask syntax without changing offsets or line numbers."""
    return "".join("\n" if char == "\n" else " " for char in text)


def unescape_markdown(text: str) -> str:
    return html.unescape(ESCAPE.sub(r"\1", text))


def escaped(text: str, position: int) -> bool:
    slashes = 0
    while position > 0 and text[position - 1] == "\\":
        slashes += 1
        position -= 1
    return slashes % 2 == 1


def mask_inline_code(text: str) -> str:
    output = list(text)
    runs = list(re.finditer(r"`+", text))
    index = 0
    while index < len(runs):
        start = runs[index]
        if escaped(text, start.start()):
            index += 1
            continue
        end_index = index + 1
        while end_index < len(runs) and len(runs[end_index][0]) != len(start[0]):
            end_index += 1
        if end_index == len(runs):
            index += 1
            continue
        end = runs[end_index].end()
        output[start.start():end] = blank(text[start.start():end])
        index = end_index + 1
    return "".join(output)


def bracket_end(text: str, start: int) -> int | None:
    depth = 0
    for position in range(start, len(text)):
        if escaped(text, position):
            continue
        if text[position] == "[":
            depth += 1
        elif text[position] == "]":
            depth -= 1
            if depth == 0:
                return position
    return None


def destination(text: str, start: int) -> tuple[str, int] | None:
    """Read an angle-wrapped or balanced plain Markdown destination."""
    position = start
    if position < len(text) and text[position] == "<":
        end = position + 1
        while end < len(text):
            if text[end] == "\n" or (text[end] == "<" and not escaped(text, end)):
                return None
            if text[end] == ">" and not escaped(text, end):
                return unescape_markdown(text[position + 1:end]), end + 1
            end += 1
        return None
    depth = 0
    while position < len(text):
        char = text[position]
        if escaped(text, position):
            position += 1
            continue
        if char.isspace():
            break
        if char == "(":
            depth += 1
        elif char == ")":
            if depth == 0:
                break
            depth -= 1
        position += 1
    if depth:
        return None
    return unescape_markdown(text[start:position]), position


def inline_target(text: str, start: int) -> tuple[str, int] | None:
    """Read `(destination optional-title)`; start points at the opening `(`."""
    position = start + 1
    while position < len(text) and text[position].isspace():
        position += 1
    found = destination(text, position)
    if found is None:
        return None
    target, position = found
    while position < len(text) and text[position].isspace():
        position += 1
    if position < len(text) and text[position] in {'"', "'", "("}:
        closing = ")" if text[position] == "(" else text[position]
        position += 1
        while position < len(text) and (text[position] != closing or escaped(text, position)):
            position += 1
        if position == len(text):
            return None
        position += 1
        while position < len(text) and text[position].isspace():
            position += 1
    if position < len(text) and text[position] == ")":
        return target, position + 1
    return None


def reference_key(label: str) -> str:
    return " ".join(unescape_markdown(label).split()).casefold()


def iter_links(text: str, references: dict[str, str]):
    """Yield (start, end, label, destination), including images and known refs."""
    position = 0
    while position < len(text):
        if text[position] != "[" or escaped(text, position):
            position += 1
            continue
        close = bracket_end(text, position)
        if close is None:
            position += 1
            continue
        label = text[position + 1:close]
        end, target = close + 1, None
        if end < len(text) and text[end] == "(":
            found = inline_target(text, end)
            if found:
                target, end = found
        elif end < len(text) and text[end] == "[":
            ref_close = bracket_end(text, end)
            if ref_close is not None:
                key = text[end + 1:ref_close] or label
                target = references.get(reference_key(key))
                if target is not None:
                    end = ref_close + 1
        else:
            target = references.get(reference_key(label))
        if target is not None:
            begin = position
            if begin > 0 and text[begin - 1] == "!" and not escaped(text, begin - 1):
                begin -= 1
            yield begin, end, label, target
            position = end
        else:
            # Literal [placeholders] and unknown shortcut references are plain text.
            position = close + 1


class HTMLDetails(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[tuple[int, str]] = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"])
        if tag == "a" and attributes.get("name"):
            self.ids.add(attributes["name"])
        key = "href" if tag == "a" else "src" if tag == "img" else None
        if key and attributes.get(key) is not None:
            self.links.append((self.getpos()[0], attributes[key]))

    handle_startendtag = handle_starttag


def heading_slug(text: str, references: dict[str, str]) -> str:
    for start, end, label, _ in reversed(list(iter_links(text, references))):
        text = text[:start] + label + text[end:]
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"(`+)(.*?)\1", r"\2", text)
    text = re.sub(r"(?<!\w)(\*{1,3}|_{1,3})(.+?)\1(?!\w)", r"\2", text)
    text = text.replace("~~", "")
    text = unescape_markdown(text).strip().lower()
    # GitHub retains Unicode letters/numbers/marks, hyphens and underscores;
    # punctuation/symbols are removed, and spaces become hyphens.
    text = "".join(
        char for char in text
        if char in "-_ " or char.isalnum()
        or unicodedata.category(char).startswith("M")
        or unicodedata.category(char) == "Pc"
    )
    return text.replace(" ", "-")


@dataclass
class Document:
    path: Path
    prose: str
    anchors: set[str] = field(default_factory=set)
    links: list[tuple[int, str]] = field(default_factory=list)


class Checker:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.errors: list[str] = []
        self.notes: list[str] = []
        self.documents: dict[Path, Document] = {}
        self.html_ids: dict[Path, set[str]] = {}
        self.stats = dict(markdown=0, svg=0, links=0, external=0,
                          anchors=0, fences=0, json=0, json_skipped=0)

    def location(self, path: Path, line: int = 0) -> str:
        try:
            name = path.relative_to(self.root).as_posix()
        except ValueError:
            name = str(path)
        return f"{name}:{line}" if line else name

    def error(self, path: Path, line: int, message: str):
        self.errors.append(f"{self.location(path, line)}: {message}")

    def note(self, path: Path, line: int, message: str):
        self.notes.append(f"{self.location(path, line)}: {message}")

    def read(self, path: Path) -> str | None:
        try:
            return path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            self.error(path, 0, f"无法读取 UTF-8 文件：{exc}")
            return None

    def check_json(self, path: Path, line: int, info: str, body: str, previous: str):
        language = info.split(maxsplit=1)[0].lower() if info.strip() else ""
        if language not in {"json", "jsonc", "json5"}:
            return
        if language != "json":
            self.stats["json_skipped"] += 1
            self.note(path, line, f"跳过严格 JSON 校验：显式使用 {language} 格式。")
            return
        try:
            def reject_constant(value):
                raise ValueError(f"JSON 标准不接受 {value}")
            json.loads(body, parse_constant=reject_constant)
            self.stats["json"] += 1
        except (json.JSONDecodeError, ValueError) as exc:
            marker = SKIP_JSON.search(previous)
            reason = marker.group(1).strip() if marker else ""
            if not reason and PSEUDOCODE.search(info):
                reason = f"围栏已明确标注 {info}"
            if reason:
                self.stats["json_skipped"] += 1
                self.note(path, line, f"跳过占位/伪代码 JSON：{reason}")
            else:
                error_line = line + getattr(exc, "lineno", 1)
                self.error(path, error_line, f"JSON 示例无法解析：{exc}")

    def parse_markdown(self, path: Path, text: str) -> Document:
        lines = text.splitlines(keepends=True)
        visible = list(lines)
        opened = None
        for index, original in enumerate(lines):
            # Recognize fences within ordinary block quotes as well.
            line = re.sub(r"^(?: {0,3}>[ \t]?)+", "", original.rstrip("\r\n"))
            if opened is None:
                match = FENCE_OPEN.match(line)
                if match and not (match[1][0] == "`" and "`" in match[2]):
                    opened = (match[1][0], len(match[1]), index, match[2].strip())
                    self.stats["fences"] += 1
                    visible[index] = blank(original)
            else:
                char, length, first, info = opened
                visible[index] = blank(original)
                if re.fullmatch(r" {0,3}" + re.escape(char) + "{" + str(length) + r",}[ \t]*", line):
                    previous = lines[first - 1].strip() if first else ""
                    code = "".join(lines[first + 1:index])
                    if original.lstrip().startswith(">"):
                        code = re.sub(r"^(?: {0,3}>[ \t]?)+", "", code, flags=re.M)
                    self.check_json(path, first + 1, info, code, previous)
                    opened = None
        if opened:
            self.error(path, opened[2] + 1, "代码围栏没有对应的结束围栏。")

        prose = "".join(visible)
        prose = re.sub(r"<!--[\s\S]*?-->", lambda match: blank(match[0]), prose)
        reference_lines = prose.splitlines(keepends=True)
        references: dict[str, str] = {}
        definition_links = []
        for index, line in enumerate(reference_lines):
            match = REF_DEF.match(line.rstrip("\r\n"))
            if not match or match[1].startswith("^"):
                continue
            tail = match[2]
            continuation = False
            if not tail and index + 1 < len(reference_lines):
                tail = reference_lines[index + 1].strip()
                continuation = True
            found = destination(tail, 0)
            if found and found[0]:
                key = reference_key(match[1])
                references.setdefault(key, found[0])
                definition_links.append((index + 1, found[0]))
                reference_lines[index] = blank(line)
                if continuation:
                    reference_lines[index + 1] = blank(reference_lines[index + 1])

        prose = "".join(reference_lines)
        doc = Document(path, prose)
        used_slugs: set[str] = set()
        heading_lines = prose.splitlines()
        for index, line in enumerate(heading_lines):
            match = ATX_HEADING.match(line)
            heading = None
            if match:
                heading = re.sub(r"[ \t]+#+[ \t]*$", "", match[1])
            elif index + 1 < len(heading_lines) and line.strip() and SETEXT.match(heading_lines[index + 1]):
                if not SETEXT.match(line) and not line.lstrip().startswith(("|", ">", "- ", "* ", "+ ")):
                    heading = line.strip()
            if heading is not None:
                base = heading_slug(heading, references)
                slug, suffix = base, 0
                while slug in used_slugs:
                    suffix += 1
                    slug = f"{base}-{suffix}"
                used_slugs.add(slug)
        doc.anchors.update(used_slugs)

        searchable = mask_inline_code(prose)
        details = HTMLDetails()
        details.feed(searchable)
        doc.anchors.update(details.ids)
        doc.links.extend(details.links)
        doc.links.extend(definition_links)
        for start, _, _, target in iter_links(searchable, references):
            doc.links.append((searchable.count("\n", 0, start) + 1, target))
        return doc

    def load_document(self, path: Path) -> Document | None:
        path = path.resolve()
        if path in self.documents:
            return self.documents[path]
        text = self.read(path)
        if text is None:
            return None
        self.stats["markdown"] += 1
        doc = self.parse_markdown(path, text)
        self.documents[path] = doc
        return doc

    def check_svg(self, path: Path):
        self.stats["svg"] += 1
        try:
            root = ET.parse(path).getroot()
        except (ET.ParseError, OSError) as exc:
            self.error(path, 0, f"SVG XML 无法解析：{exc}")
            return
        if root.tag.rsplit("}", 1)[-1] != "svg":
            self.error(path, 0, "SVG 文件的根元素应为 svg。")
            return
        tags = {"title": False, "desc": False}
        ids = set()
        for node in root.iter():
            local_name = node.tag.rsplit("}", 1)[-1]
            if local_name in tags and "".join(node.itertext()).strip():
                tags[local_name] = True
            if node.get("id"):
                ids.add(node.get("id"))
        self.html_ids[path.resolve()] = ids
        missing = [name for name, present in tags.items() if not present]
        mermaid = bool(root.get("aria-roledescription") or root.get("id", "").startswith("mermaid"))
        role = root.get("role", "")
        if missing and mermaid and role in {"img", "graphics-document", "graphics-symbol"}:
            self.note(path, 0, "跳过 Mermaid 渲染 SVG 的 title/desc 要求：已有图形 role；可访问名称仍需视觉验收。")
        elif missing:
            self.error(path, 0, "SVG 缺少非空 " + " / ".join(missing) + "。")

    def check_link(self, source: Path, line: int, target: str):
        target = target.strip()
        if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("//"):
            self.stats["external"] += 1
            return
        # Host-root links are not repository-relative GitHub links.
        if target.startswith("/"):
            self.stats["external"] += 1
            return
        self.stats["links"] += 1
        try:
            parsed = urlsplit(target)
        except ValueError as exc:
            self.error(source, line, f"链接格式错误 {target!r}：{exc}")
            return
        local = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source.resolve()
        if not local.is_relative_to(self.root):
            self.error(source, line, f"相对链接越出仓库范围：{target}")
            return
        if not local.exists():
            self.error(source, line, f"内部目标不存在：{target}")
            return
        if not parsed.fragment:
            return
        anchor = unquote(parsed.fragment)
        if local.is_dir():
            readmes = [local / name for name in ("README.md", "readme.md", "README.markdown")]
            local = next((item for item in readmes if item.is_file()), local)
        anchors = None
        if local.suffix.lower() in MARKDOWN_SUFFIXES and local.is_file():
            doc = self.load_document(local)
            anchors = doc.anchors if doc else None
        elif local.suffix.lower() in {".html", ".htm", ".svg"} and local.is_file():
            if local not in self.html_ids:
                text = self.read(local)
                if text is not None:
                    parser = HTMLDetails()
                    parser.feed(text)
                    self.html_ids[local] = parser.ids
            anchors = self.html_ids.get(local)
        else:
            self.note(source, line, f"跳过非 Markdown/HTML/SVG 目标的片段语义：{target}")
        if anchors is not None:
            self.stats["anchors"] += 1
            if anchor not in anchors:
                self.error(source, line, f"内部锚点不存在：{target}")

    def run(self) -> int:
        markdown_paths, svg_paths = [], []
        for directory, folders, filenames in os.walk(self.root, followlinks=False):
            folders[:] = sorted(name for name in folders if name not in EXCLUDED_DIRS)
            for name in sorted(filenames):
                path = Path(directory) / name
                if path.is_symlink():
                    continue
                if path.suffix.lower() in MARKDOWN_SUFFIXES:
                    markdown_paths.append(path)
                elif path.suffix.lower() == ".svg":
                    svg_paths.append(path)
        for path in markdown_paths:
            self.load_document(path)
        for path in svg_paths:
            self.check_svg(path)
        for doc in list(self.documents.values()):
            for line, target in doc.links:
                self.check_link(doc.path, line, target)
        print(f"文档检查：{self.root}")
        print("Markdown {markdown} · SVG {svg} · 内部链接 {links} · 锚点 {anchors} · "
              "围栏 {fences} · JSON 通过 {json} / 跳过 {json_skipped} · 外部链接未联网 {external}".format(**self.stats))
        for note in self.notes:
            print(f"SKIP {note}")
        for error in self.errors:
            print(f"ERROR {error}")
        print(f"结果：{'失败' if self.errors else '通过'}；{len(self.errors)} 个错误，{len(self.notes)} 条跳过说明。")
        return 1 if self.errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="仓库根目录；默认取脚本的上级目录")
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error(f"仓库目录不存在：{args.root}")
    return Checker(args.root).run()


if __name__ == "__main__":
    sys.exit(main())
