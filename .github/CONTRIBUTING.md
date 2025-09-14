# Contributing

Thanks for your interest in improving this tiny utility! The goal is to keep it **small, dependency‑free, and easy to read**.

## Guiding Principles

- Single file (`size.py`) stays minimal
- No third‑party dependencies
- Cross‑platform friendliness (Windows, macOS, Linux)
- Prefer clarity over micro‑optimizations unless a measurable win

## Good Contribution Types

- Documentation clarifications (README, FAQ, examples)
- Reproducible bug fixes (with a short explanation of cause)
- Tiny, optional flags (opened via issue first)
- Improved edge‑case handling without adding complexity

## Please Avoid

- Adding packaging / installers / publishing logic
- Large feature sets (interactive UI, progress bars, etc.)
- Refactors that only rename things
- Adding dependency managers or lock files

## Workflow

1. Fork the repo
2. Create a branch: `feat/short-name` or `fix/short-name`
3. Make your change (ensure script still runs with `python size.py`)
4. Update docs if behavior changed
5. Open a Pull Request describing the motivation

## Reporting Issues

Include:

- OS + Python version (`python --version`)
- Example of unexpected output
- If possible, the directory layout or a redacted tree

## Light Feature Requests

Open an issue first. Some acceptable minimal ideas:

- `--top N` to limit rows
- `--min-mb X` threshold
- Optional JSON output

## Code Style

- Standard library only
- Keep functions short & purpose driven
- Avoid premature abstraction

## License

By contributing you agree your code is released under the repository's MIT License.

---

Keep it lean. Happy hacking!
