# Audit 031 — Complete-monotone convertibility boundary

## Question
Can Paper II obtain a universal structured complete convertibility criterion merely by asserting a finite/computable/dual family of monotones for GC-II operational convertibility?

## Result
Not in this generality. Two distinct facts must be separated.

1. **Existence of some complete family is order-theoretic and therefore not a GC-II breakthrough.** Once admissible GC transformations induce a preorder `x >=_G y`, a complete family of monotones can be manufactured from the preorder itself. This is a representation of the order, not an independently informative computational theorem.
2. **A universal finite or computable complete family cannot be assumed.** General resource-theoretic convertibility problems can require infinite monotone families, and sufficiently expressive generated transformation theories can have undecidable membership/convertibility. Hence a finite/computable complete criterion needs explicit restrictions and a constructive proof.

Status: **IMPORTED/KNOWN boundary; FALSIFIED as a universal Paper-II route.**

## Elementary complete family on a finite quotient
Let `Q` be the quotient of a finite GC operational preorder by mutual convertibility. For every `z in Q`, define

\[
M_z(x)=\mathbf 1[z\preceq_G x].
\]

Each `M_z` is monotone: if `x >=_G y` and `z <=_G y`, transitivity gives `z <=_G x`, so `M_z(x)>=M_z(y)` under the chosen orientation.

Moreover,

\[
x\ge_G y \quad\Longleftrightarrow\quad M_z(x)\ge M_z(y)\ \text{for all }z\in Q.
\]

For the reverse implication choose `z=y`; then `M_y(y)=1`, so the inequalities force `M_y(x)=1`, hence `x>=_G y`.

Thus every finite quotient has a finite complete family of at most `|Q|` Boolean monotones. This construction is exact but tautological: evaluating `M_z` already asks an order-membership question.

## Why this does not solve GC-II
A useful Paper-II criterion must improve on direct reachability/convertibility. At minimum it should provide one or more of:

- a family whose members are computable substantially more cheaply than exhaustive closure;
- a polynomial-size family under explicit structural hypotheses;
- a dual certificate with independently checkable witnesses;
- a closed-form criterion tied to task-scale-error-budget geometry;
- a parameterized criterion whose complexity is bounded by a declared GC structural parameter.

Without such a surplus, `complete monotones exist` simply repackages the preorder.

## Universal finite/computable claim fails
The unrestricted GC-II program allows arbitrary admissible transformations/rules and therefore can encode transition systems whose reachability or generated-operation membership is not uniformly decidable. If a uniformly computable complete monotone family with a terminating decision procedure existed for every such system, it would decide the encoded convertibility problem, contradicting undecidable instances.

This is a boundary statement, not a new undecidability theorem: the mechanism is inherited from computation/resource-theory membership problems.

Likewise, finiteness cannot be promoted universally merely because finite examples admit the construction above. Infinite/continuous resource theories can require infinite complete families; a finite family is an additional theorem requiring topology/algebra/geometry assumptions.

## Degenerate and edge cases
- Finite explicitly enumerated world: finite complete Boolean family exists; useful only if it compresses or accelerates the explicit order.
- Total preorder: a single scalar representation may exist under additional representability conditions; this is not generic.
- Infinite but decidable world: undecidability obstruction disappears, but finite completeness still does not follow.
- Oracle monotones: can trivially encode convertibility and are excluded from any computational novelty claim.
- Discontinuous/nonconstructive monotones: may restore mathematical completeness while offering no algorithmic criterion.
- Approximate conversion: exact indicator monotones need not give a stable quantitative theory; topology/error tolerance must be declared.
- Catalysis/composition: monotones complete for single-copy direct conversion need not automatically be complete for catalytic/asymptotic conversion unless those operations are included in the preorder being represented.

## Consequence for Omega_G and Closure-Escape
A separating monotone can certify closure escape:

\[
M(Y)>M(X) \Rightarrow X\not\Rightarrow_G Y
\]

for the appropriate orientation. But defining `M` from the already-computed closure is circular. Therefore a non-tautological Closure-Escape theorem must produce a separator from primitive operational data (resources, information, interfaces/actions, rules, task-scale-error-budget constraints) without first solving the full closure problem.

This gives a sharper Paper-II target:

> Identify a restricted but scientifically meaningful GC class for which a small, independently computable family of whole-envelope monotones is both sound and complete, and prove that completeness from primitive structure rather than from the precomputed convertibility relation.

A stronger candidate would additionally yield a quantitative separation margin connected to `Omega_G`, not just a yes/no order witness.

## Prior-art collision classification
- Complete monotone families for abstract resource preorders: **IMPORTED/KNOWN**.
- Finite Boolean principal-ideal construction above: **elementary order theory / IMPORTED-KNOWN mechanism**.
- Universal finite/computable complete GC-II family: **FALSIFIED without restrictions**.
- Restricted GC-essential efficiently computable complete family: **OPEN**.
- Dual monotones with a quantitative `Omega_G` separation margin derived from primitive GC structure: **OPEN**.

## Next attack
1. Define a finite primitive GC class with explicit vector budgets and task-scale-error feasibility but without arbitrary oracle rules.
2. Compute exact convertibility by exhaustive enumeration as ground truth.
3. Generate candidate primitive monotones from support functions / taskwise deficits / budget gauges rather than from the closure matrix.
4. Collision-test completeness exhaustively on all small worlds.
5. If collisions occur, catalog the minimal missing joint structure; if none occur, attempt a proof and then compare directly with Blackwell/Le Cam, majorization, simulation preorders, LP/Farkas duality, energy games, and general resource-theory monotones.
6. Promote only if the resulting criterion is smaller or independently computable and its proof uses an essential GC whole-envelope coupling.