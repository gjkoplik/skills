#!/usr/bin/env python3
"""Structural checks for the agent-viz wiki. No dependencies.

Run from anywhere:  python3 .claude/skills/agent-viz-wiki/validate.py
Exits non-zero if anything fails. Reports gaps separately from failures.
"""
import pathlib, re, sys, collections

HERE = pathlib.Path(__file__).resolve()
REPO = HERE.parents[3]
PLUGIN = REPO / "plugins" / "agent-viz"
W = PLUGIN / "wiki"

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
RESEARCH = {"sources": "source", "studies": "study", "people": "person"}
fail, gaps = [], []

def frontmatter(p):
    t = p.read_text(encoding="utf-8")
    if not t.startswith("---\n"):
        return None, t
    end = t.find("\n---", 4)
    if end == -1:
        return None, t
    fm = {}
    for line in t[4:end].split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm, t[end + 4:]

pages = {p: frontmatter(p) for d in list(RESEARCH) + ["concepts", "chart-types"]
         for p in sorted((W / d).glob("*.md")) if p.name != "README.md"}

# 1. every page has frontmatter with a type
for p, (fm, _) in pages.items():
    rel = p.relative_to(W)
    if fm is None:
        fail.append(f"no frontmatter: {rel}")
    elif "type" not in fm:
        fail.append(f"no type: {rel}")

# 2. research pages carry a valid status
counts = collections.Counter()
partial = 0
for d, ptype in RESEARCH.items():
    for p in sorted((W / d).glob("*.md")):
        fm, _ = pages.get(p, (None, ""))
        if not fm:
            continue
        st = fm.get("status")
        if st not in {"primary-read", "secondary-only", "not-reached"}:
            fail.append(f"bad/missing status: {p.relative_to(W)} -> {st!r}")
        else:
            counts[st] += 1
        if fm.get("status_partial") == "true":
            partial += 1
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fm.get("retrieved", "")):
            fail.append(f"bad/missing retrieved: {p.relative_to(W)}")

# 3. README's asserted counts match reality
readme = (W / "README.md").read_text(encoding="utf-8")
m = re.search(r"\*\*Current state: (\d+) `primary-read`, (\d+) `secondary-only`, "
              r"(\d+) `not-reached`, of which (\d+) are `status_partial`", readme)
if not m:
    fail.append("README count line not found or reworded; update validate.py with it")
else:
    want = (counts["primary-read"], counts["secondary-only"], counts["not-reached"], partial)
    got = tuple(int(x) for x in m.groups())
    if want != got:
        fail.append(f"README counts stale: says {got}, actual {want}")

# 4. chart-type relationships agree with the indexes that list them
for p, (fm, body) in pages.items():
    if not fm or fm.get("type") != "chart-type":
        continue
    rels = [r.strip() for r in fm.get("relationships", "").strip("[]").split(",") if r.strip()]
    if not rels:
        fail.append(f"chart-type with no relationships: {p.relative_to(W)}")
    for r in rels:
        idx = W / "chart-types" / f"{r}.md"
        if not idx.exists():
            continue                       # index not written yet: allowed
        if p.name not in idx.read_text(encoding="utf-8"):
            fail.append(f"{p.name} claims '{r}' but {r}.md does not list it")

# 4b. chart-type pages carry the required sections, in the required shape.
# The shape is non-negotiable and was previously enforced only by prose in the brief,
# which let one page merge two required sections into "measurably good at, and bad at".
REQUIRED_TYPE_SECTIONS = [
    "When to reach for it, and when not",
    "Structural decomposition",
    "Channels",
    "What it is measurably good at",
    "What it is measurably bad at",
    "What is contested",
    "The failure mode it invites",
    "Justifying the choice",
]
for p, (fm, body) in pages.items():
    if not fm or fm.get("type") != "chart-type":
        continue
    heads = re.findall(r"^##\s+(.*?)\s*$", body, re.M)
    for want in REQUIRED_TYPE_SECTIONS:
        if want not in heads:
            fail.append(f"missing required section '{want}': {p.relative_to(W)}")
    # a header block belongs to research pages, never to a chart-type or index page
    if re.search(r"^\*\*(Status|What it is good for|What it does not settle)\.", body, re.M):
        fail.append(f"chart-type page carries a research header block: {p.relative_to(W)}")

# 4c. aliases: frontmatter agrees with the aliases.md name index, both ways.
# The name index is only useful if it is complete, and a page's own alias list is
# only useful if the index can be reached from the name. Neither is checkable alone.
ALIAS_IDX = W / "chart-types" / "aliases.md"
if ALIAS_IDX.exists():
    idx_map = {}          # name -> target page filename, for rows that assert an alias
    for line in ALIAS_IDX.read_text(encoding="utf-8").split("\n"):
        if not line.startswith("| "):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3 or cells[0] == "Name":
            continue
        name, goes, status = cells[0], cells[1], cells[2]
        if goes.startswith("No page") or "for the caution, not for the form" in status:
            continue                      # a pointer to a different form, not an alias
        m3 = re.match(r"\[[^\]]*\]\(([a-z0-9-]+\.md)\)", goes)
        if m3:
            idx_map[name] = m3.group(1)
    for p, (fm, _) in pages.items():
        if not fm or fm.get("type") != "chart-type":
            continue
        declared = [a.strip() for a in fm.get("aliases", "").strip("[]").split(",") if a.strip()]
        if not declared:
            fail.append(f"chart-type with no aliases: {p.relative_to(W)}")
            continue
        for a in declared:
            if a not in idx_map:
                fail.append(f"{p.name} declares alias {a!r} which aliases.md does not list")
            elif idx_map[a] != p.name:
                fail.append(f"{p.name} declares alias {a!r} but aliases.md sends it to "
                            f"{idx_map[a]}")
    for name, target in idx_map.items():
        tp = W / "chart-types" / target
        if not tp.exists():
            continue
        tfm, _ = pages.get(tp, (None, ""))
        if not tfm or tfm.get("type") != "chart-type":
            continue          # index pages carry no aliases field
        declared = [a.strip() for a in tfm.get("aliases", "").strip("[]").split(",") if a.strip()]
        if name not in declared:
            fail.append(f"aliases.md maps {name!r} to {target} but that page does not "
                        f"declare it")

