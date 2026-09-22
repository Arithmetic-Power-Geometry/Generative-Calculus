# GC-II Audit 323 — Branchwise Class-Separation Persistence

## Purpose
Audit 322 showed that finite pairwise separators at the root do not imply a finite joint resolving policy when admissibility may disappear after an observation. Audit 323 asks for a branch-relative replacement for global/hereditary admissibility that is sufficient for quantitative joint resolution.

A first draft using only world-pair separation was rejected during proof audit: if a decision class contains multiple worlds, separating one representative from another does not force either whole class to disappear from every child. The corrected theorem below uses **class separation**, and records this failed proof route explicitly rather than hiding it.

## Finite operational model
Let `B` be a finite uncertainty cell. Each world `x in B` has required decision `g(x)`. An admissible test `u` at cell `C subseteq B` has nonnegative cost `c_C(u)` and finite deterministic outcome map `Z_u:C -> Y_u`. The child after outcome y is `C_{u,y}={x in C:Z_u(x)=y}`. A cell is resolved when g is constant. Let `k(C)=|g(C)|`.

The optimal worst-case resolving cost is

`V(C)=0` for resolved C, and otherwise

`V(C)=min_{u in Adm(C)} [c_C(u)+max_{y:C_{u,y} nonempty} V(C_{u,y})]`,

with `V(C)=+infinity` if no finite resolving policy exists.

## Branchwise class-separation persistence (BCSP)
Fix `P>=0`. For a decision label a represented in C, write `C_a={x in C:g(x)=a}`. BCSP(P) holds if, at every unresolved reachable cell C, there exist two represented decision labels a != b and an admissible test u such that

1. `Z_u(C_a) intersect Z_u(C_b) = emptyset`, and
2. `c_C(u)<=P`.

Thus no outcome child can retain representatives of both selected decision classes. BCSP is branch-relative: the separating test may be entirely different at every history; no nesting relation between admissible test catalogues is required.

A stronger all-class-pairs version may be useful as a certificate, but the theorem needs only **one** separable class pair at each unresolved reached cell.

## Theorem 323.1 — Dynamic class-separation bound
In a finite deterministic model with nonnegative costs, if BCSP(P) holds recursively on the cells reached by the construction, then

`V(C) <= (k(C)-1)P`.

Hence at a root with K decision classes,

`V(B) <= (K-1)P`.

### Proof
Induct on k(C). The case k=1 has V=0. For k>=2, BCSP supplies labels a,b and a test u of cost at most P whose outcome sets on C_a and C_b are disjoint. Consequently no child contains both classes a and b, so every nonempty child C_y has `k(C_y)<=k-1`. Apply the induction hypothesis on each unresolved child:

`V(C_y)<=(k(C_y)-1)P <= (k-2)P`.

Therefore

`V(C)<=c_C(u)+max_y V(C_y)<=P+(k-2)P=(k-1)P`.

QED.

## Theorem 323.2 — Tightness
The coefficient K-1 is sharp. For K singleton decision classes, use singleton membership tests of cost P, admissible whenever their queried class remains possible. BCSP(P) holds, while an adversary can return the nonsingleton outcome K-1 times. Thus `V=(K-1)P`.

## Strict weakening of hereditary admissibility
BCSP does not require hereditary admissibility. With three singleton classes {0,1,2}, allow only `root_is_0` at the root. On its unresolved {1,2} child, delete that root test and introduce the fresh test `branch_is_1`. No root catalogue persists, yet BCSP(1) holds on the reached unresolved cells and V=2.

Audit 322 instead has no admissible test on the unresolved two-class child, so BCSP fails exactly where deadlock appears.

## Rejected weaker candidate: representative-pair persistence
Candidate: at every unresolved cell, every incompatible world pair (or merely some incompatible world pair) has a cheap test giving those two worlds different outcomes.

**Status: FALSIFIED as a route to the K-class induction when classes may contain multiple worlds.** A test can separate chosen representatives x in C_a and x' in C_b while another representative of class a follows x' and another representative of class b follows x. A child may therefore retain both decision classes, and potentially all K classes. The inference `pair separated => k(child)<=K-1` is invalid without a class-level condition. For singleton decision classes the distinction disappears, which is why Audits 319–322 remain unaffected.

## What is and is not established
- **PROVED:** BCSP(P) implies `V <= (K-1)P`.
- **PROVED:** K-1 is tight under BCSP alone.
- **PROVED:** persistence of a fixed/hereditary action catalogue is stronger than necessary for this bound.
- **FALSIFIED:** root-only pairwise availability is sufficient (Audit 322).
- **FALSIFIED:** representative-pair separation alone justifies the K-class induction for nonsingleton classes.
- **NOT CLAIMED:** BCSP is necessary for finite resolution. A useful multiway test may reduce every child without cleanly separating two whole decision classes.
- **OPEN:** a strictly weaker progress statistic that is both easy to certify and yields a sharp quantitative bound under history-dependent resources/costs.

## Edge, domain, and invariance checks
K=1 gives V=0. P=0 gives V=0 under BCSP(0). Empty outcome cells are ignored. Multiple worlds per decision class are explicitly allowed. Costs may depend on the current cell/history; only the branchwise bound P is used. The theorem is invariant under relabeling worlds, decisions, tests, and outcomes. Scaling all costs by alpha>=0 scales P and V by alpha. No product/additivity assumption is made; arbitrary coupling constraints can destroy BCSP in a composite system.

## Prior-art collision note
Bellman recurrences, costed adaptive diagnosis, discrete-function evaluation, and constrained/precedence sequential testing are established neighboring theory. Audit 323 does not claim those mechanisms as new. Its role in GC-II is to identify a precise dynamic persistence certificate that repairs Audit 322 without requiring a fixed hereditary catalogue, while explicitly rejecting the tempting but invalid representative-pair proof for nonsingleton decision classes.

## Paper-II consequence
A Generative Novelty Gap or closure-escape account based on local witnesses must track whether useful distinctions remain executable **along the branches they create**. Root witness catalogues are insufficient. BCSP supplies one conservative, auditable certificate: `(K,P)` yields the sharp envelope `(K-1)P`. Models lacking BCSP require a richer progress measure rather than an unjustified pairwise reduction.
