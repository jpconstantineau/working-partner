"""Validate the distributed skill layout and local documentation links."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
def require(condition, message):
    if not condition:
        errors.append(message)

skills = list((ROOT / "skills").glob("*/SKILL.md"))
names = set()
for path in skills:
    text = path.read_text()
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    require(match is not None, f"{path}: missing frontmatter")
    if not match:
        continue
    fields = dict(re.findall(r"^([a-z-]+):\s*(.+)$", match[1], re.M))
    name = fields.get("name", "")
    require(name == path.parent.name, f"{path}: folder/name mismatch")
    require(name not in names, f"{path}: duplicate name")
    require(bool(fields.get("description")), f"{path}: missing description")
    require(fields.get("license") == "MIT", f"{path}: license metadata")
    names.add(name)
    if name != "working-partner":
        require(bool(re.fullmatch(r"productivity(?:-[a-z0-9]+){0,3}", name)), f"{path}: expected class-use-method-tool naming")
require("productivity-brainstorming-gtd-npm" in names, "GTD method has wrong selection-path name")
require(not list((ROOT / "skills").rglob("LICENSE")), "Use root LICENSE, include it in release distributions")
require(not list(ROOT.rglob("source-record.json")), "Keep source details in Markdown")
require(len(list((ROOT / "skills").rglob("SKILL.md"))) == len(skills), "Distributed skills must use the documented flat layout")
for path in ROOT.rglob("*"):
    if path.suffix not in (".md", ".html"):
        continue
    text = path.read_text()
    links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", text) if path.suffix == ".md" else re.findall(r'href="([^"]+)"', text)
    for link in links:
        if urlsplit(link).scheme or link.startswith("#"):
            continue
        target = (path.parent / unquote(link.split("#")[0])).resolve()
        require(target.exists(), f"{path.relative_to(ROOT)}: broken link {link}")
    require("List-Prototype" not in text, f"{path}: migration history belongs in PR")
readme = (ROOT / "README.md").read_text()
require(not re.search(r"\bseed\b", readme, re.I), "README should describe the product")
for f in ("LICENSE", "Licenses.md", "Attributions.md", "AGENTS.md"):
    require((ROOT / f).exists(), f"Missing {f}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {len(skills)} distributed skills; metadata, layout and local links")
