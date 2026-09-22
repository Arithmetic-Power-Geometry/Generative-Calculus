# GC-II Audit 319 — Joint-resolution gap and exact finite dynamic program

## Status

- Pairwise-separation cost as a complete closure-escape criterion: **FALSIFIED**.
- Unbounded gap between pairwise witness cost and joint exact-resolution cost: **PROVED**.
- Exact Bellman recurrence for the restricted finite deterministic diagnostic model: **PROVED / IMPORTED-KNOWN mechanism**.
- General transformed-state/state-dependent-cost version: **OPEN**; it requires augmented belief/resource state and must not be inferred from the restricted recurrence.
- Foundational novelty claim: **NOT MADE**.

## 1. Why this audit is needed

Audit 318 identified a quantifier obstruction: the existence, for every decision-incompatible pair, of some affordable separating policy does not imply the existence of one affordable policy resolving all decisions. This audit makes that obstruction quantitative and shows that the gap is unbounded.

The purpose is negative but important for Paper II: a Generative Novelty Gap or closure-escape cost cannot be defined as merely the largest/sum of cheapest pairwise witnesses and then advertised as a complete operational capability measure.

## 2. Restricted model used for the exact theorem

Let `X` be a finite hypothesis/state set and `d:X->D` an independently fixed decision label. Let `U` be a finite family of diagnostic actions. Each `u in U` has:

- deterministic observation map `Z_u:X->Y_u`;
- state-independent nonnegative cost `c(u)>=0`;
- no state transformation (the hidden state remains `x`).

Actions may be selected adaptively from previous observations. Repeated actions are unnecessary in this deterministic static model because they return the same observation and have nonnegative cost.

For a compatible set `B subseteq X`, write

`B_{u,y}={x in B: Z_u(x)=y}`.

Call `B` resolved when `d` is constant on `B`.

Define `V(B)` as the minimum worst-case additional cost of an adaptive policy that exactly resolves `d` on `B`; set `V(B)=+infinity` if impossible.

## 3. Exact recurrence

### Theorem 319.1 — finite joint-resolution dynamic program

For every nonempty `B`,

`V(B)=0` if `d` is constant on `B`, and otherwise

`V(B)=min_{u useful on B} [ c(u) + max_{y:B_{u,y} nonempty} V(B_{u,y}) ]`,

where an action is useful when every nonempty outcome cell is a strict subset of `B`. If no useful action exists, `V(B)=+infinity`.

### Proof

If `d` is constant, STOP resolves the decision at zero additional cost.

Otherwise, every finite resolving policy has a first action `u`. An action with only one nonempty cell does not reduce the compatible set; because costs are nonnegative and observations are deterministic, deleting such an action cannot hurt resolution or increase cost. Hence an optimal finite policy may start with a useful action.

After observing `y`, exactly the states in `B_{u,y}` remain compatible. The continuation must resolve that subproblem and therefore has worst-case additional cost at least `V(B_{u,y})`. Thus every policy beginning with `u` costs at least

`c(u)+max_y V(B_{u,y})`.

Conversely, choose for each nonempty outcome cell an optimal continuation attaining `V(B_{u,y})` (finite state/action sets imply the recurrence can be evaluated over strictly shrinking subsets; if a child is impossible its value is infinity). Concatenating `u` with those branch policies achieves exactly the displayed quantity. Minimizing over first actions proves the recurrence. QED.

### Domain checks

- Units: `V` and `c` have the same resource/cost units; no information quantity is added to a physical cost.
- Zero-cost actions are allowed. Because useful actions strictly shrink `B`, recursion still terminates.
- Constant `d` gives `V=0` regardless of state identifiability.
- If two differently labelled states have identical outcomes for every action, `V=+infinity`.
- Adding actions cannot increase `V`; deleting actions cannot decrease it.
- Decreasing action costs componentwise cannot increase `V`.

This recurrence is standard optimal decision-tree / active-identification machinery and is **IMPORTED/KNOWN in mechanism**.

