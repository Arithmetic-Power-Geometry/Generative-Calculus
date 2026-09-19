# GC-II Audit 248 — Fixed-generator capability congruence

Status: **PROVED / IMPORTED-KNOWN mechanism; GC-specific novelty OPEN**

## Scope

This audit follows the Audit-247 extension-stability no-go. We now freeze a finite deterministic generator language rather than allowing arbitrary future state-separating extensions.

Let a finite operational system be

\[
\mathcal S=(X,O,F,\mathrm{En},T,c),
\]

where `X` is a finite state set, `O` is the declared typed generator language, `F` is the capability-goal set, `En_o(x)` says whether operation `o` is enabled at `x`, `T_o(x)` is its successor when enabled, and `c_o(x)>=0` is its execution cost. Types R/I/A/L are metadata unless their semantics impose additional restrictions.

## Exact fixed-language equivalence

Define partitions recursively. Initially

\[
x\equiv_0 y \iff [x\in F]=[y\in F].
\]

Given `equiv_k`, define `x equiv_{k+1} y` iff:

1. `x equiv_0 y`;
2. for every declared operation `o`, `En_o(x)=En_o(y)`;
3. whenever enabled, `c_o(x)=c_o(y)`; and
4. whenever enabled, `T_o(x) equiv_k T_o(y)`.

Because `X` is finite, refinement stabilizes after finitely many strict splits. Write the stable relation as `equiv_*`.

## Theorem 248.1 — operational congruence

If `x equiv_* y`, then every finite operation word has identical executability from `x` and `y`; when executable it has identical accumulated cost and ends in states with the same goal/non-goal status.

### Proof

Induct on word length. Length zero follows from equal goal status. For `o sigma`, stable equivalence gives equal enabledness of `o`; if enabled it gives equal immediate cost and equivalent successors. Apply the induction hypothesis to `sigma`. QED.

## Corollary 248.2 — exact minimum capability cost

For

\[
V_F(x)=\inf\{C(\pi):x\xrightarrow{\pi}F\},
\]

with `inf(empty)=+infinity`,

\[
x\equiv_*y \Longrightarrow V_F(x)=V_F(y).
\]

Thus quotienting by `equiv_*` preserves exact finite-language Closure-Escape and minimum generative cost.

## Theorem 248.3 — coarsest deterministic cost/goal congruence

Among equivalence relations that preserve goal membership and, for every operation, preserve enabledness, immediate cost, and successor equivalence, `equiv_*` is the coarsest one.

### Proof sketch

Any such congruence is contained in `equiv_0`. If it is contained in `equiv_k`, successor stability forces it to be contained in `equiv_{k+1}`. Induction and stabilization give containment in `equiv_*`. QED.

## Finite computable criterion

Partition refinement therefore supplies a finite complete signature for the **fixed declared deterministic language**. The signature is not a universal GC invariant: Audit 247 proves that arbitrary future state-separating generators can invalidate every nontrivial positive-gap compression.

## Edge cases checked

- Goal states: distinguished at depth zero.
- Dead ends: states with the same disabled-operation pattern remain equivalent unless later refinement separates reachable successors elsewhere.
- Zero-cost cycles: preserved because costs are compared transitionwise; no positivity assumption is used.
- Unreachable goal: equivalent states remain jointly unreachable, hence both have value `+infinity`.
- Operation order: fully retained by successor refinement; no commutativity assumption.
- R/I/A/L labels alone: insufficient unless the declared semantics force the transition conditions above.
- Extension stability: **not claimed**. Adding a new generator can split stable classes, exactly as Audit 247 requires.

## Novelty collision

The mathematical mechanism is standard deterministic bisimulation / partition refinement and cost-preserving abstraction. It must be classified **IMPORTED/KNOWN**, not a GC-II breakthrough. Planning literature explicitly uses bisimulation-like abstractions to preserve perfect heuristic information, and cost-preserving bisimulation is established for weighted/probabilistic transition systems.

## Scientific consequence

The Paper-II search space is now cleanly divided:

- unrestricted endogenous generator extension: nontrivial complete compression is impossible (Audit 247);
- fixed declared generator language: exact coarsest congruence exists and is computable (Audit 248), but the mechanism is known;
- surviving GC-II novelty target: prove that a semantically restricted R/I/A/L generator grammar induces a **strictly cheaper structural signature or quantitative law** than generic transition-system refinement, without defining the restriction merely to force the desired theorem.

## Ledger

- Stable fixed-language congruence: **PROVED**.
- Exact preservation of executable traces and costs: **PROVED**.
- Exact preservation of minimum capability cost: **PROVED**.
- Coarsest congruence under the stated deterministic transition semantics: **PROVED**.
- Generic bisimulation/partition-refinement mechanism: **IMPORTED/KNOWN**.
- Universal extension-stable nontrivial quotient: **FALSIFIED by Audit 247**.
- GC-specific smaller complete signature derived from non-ad-hoc R/I/A/L semantics: **OPEN**.
