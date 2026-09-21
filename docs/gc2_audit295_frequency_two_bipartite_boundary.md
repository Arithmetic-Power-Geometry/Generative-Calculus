# GC-II Audit 295 — Frequency-two bipartite tractability boundary

## Scope
This audit continues Audits 290–294 on finite worst-case capability accounting. It does not alter GC-I foundations.

## Setup
Let Y be a finite attainable-state set, A a finite decoder-action set, and let B_0(a)={y in Y : ell(y,a)=0}. Assume every nontrivial target y is feasible for exactly two distinct actions. Construct the action-incidence graph G=(A,E) by assigning one edge e_y={a,b} for each target y whose feasible-action set is {a,b}. Duplicate targets may induce parallel edges; they do not change the minimum vertex-cover number and may be merged for optimization.

A zero-loss accounting state chooses one decoder action. Hence a family C subseteq A is a valid account exactly when every target has at least one feasible action in C, equivalently when C meets every edge of G.

## Theorem 295.1 — exact graph reduction
For frequency-two zero-loss instances,

    N_0 = tau(G),

where N_0 is the minimum number of decoder states/actions needed and tau(G) is the minimum vertex-cover number of the action-incidence graph.

### Proof
C covers every target iff for every edge e_y={a,b}, C contains a or b. This is precisely the definition of a vertex cover. Minimizing |C| on both sides gives equality. QED.

Status: PROVED.

## Theorem 295.2 — bipartite frequency-two tractability
If the action-incidence graph G is bipartite, then

    N_0 = tau(G) = nu(G),

where nu(G) is the maximum matching number. Consequently the optimum account is computable in polynomial time by maximum bipartite matching followed by standard minimum-vertex-cover recovery.

### Proof
The first equality is Theorem 295.1. The second is Konig's theorem for finite bipartite graphs. Polynomial-time matching and cover recovery are classical. QED.

Status: PROVED, using IMPORTED/KNOWN Konig theorem and bipartite matching algorithms.

## Sharp contrast with Audit 294
Audit 294 established NP-hardness already when every target has exactly two feasible actions, by realizing arbitrary graphs. Audit 295 shows that frequency two is not itself the source of hardness: the global incidence geometry matters.

    frequency <= 1                         -> trivial exact accounting
    frequency = 2 + bipartite incidence   -> polynomial exact accounting
    frequency = 2 + unrestricted incidence-> NP-hard in general

The obstruction separating the latter two classes is therefore not local target ambiguity but global non-bipartite incidence structure.

## Edge and degenerate cases
- Empty target set: N_0=0=tau=nu.
- Isolated decoder actions: irrelevant to all three quantities.
- Duplicate targets with the same action pair: parallel edges do not alter tau; one representative edge suffices.
- Disconnected incidence: tau and nu add across connected components.
- A target with zero feasible actions is infeasible rather than a cover instance and must be detected before applying the theorem.
- Frequency-one targets can be represented as forced actions and preprocessed; Theorem 295.2 is stated for the exact frequency-two core.

## Composition behavior
Disjoint union is additive: N_0(G1 disjoint-union G2)=N_0(G1)+N_0(G2). Bipartiteness is preserved under disjoint union. General interface composition need not preserve bipartiteness; a newly induced odd cycle can leave the tractable subclass.

## Prior-art collision discipline
The graph reduction is elementary and Konig's theorem / polynomial bipartite matching are classical. They are IMPORTED/KNOWN and are not novelty claims. The GC-II contribution of this audit is the operational classification obtained after the exact feasible-action reduction: a directly testable global incidence condition separates a polynomial frequency-two subclass from Audit 294's NP-hard unrestricted frequency-two class.

## Exact finite verification
The companion verifier `experiments/gc2_audit295_bipartite_frequency_two.py` exhaustively enumerates every labeled bipartite graph with left and right part sizes 1..3 (682 graphs total; 2,753 edge occurrences across the enumeration), computes minimum vertex cover by brute force, computes maximum matching independently by brute force, and asserts equality. It also checks empty, disconnected, duplicate-target and forced-frequency-one preprocessing cases.

## Status ledger
- Frequency-two account = vertex cover: PROVED.
- Bipartite frequency-two account = maximum matching number: PROVED via IMPORTED/KNOWN theorem.
- Polynomial exact accounting for this subclass: PROVED.
- Bounded local ambiguity alone implies tractability: FALSIFIED by Audit 294.
- Bipartite incidence is necessary for tractability: NOT CLAIMED / false as a general necessity; many non-bipartite special classes are tractable.
- Strongest operational global-incidence criterion: OPEN.
