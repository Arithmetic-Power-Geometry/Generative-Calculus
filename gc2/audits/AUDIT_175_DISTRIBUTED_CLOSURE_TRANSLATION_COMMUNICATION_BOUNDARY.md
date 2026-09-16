# GC-II Audit 175 — Distributed Closure Translation: Communication-Complexity Boundary

Status date: 2026-09-16
Branch scope: `gc2-capability-accounting-lab` only. GC-I/main unchanged.

## Objective

Attack Audit 174's surviving target: whether proper-projection irreducibility can be strengthened into an operational local-to-global translator lower bound when the information determining admissibility is split across components.

## Distributed closure translator model

Let component A observe local projection x in X and component B observe local projection y in Y. For a candidate global action/task a, exact budgeted closure determines an admissibility bit

    f_a(x,y) in {0,1}.

A distributed closure translator is a communication protocol which, using only the permitted local views and messages, outputs f_a(x,y) exactly for every admissible input pair. Define

    T_G(a) = minimum worst-case number of communicated bits

among exact deterministic translators for a. If multiple actions must be reconstructed, replace f_a by the vector-valued admissibility map F(x,y).

## Exact reduction theorem

For every finite two-component instance with unrestricted local computation and ordinary bit communication,

    T_G(a) = D(f_a),

where D(f_a) is deterministic two-party communication complexity.

Proof. Any GC translator is, by definition, a deterministic communication protocol computing f_a, hence costs at least D(f_a). Conversely any deterministic protocol for f_a is a valid translator under the stated communication model, hence T_G(a) <= D(f_a). Therefore equality holds.

Status: PROVED under the stated model / mechanism IMPORTED-KNOWN.

The same argument applies to randomized, one-way, nondeterministic, quantum, simultaneous-message, multiparty, or bounded-round variants after matching the GC communication rules to the corresponding standard protocol class. Merely changing the protocol class therefore does not by itself create a new invariant.

## Projection irreducibility is insufficient

A nontrivial projection fiber does not imply positive communication. Example: let global hidden state be (x,y), but let the required admissibility decision be f(x,y)=g(x). B's hidden coordinate may vary inside the projection fiber, yet A alone computes the decision and T_G=0.

Thus GC-I proper-projection irreducibility can imply a translator lower bound only after a stronger operational hypothesis: projected worlds must be separated by required global decisions in a way that forces cross-component dependence.

Status: PROVED by counterexample; projection-fiber size alone as communication lower bound is FALSIFIED.

## Rectangle/fooling-set translator lower bound

Let S={(x_i,y_i)}_{i=1}^M be a fooling set for f: all diagonal pairs have the same output b, while for every i != j at least one crossed pair (x_i,y_j) or (x_j,y_i) has output 1-b. Every deterministic protocol partitions X x Y into monochromatic rectangles. No monochromatic b-rectangle can contain two elements of S. Hence at least M protocol leaves are required and

    T_G >= ceil(log2 M).

This is a valid local-to-global translator lower bound, but it is exactly the classical fooling-set method.

Status: PROVED / IMPORTED-KNOWN.

## Exact finite stress families

### Equality family

x,y in {0,1}^n and f(x,y)=1 iff x=y. The diagonal {(z,z):z in {0,1}^n} is a fooling set of size 2^n, so exact deterministic translation needs at least n bits. A sends x using n bits, giving equality up to the conventional output/round accounting.

Status: PROVED / IMPORTED-KNOWN.

### Inner-product/parity family

For f(x,y)=<x,y> mod 2, standard rank/communication arguments give linear deterministic communication. This is again a renamed communication-complexity hard function, not a GC-specific lower bound.

Status: IMPORTED-KNOWN mechanism.

### Degenerate local family

If f(x,y)=g(x), communication is zero regardless of hidden multiplicity in y. This kills any theorem depending only on projection cardinality.

Status: PROVED.

## Dimension/domain checks

- T_G is measured in communicated bits; it cannot be added directly to physical R/I/A/L quantities unless a conversion/calibration map is explicitly supplied.
- Constant admissibility map: T_G=0.
- One component already holds a sufficient statistic: T_G may be 0 even with large global state.
- Unlimited shared preprocessing does not change deterministic communication if it is input-independent; input-dependent shared information changes the model and must be charged or represented explicitly.
- Randomization changes the relevant complexity from D(f) to the appropriate randomized complexity; error tolerance must be explicit.
- Interactive communication can be cheaper than one-way communication; the admissible interface determines the protocol class.
- If local computation is itself resource-bounded, the exact reduction becomes communication-plus-computation complexity rather than ordinary communication complexity.
- If messages consume physical resources, communication bits and R/I/A/L costs form a multi-resource implementation problem; no scalar conversion is automatic.