## 4. Pairwise witness lower bound

For differently labelled states define

`p(x,x') = min{c(u): Z_u(x) != Z_u(x')}`,

with `p=+infinity` if no action separates them. Define

`P(B)=max_{x,x' in B: d(x)!=d(x')} p(x,x')`,

with `P(B)=0` when `d` is constant.

Whenever `V(B)<infinity`,

`P(B) <= V(B)`.

Indeed, a resolving decision tree must separate each differently labelled pair somewhere on their common transcript prefix, and the worst-case root-to-leaf cost is at least the cost of that separating action. Therefore `P` is a valid necessary lower bound.

The question is whether it is even approximately complete without extra structure. It is not.

## 5. Unbounded joint-resolution gap

### Theorem 319.2

There is no universal constant `C` such that

`V(B) <= C P(B)`

for all finite deterministic diagnostic systems with unit-cost binary actions.

### Construction

For integer `m>=1`, let

`X={0,1}^m`,

let every state have a distinct required decision label `d(x)=x`, and provide the `m` coordinate tests

`u_j(x)=x_j`,  `j=1,...,m`,

all with cost one.

Every distinct pair differs in at least one coordinate, hence

`P(X)=1`.

But every exact resolving policy is a binary decision tree with at least `2^m` leaves. A binary tree with all leaves at depth strictly less than `m` has fewer than `2^m` leaves, so some root-to-leaf path has length at least `m`. Testing all `m` coordinates attains worst-case cost `m`. Therefore

`V(X)=m`.

Thus

`V(X)/P(X)=m`,

which is unbounded. QED.

Equivalently, for `N=2^m` decision-distinct states, the ratio is `log_2 N` in this construction.

## 6. Consequence for GC-II capability accounting

The decisive point is not merely that pairwise separability and joint resolvability differ qualitatively. Their resource requirements can diverge without bound:

`cheap witness for every incompatible pair` does not imply `cheap globally resolving capability`.

Therefore any candidate quantitative closure-escape functional based only on cheapest pairwise separation witnesses loses an essential interaction term: the cost of composing distinctions into one admissible adaptive policy.

This is a concrete form of **capability non-composability under a shared budget**. The phrase is descriptive here, not a novelty claim; the mechanism is classical decision-tree complexity.

## 7. What this does and does not prove

**PROVED:**

1. Pairwise witness cost is a lower bound on joint resolution cost in the stated model.
2. The lower bound can be arbitrarily loose.
3. Exact joint resolution is characterized by the Bellman recurrence in the stated finite deterministic static model.

**FALSIFIED:**

1. `P(B)` as a complete quantitative Generative Novelty Gap.
2. Any universal constant-factor upper bound `V <= C P` without additional structural assumptions.
3. The idea that pairwise affordable escape witnesses alone certify affordable closure escape.

**OPEN:**

1. Weak structural assumptions under which pairwise or low-order witness costs approximate `V`.
2. A transformed-state recurrence for Audit 318's full `T_u` model with state-dependent charges and branchwise residual resources.
3. A non-tautological GC-II theorem that links conversion capability itself, rather than an externally chosen decision map, to a mandatory charged extension.
4. Approximation bounds using interaction/entropy/treewidth parameters that survive collision with optimal decision-tree theory.

## 8. Prior-art collision audit

The exact recurrence and the logarithmic identification phenomenon sit squarely inside established optimal decision-tree / active-learning / diagnosis theory. Minimum-cost identification trees and their hardness/approximation properties are known, including weighted testing and worst/expected-cost formulations. Blackwell/Le Cam theory separately supplies established experiment-comparison and deficiency notions. Accordingly none of those mechanisms is labeled novel here.

The valid GC-II use of Audit 319 is restrictive: it eliminates an over-simple candidate accounting law and forces any future Omega_G/Closure-Escape theorem to represent **joint adaptive composition cost**, not merely a catalogue of pairwise witnesses.
