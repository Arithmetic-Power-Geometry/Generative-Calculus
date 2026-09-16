# GC-II Audit 178 — Interpreter-relative recovery product no-go

Status: **PROVED / IMPORTED-KNOWN mechanism; novelty route FALSIFIED under finite Markov assumptions**

## Question
Audit 177 left open whether an interpreter-relative recovery quantity could escape ordinary forward/reverse closure cost. Fix an operational system with finite Markov-sufficient state set `S`, admissible labelled transitions `E`, nonnegative transition costs, and a scientifically fixed interpreter class `K`. Each interpreter has finite internal state `Q_k`; its state updates from the current operational transition and determines which recovery actions it may issue. Let `F_x` denote the required future-closure signature of the pre-intervention state `x`.

For an intervention taking `x` to `y`, define

\[
R_K(x\to y)=\inf\{\operatorname{cost}(\pi): \pi \text{ is a K-admissible recovery execution from }y\text{ to some }z\text{ with }F_z=F_x\}.
\]

The Audit-177 residual was

\[
\Omega^{\rm rev}_{G,K}(x,y)=R_K(x\to y)-D(y,x)
\]

when both terms are finite.

## Theorem 178.1 — finite-interpreter product compilation
Assume:

1. `S` is finite and Markov-sufficient for operational evolution and future-closure evaluation;
2. every `k in K` has finite internal state `Q_k`;
3. interpreter updates and enabled recovery actions depend only on the current pair `(s,q)` and selected transition/action;
4. transition costs are nonnegative and Markovian;
5. recovery success is determined by membership in the target set `T_x={z:F_z=F_x}`.

Then `R_K(x->y)` is exactly a shortest-path value on the finite product graph

\[
P_K=\bigsqcup_{k\in K}(S\times Q_k),
\]

with target vertices `(z,q)` satisfying `z in T_x`. Consequently `R_K` adds no behavioral expressivity beyond ordinary finite weighted-state planning on this product.

### Proof
For every K-admissible recovery step from `(s,q)` to `(s',q')`, insert a product edge with exactly the same cost. Conversely, every product edge is inserted only from a K-admissible recovery step. Induction on path length gives a cost-preserving bijection between finite K-admissible recovery executions and product paths from the initialized `(y,q0)` vertices. Recovery succeeds exactly at the stated target vertices. Taking the infimum over corresponding path costs proves equality. Nonnegative finite graphs permit the standard shortest-path interpretation; unreachable targets have value `+infinity`. QED.

## Corollary 178.2 — residual novelty failure
Under Theorem 178.1, any scalar residual computed solely from `R_K` and ordinary closure distances is a derived statistic of a compiled weighted transition system. In particular, `Omega_rev_GK=R_K-D_reverse` can quantify a restriction penalty, but cannot by itself establish a new GC-II invariant.

## Edge and degeneracy checks
- If `y` already has `F_y=F_x`, recovery cost is `0` provided the initialized product state is accepted.
- If no product target is reachable, `R_K=+infinity`.
- Zero-cost cycles do not alter the infimum.
- If `K` contains an unrestricted controller whose actions reproduce the base system, `R_K` can collapse to an ordinary target-set shortest-path cost.
- Distinct states with identical future-closure signatures are intentionally valid recovery targets: recovery concerns capability, not microscopic identity.
- Negative costs are excluded; otherwise negative cycles require a different optimization semantics.
- A finite family `K` is handled by disjoint union; a single finite meta-controller is equivalent.
- If interpreter memory is unbounded, the theorem does not assert finite compilation.

## Composition/invariance checks
Relabelling operational or interpreter states preserves `R_K`. Independent product composition remains an ordinary larger product construction. Thus finite coupling between interpreter memory and R/I/A/L variables is already covered by the Audit-176 finite-product boundary.

## Prior-art collision boundary
The mathematical mechanism is finite-state product construction plus shortest-path/planning. Reversible-computation work already studies recovery/uncomputation under explicit machine restrictions and time/space tradeoffs (Bennett 1973/1989; Levine-Sherman 1990; Li-Vitanyi 1997). Therefore merely fixing an interpreter class and measuring restoration cost does not clear the novelty gate.

## Ledger
- finite-interpreter recovery product theorem: **PROVED**
- shortest-path characterization of `R_K`: **PROVED / IMPORTED-KNOWN mechanism**
- `Omega_rev_GK` as independent GC-II novelty under these assumptions: **FALSIFIED**
- unbounded/non-finitely-compilable interpreter recovery: **OPEN**, but novelty not established
- uniform lower bounds for restricted *families* of interpreters: **OPEN**, collision risk with automata/state/communication/descriptional complexity

## Stronger surviving gate
Do not pursue another scalar recovery cost without first exhibiting an operational distinction that survives finite product compilation. A defensible next target is a **uniform-family theorem**: parameterized systems `G_n` and a fixed syntactically/physically justified compiler class `K` for which every admissible interpreter restoring a specified closure family requires a quantitatively growing resource jointly involving interpreter description/memory and R/I/A/L expenditure. Any such lower bound must then be proved not to be a direct restatement of automata state complexity, communication complexity, reversible pebbling, planning complexity, or circuit/branching-program lower bounds.