## Composition behavior

For independent tasks, running optimal protocols separately gives the upper bound

    T_G(f,g) <= T_G(f) + T_G(g),

but equality need not hold because joint coding, shared transcripts, correlations, or amortization may reduce total communication. Therefore no universal additive Omega_G follows.

Parallel repetition/direct-sum behavior requires explicit hypotheses and collides with direct-sum/direct-product questions in communication complexity.

## Local consistency versus global reconstruction

A second tempting GC route is to interpret compatible local closures as requiring a global closure. This also has a strong prior-art collision: marginal/contextuality frameworks formulate local compatibility versus existence of global sections, and database theory studies reconstruction/join structure and width/cover parameters. Therefore local-global inconsistency alone cannot be claimed as GC novelty.

The potentially nontrivial residual must couple at least two structures that standard single-axis reductions discard—for example, communication needed to reconstruct admissibility while transformations simultaneously consume/change resources and alter future interfaces. Even then, novelty requires proving that the joint quantity cannot be represented as a known communication/resource game, distributed synthesis problem, or multiobjective product construction.

## No-go theorem for unrestricted distributed translators

If a GC distributed closure problem has:

1. finite local inputs x,y;
2. an exact global admissibility/closure decision F(x,y);
3. unrestricted local computation;
4. communication governed by a standard protocol class P; and
5. no additional operational constraint beyond computing F,

then its minimum exact translator cost is exactly the P-communication complexity of F.

Consequently, no lower bound derived solely from the input-output communication matrix of F can constitute an independent GC-II capability invariant; it is a communication-complexity result under relabeling.

Status: PROVED under assumptions 1-5.

## Prior-art collision ledger

- deterministic/randomized communication complexity: exact reduction — IMPORTED/KNOWN;
- fooling sets, rectangle partitions, rank methods: translator lower-bound methods — IMPORTED/KNOWN;
- equality/index/disjointness/inner-product families: standard hard-function mechanisms — IMPORTED/KNOWN;
- distributed synthesis: collision required once local strategies and temporal objectives enter;
- database joins/decomposability/CSP width: collision required for relation-valued local-global reconstruction;
- marginal/contextuality/global-section obstructions: collision required for compatible-local/no-global constructions;
- multi-resource communication: collision required with communication under energy/cost constraints and network/resource games.

## Consequence for GC-II

Audit 174's distributed translator candidate is FALSIFIED as an independent breakthrough in the unrestricted finite two-party setting. A rigorous translator lower bound exists, but the exact invariant is classical communication complexity.

This is nevertheless a useful structural result for Paper II: GC-I projection irreducibility is not enough. The correct operational strengthening is future/task separation plus a specified interface restriction, and under ordinary bit interfaces the resulting lower bound is already communication complexity.

The next high-value gate is **coupled closure debt**: search for finite systems in which (i) local-to-global information transfer, (ii) resource expenditure/replenishment, and (iii) endogenous modification of future admissible interfaces are inseparable under composition, and test whether the optimal closure cost can or cannot be reduced to a product-state communication/resource game. A genuine candidate must separate systems that have the same ordinary communication matrix, same minimum resource costs, and same compiled transition behavior, yet differ under an admissible GC operational experiment. If no such pair exists under finite Markov assumptions, seek and prove a general product-compilation no-go theorem instead.

## Status ledger

| Candidate | Status | Reason |
|---|---|---|
| Distributed exact translator cost T_G | PROVED / IMPORTED-KNOWN | equals communication complexity under matched protocol model |
| Projection fiber size alone lower-bounds translation | FALSIFIED | hidden variation can be decision-irrelevant |
| Fooling-set local-to-global lower bound | PROVED / IMPORTED-KNOWN | classical rectangle argument |
| Equality-family n-bit lower bound | PROVED / IMPORTED-KNOWN | standard communication complexity |
| Local consistency/global reconstruction obstruction | IMPORTED-KNOWN boundary | contextuality/database collision |
| Distributed closure translation as independent GC-II breakthrough | FALSIFIED in unrestricted finite protocol setting | exact reduction |
| Coupled information-resource-interface closure debt | OPEN | next collision gate |