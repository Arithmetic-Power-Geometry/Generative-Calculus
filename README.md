# Generative Calculus v2.0.0 — Reproducibility Package

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Released under the Apache License 2.0.

This repository accompanies the manuscript **Generative Calculus: Embodied Operational Envelopes, Reachable Capability, and Resource-Scaled Comparison**. It implements every finite/computational experiment reported in the paper and keeps validation reductions separate from scoped Generative Calculus results.

## One-command reproduction

```bash
python -m pip install -e '.[test]'
pytest -q
python -m generative_calculus.reproduce
```

or:

```bash
make all
```

GitHub Actions runs the same test-and-reproduce pipeline on pushes, pull requests, and manual dispatch.

## Interactive app

```bash
python app.py
```

The ten tabs vary Blackwell accuracies, Pareto costs/budgets, parity-envelope dimension, convex reconstruction resolution, reversal scale, reachable-envelope budgets, exact generator count, Equality size/error, MLPerf Power portfolio inspection, and theorem/novelty audits.

## Reproduced result families

1. Blackwell/Le Cam symmetric binary experiment validation.
2. Marginal-incompleteness and coupling-gap sensitivity.
3. Equality communication-complexity projection.
4. Polynomial hierarchy visualization.
5. Finite whole-envelope inclusion grid.
6. Strong proper-projection irreducibility and unbounded GC projection order.
7. Convex support-function reconstruction test.
8. Reversible microdynamics with exponentially costly operational reversal.
9. Exact generator-program dimension corollary.
10. Budgeted reachable-envelope transport audit.
11. Public MLPerf Power multi-workload performance/power portfolio validation.
12. Machine-readable novelty, theorem-status, and existing-vs-GC comparison reports.

## Public MLPerf Power data

`data/mlperf_power_public_subset.csv` is a small, explicitly attributed subset of the public MLPerf Power data used only for reproducible validation. The underlying MLPerf Power study reports 1,841 power measurements across 60 systems and was published at HPCA 2025 (DOI: 10.1109/HPCA61900.2025.00092). The upstream public repository is `aryatschand/MLPerf-Power-HPCA-2025`.

## Scientific scope

This software does **not** claim novelty for Blackwell comparison, Le Cam deficiency, Pareto optimization, resource convertibility, reachability transitivity, quantum no-programming, or time-hierarchy results. Those are validation reductions or inherited ingredients. The scoped GC contribution is the organization of task, scale, error, composition, and multi-resource feasibility into whole embodied operational envelopes, together with their resource-scaled translations and dynamic reachable-envelope formulation.
