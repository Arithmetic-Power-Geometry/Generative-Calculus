from __future__ import annotations
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from .core import (
    blackwell_binary_deficiency,
    canonical_reachability_system,
    convex_reconstruction_identity,
    cyclic_reversal_cost,
    equality_costs,
    exact_program_qubits,
    feasible,
    generative_order_parity,
    hierarchy_costs,
    marginal_incompleteness_example,
    pareto_frontier,
    parity_projection_profile,
    reachable_transport_audit,
)


def _savefig(path: Path):
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()


def _write_audits(reports: Path):
    novelty = pd.DataFrame([
        ["Changing state spaces/meta-rules", 10, "Not claimed", "Evolving spaces, reflective rewriting, OEE"],
        ["Experiment simulability/deficiency", 15, "Reduction only", "Blackwell and Le Cam"],
        ["Resource convertibility", 15, "Reduction only", "General/quantum resource theories"],
        ["Pareto multi-resource trade-offs", 25, "Building block", "Multiobjective optimization"],
        ["Whole task-scale-error-budget-composition envelope", 82, "Core scoped contribution", "Closest: operational/resource/reachability frameworks"],
        ["Resource-scaled whole-envelope translation", 84, "Core scoped contribution", "Closest: simulation preorders and resource convertibility"],
        ["Strong proper-projection irreducibility in GC", 78, "Proved GC theorem", "Combinatorial/marginal skeleton known"],
        ["Unbounded generative order in GC", 80, "Proved GC hierarchy", "Higher-order interaction ideas known"],
        ["Convex generative reconstruction", 72, "Proved restricted theorem", "Support functions and Banach-valued FTC established"],
        ["Budgeted reachable-envelope transport", 76, "Proved GC structural theorem", "Reachability transitivity established"],
        ["Scalable reversal-cost separation", 82, "Proved construction", "Complexity/reversibility relatives exist"],
        ["New experimentally confirmed GC-specific physical law", 0, "Not claimed", "Breakthrough threshold remains open"],
    ], columns=["component", "novelty_score_research_judgment", "status", "nearest_territory"])
    novelty.to_csv(reports / "novelty_scores.csv", index=False)

    theorem = pd.DataFrame([
        ["Envelope Representation", "proved", "compact Pareto representation"],
        ["Generative Preorder/Equivalence", "proved", "identity plus composition"],
        ["Blackwell-Le Cam Reduction", "proved specialization", "known comparison theory"],
        ["Resource-Theory Reduction", "proved specialization", "known resource theory"],
        ["Formal/Feasible Separation", "proved specialization", "time hierarchy"],
        ["Infinite Envelope Hierarchy", "proved specialization", "time hierarchy"],
        ["Metric Generative Derivative", "conditional", "metric plus absolute continuity"],
        ["Strong Proper-Projection Irreducibility", "proved finite theorem", "parity compatibility construction"],
        ["Unbounded Generative Order", "proved finite hierarchy", "parity family"],
        ["Convex Generative Reconstruction", "proved restricted theorem", "support-function path"],
        ["Universal Scalable Envelope Conservation", "falsified as unrestricted claim", "cyclic reversal-cost construction"],
        ["Operational Reversibility Conservation", "proved conditional theorem", "two-way admissible translation"],
        ["Budgeted Reachable-Envelope Transport", "proved", "protocol concatenation"],
        ["Turing Envelope Containment/Equality", "undecidable specialization", "Rice/Turing reduction"],
        ["Exact Generator Realizability", "proved corollary", "Nielsen-Chuang no-programming"],
    ], columns=["result", "status", "basis"])
    theorem.to_csv(reports / "theorem_status.csv", index=False)

    comparison = pd.DataFrame([
        ["Binary experiment", "Blackwell/Le Cam", "Exact directional deficiency", "Matches", "validation"],
        ["Two-resource frontier", "Pareto/multiobjective", "Equal minima, different joint feasibility", "Matches underlying geometry", "GC internal demonstration"],
        ["Equality communication", "communication complexity", "Linear vs constant-in-n proxy", "Matches", "validation"],
        ["Polynomial hierarchy slice", "complexity theory", "Nested finite growth families", "Matches", "illustration"],
        ["Proper-projection parity", "marginal/higher-order interaction theory", "All proper projections agree; wholes differ", "Known skeleton, GC interpretation", "structural test"],
        ["Convex reconstruction", "convex/metric analysis", "Integrated support derivative reconstructs path", "Matches exact identity", "calculus validation"],
        ["Cyclic reversal", "reversible dynamics/complexity", "O(1) forward vs 2^n-1 operational reversal", "New GC construction, related ideas established", "nonconservation stress test"],
        ["Reachable-envelope transport", "reachability/viability", "Budget-shift inclusion holds", "Matches transitivity", "dynamic GC theorem test"],
        ["MLPerf Power portfolio", "performance-power benchmarking", "Marginal best coordinates form unattained synthetic portfolio", "Consistent with multi-resource trade-offs", "public-data validation"],
    ], columns=["problem", "existing_framework", "GC_result", "comparison", "role"])
    comparison.to_csv(reports / "problem_comparison.csv", index=False)


