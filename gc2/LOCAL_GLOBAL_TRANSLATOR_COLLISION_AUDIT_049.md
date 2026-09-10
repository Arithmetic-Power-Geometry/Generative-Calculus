# GC-II Audit 049 — Proper-Local-to-Global Translator Collision

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 048

## Question

Does strengthening GC-I proper-projection irreducibility into a growing operational local-to-global translator cost yield a GC-II breakthrough?

## Exact family

Let x=(x_1,...,x_n) in {0,1}^n and define the conserved global obligation

P_n(x)=x_1 xor ... xor x_n.

The declared local interface exposes individual coordinates through queries q_i(x)=x_i. A deterministic translator may adaptively query these local interfaces and must output P_n(x) exactly.

### Theorem 049.1 — exact local-query translator lower bound

Every exact deterministic translator for P_n using only coordinate-local interfaces has worst-case query cost at least n. The bound is tight.

Proof. Suppose a deterministic translator halts on some computation path after querying fewer than n coordinates. Then at least one coordinate j is unqueried. Choose any input x consistent with all answers on that path and let x' differ only in coordinate j. The transcript is identical on x and x', so the translator returns the same output. But P_n(x')=1-P_n(x), contradiction. Querying all n coordinates and XORing them attains cost n. Therefore Lambda_n=n under this interface/cost model. QED.

Status: **PROVED**.

## Proper-local indistinguishability witness

Let E_n be the uniform distribution on even-parity strings and O_n the uniform distribution on odd-parity strings. For every proper coordinate subset J subsetneq [n], the marginal distributions of E_n and O_n on J are both uniform on {0,1}^{|J|}. Thus every proper coordinate projection agrees, while the global parity obligation separates the two distributions perfectly.

Proof. Fix a proper J and assignment a on J. At least one coordinate remains free. Exactly half of completions have even parity and half odd parity, giving 2^{n-|J|-1} completions in each parity class. Since each parity class has 2^{n-1} strings, both projected probabilities equal 2^{-|J|}. QED.

Status: **PROVED**.

## Critical collision

The lower bound Lambda_n=n is not a new GC-II law. It is exactly ordinary deterministic decision-tree/query complexity of parity under coordinate queries. The proper-local/global separation is likewise an affine/parity phenomenon: parity is a linear functional over GF(2), and changing the allowed interface changes the complexity drastically. If the translator is permitted one global parity query, the same obligation costs one query. Hence the lower bound is interface-relative, not an intrinsic capability invariant.

The same family also collides with communication complexity when coordinates are distributed among parties, with circuit complexity when the translator is represented as a circuit, with affine CSP/coding descriptions when parity is represented as a linear constraint, and with marginal problems through the even/odd distributions having identical proper marginals.

Status: **PROVED reduction for the coordinate-query model; IMPORTED/KNOWN mechanism; standalone GC-II novelty route FALSIFIED**.

## Why superconstant growth does not rescue novelty

A growing translator burden was the additional ingredient missing from GC-I projection irreducibility. This audit supplies the strongest elementary witness: all proper marginals match and the exact local translator cost grows linearly. Nevertheless the cost is completely explained by the chosen computational interface. Therefore the conjunction

1. all proper local projections match,
2. global behavior differs, and
3. local-to-global translator cost diverges

is still insufficient for GC-II novelty.

In particular, defining Omega_G from Lambda_n without quotienting over admissible interface changes would re-label standard complexity lower bounds as generative novelty.

## Dimension/domain checks

- Lambda_n counts coordinate queries and is dimensionless until a physical/resource cost per query is declared.
- With heterogeneous query costs c_i >= 0, the same adversary argument forces every coordinate to be queried in the worst case, so the exact cost is sum_i c_i for a nonadaptive additive accounting; zero-cost coordinates create the expected degeneracy.
- For n=1 the result gives Lambda_1=1; there is no nonempty proper coordinate information sufficient to determine the bit.
- Approximate/randomized translators require a separately declared error model and distribution; the exact theorem above does not silently extend to them.
- If global XOR is an admissible primitive interface, Lambda_n collapses to one primitive query. This is the decisive interface-dependence check.
- Independent product composition can add coordinate-query burdens under the declared direct-sum interface, but this is again ordinary query/direct-sum structure rather than a GC-specific law.

## Consequence for Omega_G

No candidate that treats a local-to-global complexity lower bound under one fixed representation/interface as intrinsically generative can pass the collision test. A defensible Omega_G must distinguish ordinary cost of computing a fixed extensional obligation from a change in the operational possibility structure itself.

## Stronger surviving target

The next target must compare **interface families together with the cost of constructing/refining interfaces**, rather than freezing one interface and measuring a familiar function complexity. A possible object, with no novelty claimed, is an interface-relative Pareto envelope

E_S(q) = ParetoMin { (construction cost, observation cost, action cost, rule cost) : an admissible interface/translator pair realizes conserved obligation q }.

But Audits 041–046 already warn that installation cost, amortization, feasible-set expansion and value surfaces separately reduce to known theories. Therefore the next severe test is not to scalarize E_S. It is to ask whether there exists a representation-safe obstruction to simultaneously compressing **interface construction and downstream translation** across an entire obligation family, after quotienting semantics-preserving compilers.

Candidate research question:

Can one construct S_n,T_n with identical extensional obligation maps and matched costs for every individual obligation, yet prove that any *single reusable interface* supporting the whole obligation family incurs a superconstant joint overhead that cannot be removed by semantics-preserving compilation?

This is immediately collision-prone with data structures, preprocessing/advice, universal coding, circuit families, sufficient statistics, communication complexity, and multi-query/direct-sum complexity. It must be rejected if those theories completely account for the witness.

Status: **OPEN**.

## Final classification

- Proper-local even/odd parity indistinguishability: **PROVED / classical affine mechanism**.
- Exact coordinate-local translator lower bound Lambda_n=n: **PROVED / deterministic query complexity**.
- Diverging Lambda_n as standalone GC-II novelty: **FALSIFIED**.
- Interface dependence of Lambda_n: **PROVED**.
- Reusable whole-family interface obstruction after compiler quotienting: **OPEN; next target**.
