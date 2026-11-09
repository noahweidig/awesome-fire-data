---
icon: lucide/git-pull-request
---

# Contribute

Dataset pages are generated from YAML in `data/datasets/`. Add an entry and open a pull request. Each edit button on a dataset page opens the generated file, so edit the YAML instead.

[:fontawesome-brands-github: Open the repository](https://github.com/noahweidig/awesome-fire-data){ .md-button .md-button--primary }
[:lucide-circle-alert: Suggest a dataset](https://github.com/noahweidig/awesome-fire-data/issues/new?template=new-dataset.yml){ .md-button }

## Inclusion criteria

- Fire is the subject, or a core variable (for example fire emissions or fuels).
- The data is publicly reachable. Free registration is fine.
- The link works and goes to the provider or a stable archive such as Zenodo.
- Provider, coverage, period and license can be stated from the source.

## Entry format

Add to the file for the matching theme, for example `data/datasets/perimeters.yml`:

```yaml
- id: my-dataset            # unique, becomes the page URL
  title: My Dataset (MDS)   # text in parentheses is dropped in the navigation
  icon: lucide/flame        # any Lucide icon
  summary: One sentence.
  provider: Agency name
  coverage: Region
  period: 2000 to present
  resolution: 30 m
  format: [GeoTIFF]
  license: Public domain
  update: Annual
  access: https://example.org/data
  docs: https://example.org/docs
  tags: [United States, Bulk download, GeoTIFF, Public domain, Annual, 30 m]
  caveat: Optional warning shown on the page.
```

Tags must exist in `data/tag-vocab.yml`. To add a tag, add it there under a category.

Optional fields:

- `doi`: bare DOI such as `10.2737/RDS-2013-0009.7`. Shown under Cite and in the structured data.
- `citation`: preferred citation text.
- `verified`: `YYYY-MM-DD` date you last checked the entry against the provider. Shown in the table.
- `snippets`: list of `{label, lang, code}` shown as tabs under Quick start.

`related` is an optional list of dataset `id` values that overlap with this one. The page shows them under Related datasets.

`python scripts/validate.py` checks entries against `data/schema.json`. CI runs it on every pull request. See [CONTRIBUTING.md](https://github.com/noahweidig/awesome-fire-data/blob/main/CONTRIBUTING.md).

## Build locally

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/generate.py
zensical serve
```