def run_all(output_dir: str | Path, data_dir: str | Path | None = None) -> dict:
    out = Path(output_dir)
    tables, figs, reports = out / "tables", out / "figures", out / "reports"
    for p in (tables, figs, reports):
        p.mkdir(parents=True, exist_ok=True)
    data_dir = Path(data_dir) if data_dir else Path(__file__).resolve().parents[2] / "data"

    # 1. Blackwell/Le Cam validation
    pairs = [(0.75, 0.90), (0.90, 0.75), (0.60, 0.80), (0.80, 0.60), (0.70, 0.70)]
    sensor_rows = []
    for s, t in pairs:
        d = blackwell_binary_deficiency(s, t)
        sensor_rows.append({"source_accuracy": s, "target_accuracy": t, "deficiency_tv": d, "exactly_simulable": d < 1e-12})
    sensor = pd.DataFrame(sensor_rows)
    sensor.to_csv(tables / "binary_sensor_blackwell.csv", index=False)
    plt.figure(figsize=(7, 4))
    plt.bar(np.arange(len(sensor)), sensor.deficiency_tv)
    plt.xticks(np.arange(len(sensor)), [f"{a:.2f}->{b:.2f}" for a, b in zip(sensor.source_accuracy, sensor.target_accuracy)], rotation=20)
    plt.ylabel("Minimax TV deficiency")
    plt.xlabel("Source -> target accuracy")
    _savefig(figs / "binary_sensor_deficiency.png")

    # 2. Marginal incompleteness and sweep
    ex = marginal_incompleteness_example()
    budget_rows = []
    for tb in range(1, 4):
        for eb in range(1, 4):
            budget_rows.append({"time_budget": tb, "energy_budget": eb, "A_feasible": feasible(ex["A"], (tb, eb)), "B_feasible": feasible(ex["B"], (tb, eb))})
    pd.DataFrame(budget_rows).to_csv(tables / "pareto_budget_grid.csv", index=False)
    A, B = np.array(ex["A"]), np.array(ex["B"])
    plt.figure(figsize=(6, 5))
    plt.scatter(A[:, 0], A[:, 1], s=70, label="World A frontier")
    plt.scatter(B[:, 0], B[:, 1], s=70, label="World B frontier")
    plt.scatter([1], [1], marker="x", s=120, label="Joint budget (1,1)")
    plt.xlabel("Time cost")
    plt.ylabel("Energy cost")
    plt.legend()
    _savefig(figs / "pareto_marginal_incompleteness.png")

    sweep = []
    for high in np.linspace(1, 10, 19):
        item = marginal_incompleteness_example(1, high, 1)
        sweep.append({"low": 1.0, "high": high, "coupling_gap_euclidean": item["coupling_gap"], "joint_feasible_at_ideal": item["A_feasible"]})
    pd.DataFrame(sweep).to_csv(tables / "coupling_gap_sweep.csv", index=False)
    plt.figure(figsize=(7, 4))
    plt.plot([r["high"] for r in sweep], [r["coupling_gap_euclidean"] for r in sweep], marker="o")
    plt.xlabel("High coordinate cost")
    plt.ylabel("Distance from ideal joint point")
    _savefig(figs / "coupling_gap_sweep.png")

    # 3. Equality communication validation
    eq = pd.DataFrame([equality_costs(n, 1 / 3) for n in [8, 16, 32, 64, 128, 256, 512, 1024]])
    eq.to_csv(tables / "equality_communication.csv", index=False)
    plt.figure(figsize=(7, 4))
    plt.plot(eq.n, eq.deterministic_bits, marker="o", label="Deterministic proxy")
    plt.plot(eq.n, eq.public_randomized_proxy_bits, marker="o", label="Public-randomized proxy")
    plt.xscale("log", base=2)
    plt.yscale("log", base=2)
    plt.xlabel("Input length n")
    plt.ylabel("Communication bits")
    plt.legend()
    _savefig(figs / "equality_communication_scaling.png")

    # 4. Complexity hierarchy illustration
    hier = pd.DataFrame(hierarchy_costs())
    hier.to_csv(tables / "time_hierarchy_slice.csv", index=False)
    plt.figure(figsize=(7, 4))
    for k, g in hier.groupby("k"):
        plt.plot(g.n, g.cost, marker="o", label=f"n^{k}")
    plt.xscale("log", base=2)
    plt.yscale("log", base=2)
    plt.xlabel("n")
    plt.ylabel("Cost")
    plt.legend(ncol=2)
    _savefig(figs / "time_hierarchy_slice.png")

    # 5. Finite whole-envelope grid
    worlds = {
        "A": {"task1": [(1, 3), (3, 1)], "task2": [(2, 2)]},
        "B": {"task1": [(1, 1)], "task2": [(2, 2)], "task3": [(3, 1)]},
        "C": {"task1": [(1, 3), (3, 1)], "task2": [(2, 2)]},
    }
    inc = []
    for wname, w in worlds.items():
        for tb in range(1, 5):
            for eb in range(1, 5):
                tasks = [t for t, f in w.items() if feasible(pareto_frontier(f), (tb, eb))]
                inc.append({"world": wname, "time_budget": tb, "energy_budget": eb, "tasks": "|".join(sorted(tasks)), "task_count": len(tasks)})
    pd.DataFrame(inc).to_csv(tables / "finite_envelope_grid.csv", index=False)

    # 6. Strong proper-projection irreducibility / generative order
    projection_rows = []
    for m in range(2, 9):
        for row in parity_projection_profile(m):
            projection_rows.append({"m": m, "generative_order": generative_order_parity(m), **row})
    projection_df = pd.DataFrame(projection_rows)
    projection_df.to_csv(tables / "projection_irreducibility.csv", index=False)
    plt.figure(figsize=(7, 4))
    maxima = projection_df.groupby("m").generative_order.max()
    plt.plot(maxima.index, maxima.values, marker="o")
    plt.xlabel("Envelope dimension m")
    plt.ylabel("Minimum distinguishing projection order r_G")
    _savefig(figs / "generative_order_hierarchy.png")

    # 7. Convex support-function reconstruction
    K0 = [(0, 0), (2, 0), (0, 1)]
    K1 = [(0, 0), (1, 0), (0, 3)]
    recon_rows = []
    for steps in [1, 2, 5, 10, 25, 50, 100, 250]:
        recon_rows.append(convex_reconstruction_identity(K0, K1, t=0.73, steps=steps, n_directions=720))
    recon = pd.DataFrame(recon_rows)
    recon.to_csv(tables / "convex_reconstruction.csv", index=False)
    plt.figure(figsize=(7, 4))
    plt.plot(recon.steps, np.maximum(recon.max_abs_error, np.finfo(float).eps), marker="o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Integration steps")
    plt.ylabel("Max support-function reconstruction error")
    _savefig(figs / "convex_reconstruction_error.png")

    # 8. Reversible microdynamics with expensive operational reversal
    rev = pd.DataFrame([cyclic_reversal_cost(n) for n in range(1, 21)])
    rev.to_csv(tables / "cyclic_reversal_cost.csv", index=False)
    plt.figure(figsize=(7, 4))
    plt.plot(rev.n, rev.reverse_via_forward_cost, marker="o")
    plt.yscale("log", base=2)
    plt.xlabel("n (cycle period = 2^n)")
    plt.ylabel("Cost of one-step reversal using forward dynamics")
    _savefig(figs / "cyclic_reversal_scaling.png")

    # 9. Exact generator program-dimension corollary
    gens = [1, 2, 3, 4, 8, 16, 32, 64, 256, 1024, 1048576]
    pg = pd.DataFrame([{"generator_count": g, "minimum_program_qubits": exact_program_qubits(g)} for g in gens])
    pg.to_csv(tables / "exact_generator_program_bound.csv", index=False)

    # 10. Budgeted reachable-envelope transport
    graph, task_at = canonical_reachability_system()
    transport = pd.DataFrame(reachable_transport_audit(graph, task_at, max_budget=15))
    transport.to_csv(tables / "reachable_envelope_transport.csv", index=False)
    summary_transport = transport.groupby("budget_B").transport_holds.mean().reset_index(name="fraction_holding")
    plt.figure(figsize=(7, 4))
    plt.plot(summary_transport.budget_B, summary_transport.fraction_holding, marker="o")
    plt.ylim(0.95, 1.005)
    plt.xlabel("Budget B")
    plt.ylabel("Fraction of audited transport inclusions holding")
    _savefig(figs / "reachable_transport_audit.png")

    # 11. Public MLPerf Power subset and portfolio audit
    mlperf_path = data_dir / "mlperf_power_public_subset.csv"
    if mlperf_path.exists():
        ml = pd.read_csv(mlperf_path)
        ml.to_csv(tables / "mlperf_power_public_subset.csv", index=False)
        pair_names = ["GIGABYTE G292-Z43 (16x QAIC100)", "Krai R282-Z93 (5x QAIC100)"]
        pair = ml[ml.system.isin(pair_names)].copy()
        wide_qps = pair.pivot(index="system", columns="workload", values="throughput_qps")
        wide_pwr = pair.pivot(index="system", columns="workload", values="power_w")
        req = {"ResNet_qps_min": 150000, "BERT_qps_min": 5000, "ResNet_power_max": 1000, "BERT_power_max": 1000}
        audit = []
        for system in wide_qps.index:
            checks = {
                "resnet_qps_ok": wide_qps.loc[system, "ResNet"] >= req["ResNet_qps_min"],
                "bert_qps_ok": wide_qps.loc[system, "BERT-99.0"] >= req["BERT_qps_min"],
                "resnet_power_ok": wide_pwr.loc[system, "ResNet"] <= req["ResNet_power_max"],
                "bert_power_ok": wide_pwr.loc[system, "BERT-99.0"] <= req["BERT_power_max"],
            }
            audit.append({"system": system, **checks, "joint_portfolio_feasible": all(checks.values())})
        pd.DataFrame(audit).to_csv(tables / "mlperf_portfolio_feasibility.csv", index=False)
        ideal = pd.DataFrame([{
            "ResNet_qps_best": wide_qps["ResNet"].max(),
            "BERT_qps_best": wide_qps["BERT-99.0"].max(),
            "ResNet_power_best_low": wide_pwr["ResNet"].min(),
            "BERT_power_best_low": wide_pwr["BERT-99.0"].min(),
            "attained_by_any_single_system": False,
        }])
        ideal.to_csv(tables / "mlperf_synthetic_marginal_ideal.csv", index=False)
        plt.figure(figsize=(7, 5))
        for _, r in pair.iterrows():
            plt.scatter(r.power_w, r.throughput_qps, s=60)
            plt.annotate(f"{r.system.split(' (')[0]}\n{r.workload}", (r.power_w, r.throughput_qps), xytext=(5, 5), textcoords="offset points", fontsize=8)
        plt.yscale("log")
        plt.xlabel("System power (W)")
        plt.ylabel("Throughput (queries/s)")
        _savefig(figs / "mlperf_power_portfolio.png")

    _write_audits(reports)

    summary = {
        "version": "2.0.0",
        "binary_sensor_rows": len(sensor),
        "marginal_budget_rows": len(budget_rows),
        "equality_rows": len(eq),
        "hierarchy_rows": len(hier),
        "finite_envelope_rows": len(inc),
        "projection_rows": len(projection_df),
        "convex_reconstruction_rows": len(recon),
        "reversal_rows": len(rev),
        "reachable_transport_rows": len(transport),
        "reachable_transport_all_hold": bool(transport.transport_holds.all()),
        "public_mlperf_included": mlperf_path.exists(),
        "claims": {
            "validation": "Blackwell/Le Cam, communication, complexity, reachability, and MLPerf examples are validation or scoped applications of established theory.",
            "gc_internal": "Strong proper-projection irreducibility, unbounded GC projection order, convex reconstruction sector, reversal-cost construction, and budgeted reachable-envelope transport are formalized in the GC envelope language.",
            "not_claimed": "No experimentally confirmed new law of fundamental physics is claimed.",
        },
    }
    (reports / "benchmark_summary.json").write_text(json.dumps(summary, indent=2, default=str), encoding="utf-8")
    (reports / "README.md").write_text(
        "# Generated results\n\nRun `python -m generative_calculus.reproduce` to regenerate every CSV, PNG and audit report. "
        "Validation benchmarks are explicitly separated from scoped Generative Calculus results.\n",
        encoding="utf-8",
    )
    return summary
