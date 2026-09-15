# GC-II Audit 170 — Witness-Geometry Residual: Reliability/Provenance Collision

Status date: 2026-09-16
Branch scope: `gc2-capability-accounting-lab` only. GC-I/main unchanged.

## Objective

Attack Audit 169's surviving gate: find finite operational systems with identical all-pairs minimum closure-cost matrix `D` but operationally distinguishable witness geometry, then test whether the distinction escapes standard path/flow/reliability/provenance theory.

## Exact finite collision construction

Use a directed multigraph on states `X={s,u,t}` with nonnegative unit costs.

System A has edges

- `a: s -> t`, cost 1;
- `b: s -> u`, cost 1;
- `c: u -> t`, cost 1.

System B has all edges of A plus a second parallel edge

- `a': s -> t`, cost 1.

Both systems have exactly the same all-pairs minimum closure-cost matrix:

- diagonal entries 0;
- `D(s,u)=1`;
- `D(u,t)=1`;
- `D(s,t)=1`;
- reverse unreachable pairs are `+infinity`.

The extra parallel witness `a'` cannot improve any endpoint minimum distance, hence `D_A=D_B` exactly.

Nevertheless the systems are operationally distinguishable once admissible experiments include single-edge failure followed by a reachability query. Delete `a`. In A, `s` still reaches `t` through `s-u-t`, so this particular deletion alone does not separate the systems. Instead use the operational query `lambda(s,t)`: the maximum number of edge-disjoint `s->t` paths. In A, `lambda_A(s,t)=2` (`a` and `b,c`). In B, `lambda_B(s,t)=3` (`a`, `a'`, and `b,c`). Equivalently, an adversarial edge-failure experiment that asks for the minimum number of edge deletions required to destroy `s->t` reachability returns 2 in A and 3 in B.

Thus all-pairs shortest operational cost is not a complete invariant for failure-robust capability.

**Status: PROVED.**

## Theorem — minimum closure distance does not determine robust closure

There exist finite nonnegative-cost operational systems A and B on the same state set such that

`D_A(x,y)=D_B(x,y)` for every state pair `(x,y)`,

but their edge-connectivity capability differs:

`lambda_A(s,t) != lambda_B(s,t)`.

Proof is the explicit construction above. By the edge version of Menger/max-flow-min-cut, `lambda(s,t)` is also the minimum cardinality of an edge cut separating `s` from `t` in these unit-capacity systems.

Therefore a witness-geometry residual beyond `D` is real and operationally observable.

## But the residual is not a GC-II novelty

The surviving distinction is classical network survivability / max-flow-min-cut / disjoint-path structure. Network survivability explicitly studies connectivity under component failures and uses link- or node-disjoint paths. Network reliability similarly studies the probability that terminal connectivity survives component failures. Hence defining `Omega_G` as path multiplicity, disjoint-witness count, cut size, or robustness to witness deletion would relabel established graph/network invariants.

A second collision is provenance. Semiring provenance over graph/path queries is designed precisely to retain derivational information discarded by tropical/min-plus evaluation. The tropical semiring recovers least cost; richer provenance semirings retain counts, path features, symbolic derivations, and other witness information. Therefore the passage

`all witnesses -> min-cost D`

is a standard lossy semiring evaluation, and recovering richer witness structure is standard provenance/path algebra rather than a new generative invariant.

**Status: witness-geometry residual REAL / IMPORTED-KNOWN MECHANISMS. Independent novelty claim FALSIFIED for disjointness, cut robustness, multiplicity, and generic derivation provenance.**

## Operational identifiability check

Audit 164 is respected: `lambda(s,t)` is not inferred from `D`; it is exposed by an admissible operational stress experiment (edge suppression/failure plus reachability) or directly by a declared disjoint-witness query. If the operational interface does not permit any such intervention/query, then a multiplicity-dependent quantity remains unidentifiable from the `D`-only behavior.

This separates two statements that must not be conflated:

1. `D` does not determine witness geometry — PROVED.
2. witness geometry is automatically observable — FALSE; observability depends on the admitted operational interface.

## Edge/degenerate checks

- If there is only one `s->t` witness, `lambda=1` when reachable and 0 when unreachable.
- Parallel transformations are legitimate only when transformation identity is operationally meaningful; otherwise quotienting parallel edges removes this example. A simple-graph analogue can be obtained by adding equal-distance redundant routes while preserving the relevant endpoint distance profile, but then care is required to preserve all-pairs distances on the enlarged common state set.
- Zero-cost edges do not affect the connectivity argument, though they can create zero-distance equivalence classes.
- Non-unit capacities generalize `lambda` to max flow/min cut and therefore strengthen the prior-art collision rather than escape it.
- Probabilistic failures generalize the stress observable to network reliability, again known theory.
- Composition of independent systems depends on the declared failure model; no additive law is assumed.

## Consequence for Paper II

Audit 169's witness-geometry gate succeeds only as a separation from the scalar distance profile, not as a novelty gate. The obvious residuals are already organized by classical structures:

- shortest/minimum witness cost -> tropical/min-plus / Lawvere distance;
- witness count or symbolic derivation -> provenance semirings;
- disjoint witnesses / bottlenecks -> Menger, max-flow/min-cut;
- random witness failure -> network reliability;
- path-language restrictions -> automata/regular path queries;
- resource-labelled path feasibility -> multi-resource reachability / Petri-style models.

This suggests a stronger no-go direction: any GC-II witness observable obtained by applying a fixed semiring/quantale evaluation to the admissible derivation/path object is inherited from generic algebraic path evaluation. A genuinely new residual would need either (i) an operation on capability-generation witnesses not representable as standard path/derivation algebra under the chosen operational equivalence, or (ii) a theorem linking multiple established evaluations in a new constrained way that yields a falsifiable quantitative consequence.

## Status ledger

| Candidate | Status | Reason |
|---|---|---|
| Same all-pairs `D`, different witness geometry | PROVED | explicit finite multigraph pair |
| Edge-disjoint witness count `lambda` | PROVED distinguishable | max-flow/min-cut / Menger mechanism |
| Failure robustness residual | IMPORTED/KNOWN | network survivability/reliability |
| Generic witness multiplicity/provenance | IMPORTED/KNOWN | provenance/path semirings |
| Witness geometry as independent `Omega_G` | FALSIFIED for tested natural forms | direct prior-art reductions |
| Semiring/quantale path-evaluation no-go theorem | OPEN | needs precise scope and proof |
| Cross-evaluation coupling theorem | OPEN | must yield nontrivial quantitative consequence |

## Next exact attack

Formalize the admissible derivation object as a finite path category/free category (or appropriate quotient) and define a broad class of compositional witness evaluators `E`. Test whether every evaluator satisfying path-alternative and path-composition homomorphism laws factors through a semiring/quantale homomorphism. If yes, this gives a useful representation/no-go theorem: novelty cannot come merely from choosing another compositional witness score. Then search for the weakest operationally justified axiom whose violation is necessary for a genuinely generative residual.