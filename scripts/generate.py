#!/usr/bin/env python3
"""Generate dataset pages, theme indexes, tag config and nav from data/*.yml."""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
REQUIRED = ["id", "title", "icon", "summary", "provider", "coverage", "period",
            "resolution", "format", "license", "update", "access", "docs", "tags"]


def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def short(title):
    return re.sub(r"\s*\(.*?\)", "", title).strip()


def sc(icon):
    """lucide/flame -> :lucide-flame:"""
    return ":" + icon.replace("/", "-") + ":"


def q(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def yq(s):
    return '"' + q(s) + '"'


def replace_block(path, begin, end, body):
    text = path.read_text(encoding="utf-8")
    pat = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.S)
    if not pat.search(text):
        sys.exit(f"markers {begin!r} not found in {path}")
    path.write_text(pat.sub(lambda _: f"{begin}\n{body}\n{end}", text), encoding="utf-8")


def main():
    themes = load(ROOT / "data" / "themes.yml")
    vocab = load(ROOT / "data" / "tag-vocab.yml")
    tag_cat = {t: c for c, v in vocab.items() for t in v["tags"]}
    errors = []
    by_theme = {}
    ids = set()
    for th in themes:
        f = ROOT / "data" / "datasets" / f"{th['slug']}.yml"
        entries = load(f) if f.exists() else []
        for e in entries:
            for k in REQUIRED:
                if not e.get(k):
                    errors.append(f"{e.get('id', '?')}: missing {k}")
            if e["id"] in ids:
                errors.append(f"duplicate id {e['id']}")
            ids.add(e["id"])
            for t in e.get("tags", []):
                if t not in tag_cat:
                    errors.append(f"{e['id']}: tag {t!r} not in data/tag-vocab.yml")
        by_theme[th["slug"]] = sorted(entries, key=lambda e: e["title"].lower())
    if errors:
        sys.exit("\n".join(errors))

    dsroot = DOCS / "datasets"
    where = {e["id"]: (th["slug"], e) for th in themes for e in by_theme[th["slug"]]}
    for th in themes:
        d = dsroot / th["slug"]
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob("*.md"):
            old.unlink()
        entries = by_theme[th["slug"]]
        cards = []
        for e in entries:
            cards.append(
                f"-   {sc(e['icon'])}{{ .lg .middle }} __[{short(e['title'])}]({e['id']}.md)__\n\n"
                f"    ---\n\n    {e['summary']}\n\n"
                f"    [:lucide-arrow-right: Details]({e['id']}.md)"
            )
        (d / "index.md").write_text(
            f"---\nicon: {th['icon']}\n---\n\n# {th['title']}\n\n{th['summary']}\n\n"
            f"<div class=\"grid cards\" markdown>\n\n" + "\n\n".join(cards) + "\n\n</div>\n",
            encoding="utf-8")
        for e in entries:
            fm_tags = "\n".join(f"  - {t}" for t in e["tags"])
            rows = [
                ("lucide-building-2", "Who publishes the data", "Provider", e["provider"]),
                ("lucide-map", "Geographic extent", "Coverage", e["coverage"]),
                ("lucide-calendar", "Years covered", "Period", e["period"]),
                ("lucide-ruler", "Pixel size, grid spacing or feature type", "Resolution", e["resolution"]),
                ("lucide-file", "File and service formats", "Format", ", ".join(e["format"])),
                ("lucide-scale", "Terms of use. Check the provider before redistributing", "License", e["license"]),
                ("lucide-refresh-cw", "How often new data is published", "Updates", e["update"]),
            ]
            table = "| Field | Value |\n| --- | --- |\n" + "\n".join(
                f"| :{i}:{{ title=\"{t}\" }} {lab} | {val} |" for i, t, lab, val in rows)
            rel = ""
            if e.get("related"):
                items = "\n".join(
                    f"- [{short(where[r][1]['title'])}](../{where[r][0]}/{r}.md)" for r in e["related"])
                rel = f"\n## Related datasets\n\n{items}\n"
            cav = f"\n!!! warning \"Caveat\"\n\n    {e['caveat']}\n" if e.get("caveat") else ""
            (d / f"{e['id']}.md").write_text(
                f"---\ntitle: {yq(e['title'])}\nicon: {e['icon']}\ntags:\n{fm_tags}\n---\n\n"
                f"# {e['title']}\n\n{e['summary']}\n\n"
                f"[:lucide-download: Access data]({e['access']}){{ .md-button .md-button--primary }}\n"
                f"[:lucide-book-open: Documentation]({e['docs']}){{ .md-button }}\n\n"
                f"## At a glance\n\n{table}\n{cav}{rel}\n"
                f"[:lucide-arrow-left: Back to {th['title']}](index.md){{ .md-button }}\n",
                encoding="utf-8")

    theme_cards = "\n\n".join(
        f"-   {sc(th['icon'])}{{ .lg .middle }} __[{th['title']}](datasets/{th['slug']}/index.md)__\n\n"
        f"    ---\n\n    {th['summary']}\n\n"
        f"    {len(by_theme[th['slug']])} datasets\n\n"
        f"    [:lucide-arrow-right: Explore](datasets/{th['slug']}/index.md)"
        for th in themes)
    block = f"<div class=\"grid cards\" markdown>\n\n{theme_cards}\n\n</div>"
    replace_block(DOCS / "index.md", "<!-- BEGIN THEMES -->", "<!-- END THEMES -->", block)
    ds_block = block.replace("(datasets/", "(")
    (dsroot / "index.md").write_text(
        "---\nicon: lucide/database\n---\n\n# Datasets\n\n"
        f"{len(themes)} themes cover the fire data landscape. Each dataset page lists provider, coverage, "
        "resolution, format, license and where to get the data.\n\n"
        "<!-- BEGIN THEMES -->\n" + ds_block + "\n<!-- END THEMES -->\n", encoding="utf-8")

    th_title = {t["slug"]: t["title"] for t in themes}
    rows = []
    for th in themes:
        for e in by_theme[th["slug"]]:
            rows.append(
                f"| [{short(e['title'])}](../datasets/{th['slug']}/{e['id']}.md) | {th_title[th['slug']]} "
                f"| {e['coverage']} | {e['period']} | {e['resolution']} | {e['license']} |")
    total = len(rows)
    (DOCS / "browse" / "all-datasets.md").write_text(
        "---\nicon: lucide/table\nhide:\n  - tags\n---\n\n# All datasets\n\n"
        f"{total} datasets, grouped by theme.\n\n"
        "| Dataset | Theme | Coverage | Period | Resolution | License |\n| --- | --- | --- | --- | --- | --- |\n"
        + "\n".join(rows) + "\n", encoding="utf-8")

    nav_items = ['  { "Home" = "index.md" },']
    ds = ['      "datasets/index.md",']
    for th in themes:
        sub = [f'          "datasets/{th["slug"]}/index.md",']
        sub += [f'          {{ "{q(short(e["title"]))}" = "datasets/{th["slug"]}/{e["id"]}.md" }},'
                for e in by_theme[th["slug"]]]
        ds.append(f'      {{ "{q(th["title"])}" = [\n' + "\n".join(sub) + "\n      ] },")
    nav_items.append('  { "Datasets" = [\n' + "\n".join(ds) + "\n  ] },")
    nav_items.append('  { "Browse" = ["browse/index.md", "browse/all-datasets.md", "browse/tags.md"] },')
    nav_items.append('  { "Learn" = ["learn/index.md", "learn/choosing-a-dataset.md", "learn/fire-science-primer.md", '
                     '"learn/compare-datasets.md", "learn/data-formats.md", "learn/tools-and-apis.md", "learn/software-and-models.md", "learn/glossary.md"] },')
    nav_items.append('  { "Contribute" = ["contribute/index.md"] },')
    nav_items.append('  { "About" = ["about/index.md", "about/changelog.md"] },')
    replace_block(ROOT / "zensical.toml", "# BEGIN GENERATED NAV", "# END GENERATED NAV",
                  "nav = [\n" + "\n".join(nav_items) + "\n]")

    ident, icons = [], ["default = \"lucide/hash\""]
    for c, v in vocab.items():
        icons.append(f'{c} = "{v["icon"]}"')
        ident += [f'"{q(t)}" = "{c}"' for t in v["tags"]]
    replace_block(ROOT / "zensical.toml", "# BEGIN GENERATED TAGS", "# END GENERATED TAGS",
                  "[project.extra.tags]\n" + "\n".join(ident) + "\n\n[project.theme.icon.tag]\n" + "\n".join(icons))
    print(f"generated {total} dataset pages in {len(themes)} themes")


if __name__ == "__main__":
    main()
