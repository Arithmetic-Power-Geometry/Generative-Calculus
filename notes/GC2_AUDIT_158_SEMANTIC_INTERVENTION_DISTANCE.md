# GC-II Audit 158 — semantic intervention distance collision

## Candidate
After quotienting operational systems by a chosen semantic equivalence `~`, let `X=[M]`, `Y=[N]`.  Given admissible semantic interventions `e:X->Y` with nonnegative cost `kappa(e)`, define

`Omega_sem(X,Y) = inf { kappa(e) : e maps X to a class whose budgeted closure contains the target represented by Y }`.

Assume identity interventions have zero cost and composable interventions satisfy `kappa(f o e) <= kappa(e)+kappa(f)`.

## Proposition (directed-semimetric no-go)
Under those assumptions Omega_sem is nonnegative, vanishes on already-convertible targets, and obeys the directed triangle inequality whenever the relevant interventions compose.  Hence the quotient construction is a Lawvere-style directed distance / conversion-cost geometry on semantic classes.  If zero cost is identified with convertibility rather than equality, it is naturally a hemimetric on the conversion preorder.

Proof: identity gives the zero case.  For X->Y and Y->Z interventions within epsilon of their respective infima, composition gives an X->Z intervention of cost at most their summed costs; take infima and epsilon->0.  No symmetry follows.

This is useful structure but is not an independent GC-II breakthrough: quantitative simulation/interface distances already turn behavioural refinement/simulation into directed distances with triangle/composition properties, and general resource theories already organize convertibility by preorders and monotones.  Therefore merely quotienting first and minimizing semantic intervention cost does not escape those frameworks.

## Exact finite regression
`experiments/gc2_audit158_semantic_intervention_distance.py` enumerates all 16 closures A subseteq {0,1,2,3} with d(A,B)=|B\\A|.  It checks 256 ordered pairs and 4096 ordered triples. Frozen result: zero preorder violations = 0; triangle violations = 0.

## Status ledger
- Semantic quotient before measurement: PROVED representation-invariant relative to the chosen semantic equivalence.
- Directed triangle law: PROVED under composability/subadditive intervention cost.
- Finite regression: PASS.
- Semantic intervention distance alone as independent Omega_G novelty: FALSIFIED.
- Quantitative simulation/interface distance and general resource convertibility: IMPORTED/KNOWN.
- A GC-II-specific residual not reducible to conversion/simulation distance: OPEN.

## Surviving gate
Do not search for another distance on semantic classes.  The next candidate must concern a property that conversion-distance formalisms deliberately quotient away.  A promising target is *closure creation under endogenous task formation*: compare systems whose current operational conversion structure is identical, but in which admissible task/specification formation can expose different future closure obligations.  This must be tested first against endogenous preferences/tasks, games with changing objectives, hyperproperties, institution/action-model change, and scientific-discovery formalisms before any novelty claim.
