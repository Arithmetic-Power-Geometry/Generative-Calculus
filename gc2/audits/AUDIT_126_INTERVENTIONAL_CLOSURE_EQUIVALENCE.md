# GC-II Audit 126 — Interventional Closure Equivalence

Status: **DECISIVE FALSIFICATION of the counterfactual/interventional closure-response route as standalone GC-II novelty**

## Question
Can two systems have identical complete factual reachable augmented-state graphs and identical typed path-cost sets, yet differ in closure response under an independently specified intervention family, in a way that supplies a new GC-II invariant?

## Formal setup
Let a finite operational mechanism be `M=(Z,U,T,c)` and let `J` be an independently specified intervention family on the admissibility/transition generator. For `j in J`, write `M^j` for the intervened mechanism. For a fixed start state, horizon and typed budget convention define the closure response

`C_j(M) = (Reach(M^j), CostSet(M^j))`.

Define interventional closure equivalence

`M ≡_J N  iff  C_j(M)=C_j(N) for every j in J`.

A natural discrepancy is

`Omega_J(M,N)=sup_{j in J} d(C_j(M),C_j(N))`

for a declared response metric/pseudometric `d`.

## Proposition 126.1 — Factual equivalence does not imply interventional equivalence
**PROVED.** Equality at the factual intervention `j0` constrains only `C_j0`; it does not constrain another `C_j` without assumptions linking mechanisms across interventions.

Minimal binary witness: let intervention `j∈{0,1}` and a one-step deterministic response `f(j)∈{0,1}`. Take `f=(0,0)` and `g=(0,1)`. At factual `j=0` the reachable graph and zero typed path-cost set are identical. At `j=1`, terminal reachability differs.

## Proposition 126.2 — Complete intervention signature criterion
**PROVED but definitional/tautological.** For fixed `J`, equality of the complete response signature

`Sigma_J(M)=(C_j(M))_{j∈J}`

is necessary and sufficient for equivalence under all interventions in `J`. Consequently `Omega_J=0` is a complete criterion only when `d` separates the declared responses. This does not supply a new capability law; it repackages equivalence over a query/intervention class.

## Exact finite exhaustive test
The checker enumerates all four deterministic binary mechanisms `f:{0,1}->{0,1}` and all ordered pairs. Among the 8 ordered pairs with identical factual response at `j=0`, exactly 4 are separated by intervention `j=1`. Zero-cost edges make factual typed path-cost sets identical automatically, so the witness satisfies the stronger factual-graph + path-cost premise.

Expected frozen result: 4 mechanisms; 16 ordered pairs; 8 factually equivalent pairs; 4 intervention-separated pairs; 4 fully interventionally equivalent pairs; 0 signature-criterion mismatches.

## Prior-art collision
This phenomenon is the standard distinction between observational/factual and interventional equivalence/identifiability in causal inference. Interventional Markov equivalence is strictly finer than observational Markov equivalence under suitable interventions (Hauser & Bühlmann, JMLR 2012). Otsuka & Saigo (CLeaR/PMLR 2022) explicitly study equivalence of causal models together with translation of intervention calculi. Parametric MDPs likewise instantiate a family of transition systems by parameter valuation, so differing responses across mechanism/parameter interventions are already native to established models.

## Status ledger
- factual equivalence need not imply intervention equivalence: **PROVED**
- complete intervention-response signature criterion: **PROVED, but tautological**
- finite exhaustive witness: **NUMERICALLY SUPPORTED / exhaustive**
- observational vs interventional equivalence: **IMPORTED/KNOWN**
- parametric transition families: **IMPORTED/KNOWN**
- `Omega_J` as worst-intervention response discrepancy: **FALSIFIED as standalone GC-II novelty**
- a nontrivial GC-II theorem requiring less than the full intervention signature while giving a complete quantitative capability bound: **OPEN**

## Consequence for Paper II
Do not claim novelty from the mere existence of systems that agree factually but separate under interventions, nor from defining the supremum discrepancy over an intervention family. A surviving route must prove a structural compression theorem, lower bound, or restricted finite/computable certificate for intervention-complete capability accounting that is not already causal identifiability, testing equivalence, robust/parametric reachability, or standard resource monotonicity.
