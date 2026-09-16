# GC-II Audit 172 — Minimal Sufficient Compositional Enrichment: Nerode Boundary

Status date: 2026-09-16
Branch scope: `gc2-capability-accounting-lab` only. GC-I/main unchanged.

## Objective

Attack Audit 171's surviving proposal: define a minimal sufficient compositional enrichment complexity `C_G` and seek growing lower bounds from GC-I projection irreducibility.

## Deterministic sequential setup

Fix a projected observation alphabet `Sigma`, a target exact capability predicate `L subseteq Sigma*`, and an online deterministic enrichment/controller with state set `Q`. After a prefix `u`, its state must retain exactly enough information to answer correctly after every possible continuation `z`.

Define the future-capability equivalence

`u ~_G v  iff  for every z in Sigma*,  [uz in L] = [vz in L]`.

Let `N_G` be the number of equivalence classes (possibly infinite).

## Exact minimal-enrichment theorem

Any deterministic exact sequential enrichment realizing the capability predicate requires at least `N_G` reachable states, and the quotient by `~_G` realizes it with exactly `N_G` states whenever `N_G` is finite. Therefore

`C_G = N_G`,

and the minimal bit memory is

`B_G = ceil(log2 N_G)`

for a finite exact state encoding.

### Proof

If `u` and `v` are inequivalent, some continuation `z` distinguishes them. If an exact deterministic enrichment mapped `u` and `v` to the same internal state, determinism would force the same state trajectory/output after reading `z`, contradicting exactness. Thus different `~_G` classes require different states.

Conversely, use the equivalence classes themselves as states, with transition `[u] --a--> [ua]`. Right-congruence of `~_G` makes this well-defined. Mark `[u]` accepting exactly when `u in L`. This realizes the target exactly.

**Status: PROVED, but IMPORTED/KNOWN: this is precisely the Myhill-Nerode theorem under GC terminology.**

## Consequence for the proposed GC-II novelty route

The unrestricted deterministic sequential quantity `C_G` is not a new capability invariant. It is the Nerode index/state complexity of the induced capability language. A linear bit lower bound or exponential state lower bound can therefore be genuine and useful for an application, but it is not by itself a new GC-II theorem.

In particular, choose a family whose target after arbitrary prefixes depends on the last `n` hidden/projected bits. There are `2^n` pairwise future-distinguishable suffix states, hence

`C_G(n) >= 2^n`,  `B_G(n) >= n`.

The matching shift-register construction stores those `n` bits, so equality holds for the canonical suffix family. This is the familiar exponential state-complexity phenomenon; it does not establish GC-II novelty.

## Relation to GC-I proper-projection irreducibility

GC-I proper-projection irreducibility can supply pairwise collisions under a local projection, but to imply a state lower bound it must be strengthened to **future distinguishability**: for every two projected-prefix classes counted separately, there must exist an admissible continuation that makes their required future capability decisions differ.

A static projection collision alone is insufficient. Many hidden microscopic states may have identical future capability behavior and therefore belong to one Nerode class.

Thus the correct bridge condition is:

1. construct a family of hidden worlds/prefixes `H_n`;
2. prove that for every distinct `h,h' in H_n` there exists an admissible continuation `z(h,h')` distinguishing the target capability;
3. conclude `C_G(n) >= |H_n|`;
4. only then translate to `log2 |H_n|` bits.

This bridge is mathematically valid but, without an additional GC-specific restriction, remains a Myhill-Nerode distinguishability argument.

## Edge and degenerate cases

- If all prefixes have identical future capability behavior, `N_G=1`; no nontrivial memory is required.
- If `N_G` is infinite, no finite deterministic exact enrichment exists.
- Unreachable prefixes should be excluded when counting operationally realizable enrichment states.
- Approximate/randomized evaluators are outside this exact theorem; their complexity requires error-sensitive information/communication arguments.
- Interactive multi-agent interfaces are outside the single-stream deterministic model and may reduce to communication/distributed synthesis rather than automata state complexity.
- Resource budgets that alter which continuations are admissible must be included in the state/continuation semantics; otherwise the equivalence is ill-defined.
- If budget/history can be compiled into sufficient state, Audit 162 applies and the Nerode theorem applies on the augmented alphabet/state semantics.

## Composition and invariance checks

The quotient state `[u]` is operationally invariant under future behavior by construction. Sequential composition is exact because right extension acts on equivalence classes. Relabeling hidden microscopic states without changing the induced continuation behavior leaves `N_G` invariant.

For independent product capability predicates, concatenating exact state encodings gives the general upper bound `C_{G1 x G2} <= C_{G1} C_{G2}` and hence `B_{G1 x G2} <= B_{G1}+B_{G2}` up to ceiling effects. Equality is not universal because product residuals can collapse.

## Prior-art collision boundary

The central result is the Myhill-Nerode characterization: the number of future-distinguishability classes equals the number of states in the minimal deterministic finite automaton. Classical subset/determinization examples already exhibit tight exponential state blow-up. Communication complexity and OBDD/branching-program methods provide related lower-bound machinery once the interface is split or restricted.

Therefore:

- minimal unrestricted exact sequential enrichment size: **IMPORTED/KNOWN**;
- exponential state lower bound from pairwise distinguishing continuations: **IMPORTED/KNOWN mechanism**;
- static projection fiber cardinality as a state lower bound without future distinguishability: **FALSIFIED**;
- GC-I-to-Nerode bridge under explicit future-distinguishability hypothesis: **PROVED / IMPORTED mechanism**;
- a genuinely new GC-II lower bound requires an operational restriction not already captured by arbitrary finite-state enrichment.

## Strong surviving target

The next credible target is **budget-constrained admissible Nerode complexity** rather than unrestricted `C_G`: restrict both (i) which enrichment transitions can physically/operationally be implemented under `R/I/A/L` budgets and (ii) which distinguishing continuations are admissible. Then ask whether a capability can have small ordinary Nerode index but provably large or infinite *admissible-realization* complexity because the canonical quotient transitions themselves cannot be implemented under the operational closure rules.

This must not be defined tautologically as minimum implementation cost. A breakthrough candidate would need a structural theorem coupling GC closure geometry to realization complexity and a finite family separating ordinary state complexity from admissible GC realization complexity, followed by collision checks against constrained automata, weighted automata, energy automata, VASS/Petri nets, synthesis under partial information, communication complexity, and resource-bounded computation.

## Status ledger

| Candidate | Status | Reason |
|---|---|---|
| Exact deterministic minimal enrichment `C_G=N_G` | PROVED / IMPORTED-KNOWN | Myhill-Nerode |
| Minimal bits `ceil(log2 N_G)` | PROVED | finite state encoding |
| Exponential state growth from `2^n` future-distinguishable histories | PROVED / IMPORTED-KNOWN mechanism | classical state complexity |
| Static projection fiber size alone lower-bounds enrichment | FALSIFIED | hidden worlds can share all future behavior |
| GC-I projection irreducibility + future distinguishability implies lower bound | PROVED / IMPORTED mechanism | Nerode argument |
| Unrestricted `C_G` as GC-II breakthrough | FALSIFIED | direct classical reduction |
| Budget-constrained admissible realization complexity | OPEN | must be structurally separated from known constrained automata/resource models |
