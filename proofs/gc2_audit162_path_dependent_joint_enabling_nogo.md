# GC-II Audit 162 — No-go for path-dependent joint enabling burden under sufficient-state semantics

## Candidate gate
Audit 161 left a proposed residual: a path-dependent joint enabling burden across resource, information, action/interface, and law/rule axes (`R,I,A,L`) that cannot be reduced to fixed-state planning, synthesis, Petri/VAS reachability, or ordinary resource conversion.

## Formal model
Let a finite operational system have histories `h=a_1...a_t`. Suppose there exists an exact sufficient-state map `sigma(h)=z` such that, conditional on `z`, all quantities relevant to future capability are determined:

1. enabled transformations `E(z)`;
2. successor `T(z,a)` for every `a in E(z)`;
3. current typed stocks/budgets `B(z)=(R,I,A,L)` and any interaction/catalyst/lock variables needed to determine future enabledness;
4. goal/closure predicate `G(z)`;
5. incremental accounting vector `c(z,a)` (or a scalar burden functional after including any finite-memory accumulator in `z`).

No additivity between the four axes is assumed. Nonlinear cross-terms, threshold effects, conversion, borrowing, replenishment, catalytic availability, and order-sensitive enabling are permitted provided their future-relevant memory is contained in `z`.

Define the minimum joint enabling burden

`J*(z0,G)=inf_{p:z0 -> G} Phi(p)`,

where `Phi` may be path-dependent but has finite/effective sufficient memory. Append the state of the evaluator of `Phi` to `z` if necessary.

## Sufficient-state compilation theorem — PROVED
Under the assumptions above, exact capability feasibility and minimum joint enabling burden reduce to reachability/optimal-path computation on the augmented directed transition system whose vertices are sufficient states `z` and whose edges are the admissible transitions `(z,a,T(z,a))`.

### Proof
Every admissible operational history induces exactly one path in the augmented graph by repeated application of `T`. Conversely, every graph path is an admissible operational history because edges exist only for actions in `E(z)`. By sufficiency, two histories reaching the same augmented state have identical future enabledness, successor semantics, closure status, and future accounting semantics. If `Phi` requires finite/effective history memory, that memory is included in the state, so the accumulated burden is preserved exactly. Hence feasible goal histories and graph paths to `G` are in bijective cost-preserving correspondence. Taking an infimum/minimum over either set gives the same value. QED.

## Consequence — decisive falsification
Path dependence and nonlinear `R/I/A/L` interaction do **not** by themselves create a new mathematical object. If the interaction has an exact sufficient operational state, it is ordinary augmented-state reachability/optimal control/planning with a richer state description.

Therefore a candidate `Omega_G` cannot claim novelty merely from:

- nonadditive `R-I-A-L` interactions;
- order-sensitive acquisition;
- thresholds or locks;
- resource conversion or replenishment;
- catalysts that must be present or returned;
- actions that enable later actions;
- finite-memory history-dependent costs.

All are absorbed into sufficient state without changing the capability question.

## No-Free-Capability corollary — CONDITIONAL but exact
Let `C_b(z0)` be budgeted closure in the compiled system. If every path from `z0` to target capability `g` crosses a cut `K` and every crossing transition requires a nonfree increment according to a nonnegative monotone accounting functional `m`, with minimum crossing requirement `delta>0`, then any realization of `g` has burden at least `delta`.

This is a valid lower bound, but in this unrestricted form it is a standard cut/path lower-bound argument and is not independent GC-II novelty.

## Edge/degenerate checks
- Zero-length goal: if `G(z0)` then minimum burden is zero when the empty path is free.
- Cycles: allowed; negative scalar cycles must be excluded or treated explicitly if an infimum rather than minimum is intended. Typed physical resource consumption can remain nonnegative while stocks may be replenished.
- Nonlinear interaction: preserved by storing the variables needed to evaluate it in `z`.
- Catalysis: preserved by catalyst possession/correlation/return-condition variables in `z`; catalysis is already a central phenomenon in general resource theories.
- Composition: no automatic additivity follows. Coupled products can share state, catalysts, information, or actions.
- Representation: bijective relabeling of sufficient states preserves feasibility and burden if transition/accounting labels are transported.
- Infinite state: theorem remains semantic when an exact effective sufficient representation exists, but decidability/complexity need not follow.
- No sufficient state: this is the only surviving logical escape from this theorem, but simply declaring irreducible history is not enough; a GC-II result would need a precise invariant/lower bound that cannot be compiled into an effective state without circularly encoding the answer.

## Prior-art collision — DECISIVE
General resource theories already formalize conversion under free operations, sequential/parallel composition, monotones, and catalysis. Multi-resource theories explicitly study transformations governed by several interacting conserved/resource quantities. Petri-net/resource-allocation models represent shared resources, assembly/disassembly, routing and state-dependent enabling. Planning models handle consumable resources and multiple execution modalities. Thus a finite/effective path-dependent joint-enabling model remains inside known state-transition/resource-conversion machinery after sufficient-state augmentation.

## Ledger
- Exact sufficient-state compilation for joint path-dependent burden: **PROVED**.
- Nonlinear/nonadditive `R,I,A,L` interaction as an escape from augmented-state reduction: **FALSIFIED**.
- Finite-memory path-dependent accounting as an escape: **FALSIFIED**.
- Cut-based No-Free-Capability lower bound: **PROVED under stated cut/monotone assumptions**, but **IMPORTED/KNOWN in mechanism**.
- Catalytic/resource-conversion enabling: **IMPORTED/KNOWN**.
- Representation-independent nontrivial `Omega_G` based only on joint enabling: **FALSIFIED under sufficient-state semantics**.
- A semantic obstruction to *existence of any exact effective sufficient state*, tied to GC-I projection irreducibility and yielding an operational quantitative consequence beyond communication/compilation lower bounds: **OPEN**.

## Breakthrough consequence
Audits 153–162 now support a general no-go pattern: whenever all future-relevant operational information can be represented by an exact effective sufficient state, changing which component evolves, adding path dependence, or coupling more resource axes does not escape standard transition-system semantics.

The next credible Paper-II gate should therefore not add another state variable. It should ask whether GC-I proper-projection irreducibility can imply a theorem of **uniform finite-interface insufficiency**: for a family of growing worlds, every translator/controller restricted to a fixed interface class fails on some globally distinguishable instances unless its interface complexity grows according to a proved lower bound. The novelty test must compare that bound directly with communication complexity, streaming/cell-probe lower bounds, CSP/database width, contextuality/marginal extension, and distributed synthesis. A GC-II breakthrough requires an operational quantity or equivalence that those theories do not already capture.