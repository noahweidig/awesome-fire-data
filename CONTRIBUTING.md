# Contributing

Dataset pages are generated from YAML. Edit `data/datasets/<theme>.yml`, not files under `docs/datasets/`.

## Add a dataset

1. Pick the theme file in `data/datasets/`. If none fits, add a theme to `data/themes.yml` and a new file with the same slug.
2. Add an entry. Fields are listed in the [Contribute page](docs/contribute/index.md) and enforced by `data/schema.json`.
3. Tags must exist in `data/tag-vocab.yml`.
4. Use `related` to link overlapping datasets by `id`.
5. Run the checks:

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/generate.py
zensical build --clean
```

## Inclusion criteria

- Fire is the subject, or a core variable.
- Data is publicly reachable. Free registration is fine.
- Links go to the provider or a stable archive such as Zenodo.
- Provider, coverage, period and license are stated in the source.

## Accuracy

Every field must come from the provider or the data paper. Put unknowns in `caveat` or leave the dataset out. Do not copy values from other catalogs.

See the [Code of Conduct](CODE_OF_CONDUCT.md).
