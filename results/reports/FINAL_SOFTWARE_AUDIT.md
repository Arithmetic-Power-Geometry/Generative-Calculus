# Final Software Audit — Generative Calculus v2.0.0

- Python source compilation/import: PASS
- Automated tests: **14/14 passed**
- Gradio application import/smoke test: PASS
- CLI sensor command: PASS
- CLI projection command: PASS
- Full deterministic reproduction: PASS
- Generated result tables: **14 CSV files in `results/tables`**, plus **3 audit/comparison CSV reports** in `results/reports`
- Generated publication figures: 10 PNG files
- Public MLPerf Power subset included with explicit attribution: PASS
- Reachable-envelope transport checks: 400/400 satisfied
- Apache-2.0 LICENSE: included
- NOTICE and public-data attribution: included
- GitHub Actions push/PR/manual workflow: included
- One-command `make all`: included
- Windows `reproduce.bat` and `run_app.bat`: included
- Interactive app: 10 tabs

The local sandbox does not allow outbound PyPI access, so the clean-environment dependency-download phase could not be executed locally. Source execution used the already installed environment; GitHub Actions performs the clean installation from `pyproject.toml` before running the same tests and reproduction workflow.
