# argops

A command-line interface for promoting Argocd applications between environments.

Features:

- smart promote of value files between environments
- Dry-run option to see the changes.

## Installing

```bash
pipx install argops
```

## Usage

To use the tool, simply run it from your terminal on the directory where your environment directories are.

```bash
argops \
  --src-dir=<source directory> \
  --dest-dir=<destination directory> \
  --dry-run
```

By default the source directory is `staging` and the destination directory `production`. The `--dry-run` flag will show you what changes will it do without making them.

Once you know that the changes are ok, remove the `--dry-run` option.

# Development

If you want to run the tool from source, make sure you have Python and all required packages installed. You can do this using:
```bash
git clone https://codeberg.org/lyz/argops 
cd argops
make init
```

## Help

If you need help or want to report an issue, please see our [issue tracker](https://codeberg.org/lyz/argops/issues).

## License

GPLv3

## Authors

Lyz
