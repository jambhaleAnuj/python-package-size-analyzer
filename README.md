# python-package-size-analyzer

Find and list installed Python packages sorted by size (largest first) so you can quickly identify heavy dependencies to uninstall or move to a virtual environment.

## Why This Script?

- **Single-file, zero dependencies** – pure Python stdlib only.
- **Fast insight** – instant overview of what is bloating your global / root Python installation.
- **Actionable output** – largest packages first so you can prune immediately.
- **Portable** – works anywhere standard `site` module is available (Windows, macOS, Linux).

> Unique Selling Point: You do _not_ need to install anything (no `pip install` step). Just run it.

## Features

- Recursively calculates total on-disk size for each package directory under all discovered `site-packages` locations
- Human‑readable MB output, aligned in a clean table
- Sorts automatically (largest → smallest)
- Ignores unreadable files gracefully (permission or transient I/O errors)

## Quick Start

```bash
python size.py
```

Example output:

```
Package                                     Size (MB)
----------------------------------------------------
numpy                                          137.42
pandas                                          62.77
matplotlib                                      35.19
scipy                                           31.04
pip                                             12.11
setuptools                                      11.45
...                                             ...
```

(Your numbers will differ based on what is installed.)

## When To Use This

- Before committing a base Docker image – trim unnecessary global packages
- Cleaning up a bloated system Python install on Windows
- Auditing a CI agent or build server
- Deciding which libraries to move into a virtual environment

## How It Works

The script:

1. Uses `site.getsitepackages()` (or falls back to `site.getusersitepackages()`)
2. Walks every directory directly inside each detected `site-packages`
3. Sums file sizes with `os.walk`
4. Outputs a sorted table (descending by size)

No heuristics, no partial sampling – full recursive byte size per package directory.

## Uninstalling Large Packages (Manual Examples)

Once you identify large packages you don't need globally:

```bash
pip uninstall package_name
```

Or prefer isolating heavy libs:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install big_package_only_when_needed
```

## FAQ

**Q: Does it follow symlinks?**  
A: It traverses directories as presented by `os.walk`; typical site-packages rarely use large symlinks. Symlinked entries count the file they point to if resolved by the OS.

**Q: Will this break anything?**  
A: It is read-only; it only walks and sums file sizes.

**Q: Can I export JSON?**  
A: Not in this minimal version (by design). You can pipe to a file and parse manually if needed.

**Q: Why not use `pip list --format=...`?**  
A: `pip` does not provide recursive on-disk size summaries out-of-the-box.

## Lightweight Extensibility Ideas (Optional)

If you fork it, you could add:

- `--top N` flag
- `--min-mb` filter
- CSV / JSON output
- Total cumulative size banner
  Keep changes minimal to preserve the zero-dependency ethos.

## Contributing

This is intentionally small. Feel free to open:

- Clear bug reports (unexpected size anomalies, cross-platform edge cases)
- Tiny PRs improving readability of documentation

Please avoid feature bloat.

## License

MIT – see `LICENSE` file.

## Badge Zone

![Python](https://img.shields.io/badge/Python-Stdlib%20Only-blue)
![Maintenance](https://img.shields.io/badge/Maintained-Yes-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![CI](<img alt="CI" src="https://github.com/jambhaleAnuj/python-package-size-analyzer/actions/workflows/python-package.yml/badge.svg">)

---

## SEO-Keywords

Python package size analyzer, list largest python packages, site-packages disk usage, python dependency bloat, remove large python packages, clean global python install, python script no dependencies, package size audit.

---

If this helped you reclaim disk space, consider starring the repo so others can discover it.
