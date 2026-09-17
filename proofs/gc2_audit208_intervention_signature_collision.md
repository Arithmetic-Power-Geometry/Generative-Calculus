# GC-II Audit 208 — intervention-signature type collision

## Target
Audit 207 left open whether physically grounded interface types can be defined as equivalence classes of intervention signatures, with translator costs obtained from measured resource consumption, and whether that object escapes standard interventional/testing equivalence plus quantitative resource accounting.

## Finite definition
Fix an admissible experiment library E. For system/interface x define its complete intervention signature

sigma_E(x) = ( Law(O_e | x), c_e(x) )_{e in E},

where the cost coordinate is included only when cost is actually measured by E. Define x ~_E y iff sigma_E(x)=sigma_E(y).

## Proposition 208.1 — signature equivalence is experiment equivalence
For complete signatures over E,

x ~_E y  iff  every e in E has the same observable law (and the same measured cost, if cost is part of the observable) on x and y.

**Status: PROVED.** This is extensional equality of the indexed family. It is not a new equivalence theorem. In causal language this is interventional equivalence relative to the admitted intervention family; in process/testing language it is testing equivalence relative to E.

## Proposition 208.2 — response signatures do not identify external translator cost
Let E observe only response behavior. Two implementations x,y can have identical sigma_E while an independently declared or externally measured translator consumes q resource units. Vary q while keeping all response experiments fixed. Then sigma_E is unchanged but translation cost changes.

**Status: PROVED by construction.** Therefore intervention signatures alone do not determine translator cost.

If resource consumption is added as an observable to E, the enriched signature distinguishes systems whenever measured costs differ. This repairs identifiability but does so by enlarging the experiment language. The resulting equivalence remains equality of all admitted experimental predictions.

## Exact finite witness
`experiments/gc2_audit208_intervention_signature_collision.py` enumerates a bit interface, three interventions (`idle`, `flip`, `reset0`), both inputs, and four exact rational resource costs. It verifies:

1. signature equality iff equality under every admitted intervention/input pair;
2. fixed response signature with multiple translator costs;
3. enriching the signature with measured cost separates the cost cases.

No stochastic approximation is used.

## Checks
- Domains: finite intervention/input spaces; costs are nonnegative rationals.
- Dimensions: response coordinates are outcomes; resource cost is not algebraically mixed with response coordinates.
- Degenerate cases: zero cost allowed and behaves correctly.
- Monotonicity: no monotonicity assumption is required.
- Invariance: renaming internal implementations leaves signatures unchanged.
- Composition: no composition theorem is claimed; cost composition needs an independently specified resource law.
- Counterexample: external cost varies at fixed response signature.
- Reduction: full intervention-signature equality reduces directly to established interventional/testing equivalence relative to the experiment family.

## Prior-art collision
Interventional equivalence of causal models is explicitly defined by equality of interventional distributions. Hauser and Buehlmann (JMLR 2012) characterize interventional Markov equivalence under intervention families; Yang, Katcoff and Uhler (ICML 2018) extend such equivalence classes to general interventions. Quantitative/cost structure still requires a declared or measured operational resource model.

## Ledger
- Complete intervention-signature equivalence: **PROVED / IMPORTED-KNOWN mechanism**.
- Response signature => translator cost: **FALSIFIED**.
- Cost-enriched signature identifiability: **PROVED**, but by experiment-language enrichment.
- Intervention-signature operational atoms alone as novel Omega_G: **FALSIFIED**.
- Novelty from merely appending measured resource cost: **NOT ESTABLISHED; collides with quantitative operational/resource models**.
- Surviving target: **OPEN** — seek a theorem coupling *changes in budgeted generative closure* to a lower bound on experimentally measured translator work that cannot be removed by experiment-language enrichment, state augmentation, or ordinary resource-theory simulation.