# 5. links and anchors resolve
def slugs(p, _c={}):
    if p not in _c:
        s = set()
        if p.suffix == ".md" and p.exists():
            for h in re.findall(r"^#{1,6}\s+(.*)$", p.read_text(encoding="utf-8"), re.M):
                s.add(re.sub(r"\s+", "-", re.sub(r"[^\w\s-]", "", h.lower()).strip()))
        _c[p] = s
    return _c[p]

for md in sorted(W.rglob("*.md")):
    for target in LINK.findall(md.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        path, _, frag = target.partition("#")
        dest = (md.parent / path).resolve() if path else md.resolve()
        if not dest.exists():
            fail.append(f"broken link: {md.relative_to(W)} -> {target}")
        elif frag and frag not in slugs(dest):
            fail.append(f"broken anchor: {md.relative_to(W)} -> {target}")
        else:
            try:
                dest.relative_to(PLUGIN)
            except ValueError:
                fail.append(f"link escapes plugin dir (breaks on install): "
                            f"{md.relative_to(W)} -> {target}")

# 5b. status_partial looks under-applied
PARTIAL_SIGNAL = re.compile(
    r"partial|not opened|was not read|were not read|unread|never reached|not[- ]reached",
    re.I)
for d in RESEARCH:
    for p in sorted((W / d).glob("*.md")):
        fm, body = pages.get(p, (None, ""))
        if not fm:
            continue
        labels = len(set(re.findall(r"`(primary-read|secondary-only|not-reached)`", body[:1800])))
        signal = bool(PARTIAL_SIGNAL.search(body[:1800]))
        if (labels > 1 or signal) and fm.get("status_partial") != "true":
            gaps.append(f"body describes uneven coverage but status_partial is unset: "
                        f"{p.relative_to(W)}")

# 5c. American spelling in our own prose. Verbatim quotes and code are exempt.
BRIT = {
    "colour": "color", "colours": "colors", "coloured": "colored",
    "behaviour": "behavior", "favour": "favor", "favoured": "favored",
    "labour": "labor", "centre": "center", "centres": "centers",
    "grey": "gray", "analyse": "analyze", "analysed": "analyzed",
    "organise": "organize", "organised": "organized", "recognise": "recognize",
    "normalise": "normalize", "visualise": "visualize",
    "visualisation": "visualization", "summarise": "summarize",
    "emphasise": "emphasize", "categorise": "categorize",
    "minimise": "minimize", "maximise": "maximize", "utilise": "utilize",
    "catalogue": "catalog", "programme": "program", "defence": "defense",
    "practise": "practice", "travelling": "traveling", "modelling": "modeling",
    "labelling": "labeling", "labelled": "labeled", "cancelled": "canceled",
    "learnt": "learned", "whilst": "while", "amongst": "among",
    "artefact": "artifact", "sceptical": "skeptical", "judgement": "judgment",
    "capitalised": "capitalized", "capitalise": "capitalize",
}
QUOTED_RE = re.compile("\"[^\"]*\"|“[^”]*”|`[^`]*`")
WORD_RE = re.compile("[a-z]+")
for _md in sorted(W.rglob("*.md")):
    _fence = False
    for _n, _line in enumerate(_md.read_text(encoding="utf-8").splitlines(), 1):
        _s = _line.lstrip()
        if _s.startswith("```"):
            _fence = not _fence
            continue
        if _fence or _s.startswith(">"):
            continue
        _clean = QUOTED_RE.sub(" ", _line)
        for _b in sorted(set(WORD_RE.findall(_clean)) & set(BRIT)):
            fail.append("British spelling %r (use %r): %s:%d"
                        % (_b, BRIT[_b], _md.relative_to(W), _n))

# 6. independence claims vs recorded authorship
authored = {p.stem: fm.get("author") for p, (fm, _) in pages.items() if fm and fm.get("author")}
for md in sorted(W.rglob("*.md")):
    if md.name == "README.md" and md.parent == W:
        continue          # the schema doc discusses the phrase itself
    body = md.read_text(encoding="utf-8")
    for m2 in re.finditer(r"(\w+)\s+independent sources?", body, re.I):
        gaps.append(f"independence claim to re-check by hand: {md.relative_to(W)}: "
                    f"'{m2.group(0)}'")
no_author = [str(p.relative_to(W)) for p, (fm, _) in pages.items()
             if fm and fm.get("type") == "source" and "author" not in fm]
if no_author:
    gaps.append(f"{len(no_author)} source pages record no author, so independence "
                f"cannot be checked mechanically: {', '.join(sorted(no_author)[:4])} ...")

print(f"pages checked: {len(pages)}")
print(f"status counts: {dict(counts)} | partial: {partial}")
print()
for g in gaps:
    print("GAP  ", g)
print()
for f in fail:
    print("FAIL ", f)
print()
print(f"{len(fail)} failure(s), {len(gaps)} gap(s)")
sys.exit(1 if fail else 0)
