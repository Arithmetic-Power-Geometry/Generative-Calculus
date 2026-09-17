# GC-II Audit 196 — Simultaneous semantic–admissibility generation collision

## Question
Does allowing an operation to change both object-level semantics and the set/rules of future admissible operations escape ordinary transition-system and dynamic-network reductions?

## Finite operational model
A configuration is

\[
z=(x,\Theta),
\]

where `x` is object/world state and `Theta` is the currently enabled rule theory. A primitive meta-operation may have the form

\[
\rho:(x,\Theta)\mapsto(x',\Theta'),
\]

so one step may simultaneously change ordinary state and future admissibility/semantics.

## Proposition — finite meta-state compilation
For every finite system of the above form there is an ordinary labelled transition system `L` with state space

\[
Z=X\times\mathfrak T
\]

such that, for every initial configuration `z`, labelled one-step behavior and reachable closure are preserved exactly.

### Proof
Take each complete GC configuration `(x,Theta)` as one LTS state. For every admissible GC step

\[
(x,\Theta)\xrightarrow{a}(x',\Theta')
\]

insert exactly the corresponding labelled edge in `L`. This is a bijection on configurations and edges, hence preserves paths by induction on path length and therefore preserves reachable closure. No assumption that `Theta'=Theta` is used. QED.

## Consequence
Simultaneous generation/change of semantics and admissibility is **not**, by itself, an extensional escape from ordinary finite transition systems. Treating rules/theories as data is also a classical reflective-rewriting mechanism: rewriting logic/Maude can represent rewrite theories and terms at the metalevel and simulate deductions of represented theories. Therefore a GC-II novelty claim cannot rest merely on making rules first-class mutable state.

The compilation does **not** show that all useful quantitative accounting collapses. It shows that a candidate must impose a representation/resource restriction that makes flattening costly or impossible in the relevant uniform family. The surviving target is therefore a quantitative separation between a compact reflective/generative description and any admissibility-preserving flattened realization, with costs charged in explicitly typed resources. Any such separation must be checked against succinct representations, universal interpretation, circuit/program description complexity, dynamic complexity, and reflective rewriting.

## Exact experiment
`experiments/gc2_audit196_reflective_semantics_compilation.py` enumerates 25 two-rule catalogues over eight `(world,phase)` states. Modes include simultaneous world-bit changes and enabled-rule-set changes. It verifies exact edge equality and reachable-closure equality for every starting state.

## Status ledger
- Finite simultaneous semantic–admissibility meta-state compilation: **PROVED**.
- Reachable-closure preservation under that compilation: **PROVED**.
- Small exhaustive implementation check (25 catalogues, 8 states each): **NUMERICALLY SUPPORTED** for the implementation, not used as the proof.
- Rule/theory-as-data reflection mechanism: **IMPORTED/KNOWN** (rewriting logic / Maude reflection).
- Simultaneous semantic–admissibility generation alone as GC-II Closure-Escape: **FALSIFIED**.
- Quantitative lower bound for flattening a compact uniform reflective/generative family under typed budgets: **OPEN**.

## Edge/degenerate checks
Empty enabled theory gives no outgoing primitive steps and compiles identically. Identity semantic steps are retained. Pure semantic changes and pure admissibility changes are included as special cases. Simultaneous changes require no new proof case. Composition follows from path induction. Relabelling configurations/rules preserves the construction. The theorem is finite/extensional and deliberately makes no claim for infinite/noncomputable theory spaces or succinctness-preserving compilation.

## Prior-art collision notes
Rewriting logic is reflective: finitely presented rewrite theories and terms can be represented at the object/metalevel, with metalevel operations applying represented rules. Executable structural operational semantics in Maude likewise represents transitions as rewrites and inference rules as conditional rewrite rules. This is a stronger collision than dynamic topology alone because the rules defining behavior themselves are representable/manipulable data.

## Next gate
Do not search for another unrestricted extensional escape. Test **succinct reflective closure accounting**: construct uniform families where a compact rule-generating representation of size `s(n)` induces a flattened admissibility transition structure requiring size `S(n)`, then ask whether the separation remains after allowing universal interpreters and standard succinct automata/circuit encodings. Only a separation tied to GC's task–scale–error–budget closure, rather than generic description succinctness, should be promoted.
