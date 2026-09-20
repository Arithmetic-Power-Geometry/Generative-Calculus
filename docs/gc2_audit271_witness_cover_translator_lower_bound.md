# GC-II Audit 271 — Witness-cover local-to-global translator lower bound

## Target
Strengthen the Audit-226 no-go result into a positive operational lower bound: if a capability valuation has genuinely high-order interaction, what must an operational translator pay in local witness complexity?

## Setting
Let augmentation coordinates be `N={1,...,n}`. A finite monotone operational system has a start state and target. Each transition gate reads at most `k` augmentation coordinates. Restrict attention to target-reaching witness paths of length at most `L`. Remove redundant paths and let `W={W_1,...,W_P}` be the family of distinct minimal augmentation requirement sets induced by target-reaching paths. Thus the reachability valuation is

    v(S) = 1 iff there exists j with W_j subseteq S.

Equivalently, on Boolean variables x_i=1[i in S],

    v(x) = OR_{j=1}^P AND_{i in W_j} x_i.

Every witness path contains at most L gates and each gate reads at most k coordinates, hence |W_j| <= kL.

Let `deg(v)` denote the degree of the unique real multilinear polynomial representing v on the Boolean cube. This equals the maximum order of a nonzero real Möbius coefficient of the set function v.

## Theorem — witness-cover degree bound
For every such system,

    deg(v) <= | union_j W_j | <= sum_j |W_j| <= P k L.

Therefore, if v has a nonzero interaction of order d,

    P L >= ceil(d/k).

In particular, an n-way interaction requires

    P L >= ceil(n/k).

### Proof
For a witness W_j define its conjunction monomial

    a_j(x) = product_{i in W_j} x_i.

Boolean OR has the exact real-polynomial identity

    v(x) = 1 - product_{j=1}^P (1-a_j(x)).

After multilinear reduction x_i^r=x_i on {0,1}^n, every resulting monomial uses variables only from `union_j W_j`. Hence its degree is at most the cardinality of that union. The union bound gives

    |union_j W_j| <= sum_j |W_j| <= P k L.

If the real Möbius transform has a nonzero coefficient of order d, the unique multilinear polynomial has degree at least d, so d <= PkL. QED.

## Sharpness
The bound is exact. Take P parallel witness paths whose requirement blocks are pairwise disjoint, each block containing q=kL augmentation coordinates (realized by L serial gates, each reading k fresh coordinates). Then

    v = OR_{j=1}^P AND_{i in W_j} x_i,

with |W_j|=kL and disjoint blocks. Inclusion-exclusion contains the full-union monomial

    (-1)^(P+1) product_{i in union_j W_j} x_i,

so

    deg(v)=P k L.

Thus no universal improvement of the product bound is possible without additional overlap/topology/semantic assumptions.

## Consequences for GC-II
1. Audit 226 showed that primitive gate arity alone cannot bound global interaction order. Audit 271 identifies an explicit compensating quantity: **witness multiplicity × witness depth**.
2. Bounded depth alone is insufficient: P parallel unary one-step witnesses implement OR of P coordinates and have degree P.
3. Bounded witness count alone is insufficient: one serial unary path of length L implements an L-way AND and has degree L.
4. A local-to-global translator that realizes d-th-order capability interaction using k-local gates must pay at least d/k in the product P L. This is an operational translator lower bound, not merely a statement that high-order terms can occur.
5. The result does not yet give a bounded-treewidth theorem. Treewidth/causal-graph width without control of witness structure is not enough in general planning settings.

## Domains, invariance, composition, degeneracies
- `k,L,P,d` are nonnegative integers; the nontrivial theorem assumes a reachable target and P>=1.
- Empty witness W_j gives constant-1 reachability and degree 0; the inequalities remain valid.
- Duplicate or dominated witness sets may be deleted without changing v; P is therefore counted after minimalization.
- Relabeling augmentation coordinates leaves all quantities invariant.
- Parallel composition increases P and can increase degree through OR inclusion-exclusion; serial composition increases L and can increase degree through conjunction.
- Overlapping witness requirements can only decrease `|union W_j|` relative to `sum |W_j|`; cancellations can reduce degree further, so the theorem is an upper bound, not an equality claim.
- Costs/resources are not needed for this structural theorem. A budgeted version can apply it to the Boolean feasibility valuation at a fixed budget, provided the corresponding feasible-witness family satisfies the same k/L restrictions.

## Prior-art collision
The algebraic mechanism is **IMPORTED/KNOWN**. Exact real multilinear representations of Boolean functions and their degree are classical; DNF is an OR of conjunctions, and the displayed identity is elementary inclusion-exclusion. Boolean polynomial degree is a mature complexity measure (e.g. Nisan–Szegedy). Planning literature likewise shows that local/unary operators and simple causal graphs do not automatically make global planning easy; restricted polytree/chain results require additional assumptions.

The GC-II-specific value is the operational translation: interaction order d forces the exact lower bound `P L >= ceil(d/k)` for k-local witness-path realizations, and the disjoint-block construction proves sharpness. This should not be advertised as invention of Boolean polynomial degree or DNF algebra.

## Status ledger
- `deg(v) <= |union W_j| <= PkL`: **PROVED**.
- Translator lower bound `PL >= ceil(d/k)`: **PROVED**.
- Sharpness for every P,k,L>=1 by disjoint witness blocks: **PROVED**.
- Primitive locality + bounded depth alone implies bounded interaction: **FALSIFIED**.
- Primitive locality + bounded witness count alone implies bounded interaction: **FALSIFIED**.
- Boolean/DNF polynomial mechanism: **IMPORTED/KNOWN**.
- A stronger width-only local-to-global theorem for unrestricted operational systems: **OPEN**.
- Extension to stochastic/information-generating/catalytic witnesses: **OPEN**.

## Reproducibility
`experiments/gc2_audit271_witness_cover_translator.py` exhaustively checks the union/degree bound on finite monotone DNF witness families and verifies exact disjoint-block sharpness cases.