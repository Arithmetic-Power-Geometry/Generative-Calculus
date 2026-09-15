# GC-II Audit 163 — Uniform finite-interface insufficiency: exact bound and novelty boundary

## Gate inherited from Audit 162
Test whether GC-I proper-projection irreducibility yields a genuinely new operational theorem: across growing finite worlds, a controller restricted to a fixed interface class must eventually fail unless interface complexity grows.

## Model
Let `X_n` be a finite world family. A local projection `pi_n:X_n -> Y_n` exposes a local view. A controller additionally receives an interface symbol `c(x)` from an alphabet `C_n` and has internal memory state `q in Q_n`. For a one-shot exact target, let `a*(x)` be the required action. More generally, define two worlds in the same projection fiber to be **action-incompatible** when no single admissible controller output can satisfy the target on both.

For a fiber `F_y = pi_n^{-1}(y)`, let `K_y` be the maximum cardinality of a pairwise action-incompatible subset of `F_y`, and `K_n=max_y K_y`.

The controller's decision-relevant augmented interface state is `(c,q) in C_n x Q_n`.

## Uniform finite-interface theorem — PROVED
Any deterministic exact controller must satisfy

`|C_n| |Q_n| >= K_n`.

Equivalently,

`log2 |C_n| + log2 |Q_n| >= log2 K_n`.

For fixed-length binary encodings this gives

`b_C + b_Q >= ceil(log2 K_n)`

up to the usual distinction between ideal logarithmic information and integer code length.

### Proof
Fix a projection fiber and a pairwise action-incompatible subset `S` of size `K_n`. If two worlds `x,x' in S` induce the same augmented interface state `(c,q)`, a deterministic controller must choose the same output on both. By action incompatibility, that output cannot satisfy the target on both, contradicting exactness. Thus the map from `S` to `C_n x Q_n` must be injective. Hence `K_n <= |C_n||Q_n|`. QED.

## Tight family — PROVED
Take `X_n=[p]^n`, retain `k` coordinates, and require the controller to output the omitted `(n-k)`-tuple exactly. Every projection fiber has `p^(n-k)` pairwise action-incompatible worlds, so

`K_n=p^(n-k)`

and

`log2 |C_n| + log2 |Q_n| >= (n-k) log2 p`.

The ideal bound is tight: encode the omitted tuple itself (or its fiber index) and use one memory state.

Therefore any interface/memory class with fixed finite product capacity `B=|C||Q|` fails for all sufficiently large `n-k` once `p^(n-k)>B`.

## Edge and composition checks
- `k=n`: `K_n=1`; zero auxiliary information is sufficient.
- `k=0`: exact reconstruction/action selection needs capacity at least `p^n`.
- `p=1`: degenerate singleton world; bound is zero bits.
- Memory/interface tradeoff: only the product capacity is forced in this one-shot model; attributing the burden uniquely to interface or memory is unjustified.
- Non-injective required actions: replace fiber cardinality by `K_y`; the raw fiber-size bound would otherwise overclaim.
- Randomization: zero-error randomization cannot merge action-incompatible worlds if every random outcome must be correct; bounded-error variants require different information/communication arguments.
- Sequential systems: histories may enlarge the effective observation alphabet; the theorem applies to the complete decision-relevant transcript/state, and stronger sequential lower bounds require an explicit protocol model.
- Parallel independent fibers: incompatibility numbers multiply when the target requires independent exact outputs, so ideal logarithmic capacity lower bounds add.

## Exact finite regression
`experiments/gc2_audit163_uniform_interface.py` exhaustively checks the projection family for `p in {2,3}`, `1<=n<=6`, every `0<=k<=n`, verifies fiber cardinality `p^(n-k)`, and checks the fixed-capacity failure threshold for capacities `1,2,4,8,16`. No empirical result is claimed here until the script is independently executed by CI or a local runner.

## Prior-art collision — DECISIVE
The theorem is a pigeonhole/information-capacity lower bound. Communication complexity already lower-bounds information exchange needed to distinguish inputs and solve global functions, and communication arguments are routinely used to prove representation/automata/streaming lower bounds. Finite-state controllers in partially observable systems explicitly trade finite controller memory against observation histories. Distributed synthesis likewise studies realizability under architectural/information constraints.

Hence **uniform finite-interface insufficiency is mathematically valid but not independently novel in this raw form**. GC-I projection irreducibility supplies a clean family of hard fibers, but converting fiber multiplicity into `log K` auxiliary capacity is a standard information/communication mechanism.

## Ledger
- Uniform finite-interface product-capacity bound: **PROVED**.
- Tight projection family: **PROVED**.
- Fixed finite interface/memory eventually fails on growing proper-projection fibers: **PROVED**.
- Raw `log K_n` burden as a new `Omega_G`: **FALSIFIED as independent novelty**.
- Counting/communication/information mechanism: **IMPORTED/KNOWN**.
- Sequential bounded-error and interactive refinements: **OPEN here**, but strongly collision-prone with communication/control literature.
- GC-II-specific capability-accounting residual not reducible to protocol capacity: **OPEN**.

## Consequence for Paper II
Audits 153–163 now rule out a broad family of proposed novelty mechanisms: path cost, model edits, reflective state, endogenous tasks, compiler size without target restrictions, semantic conversion distance, information/action separation, nonlinear path coupling, and fixed-interface counting all reduce to established operational/information frameworks under their natural assumptions.

A credible next gate should not merely add a richer interface bound. It should search for a theorem linking **multiple operational budgets to capability creation in a way that is invariant under sufficient-state recoding yet is not determined by the induced reachability/conversion preorder or by protocol transcript complexity**. If no such invariant survives exact finite counterexample search, the scientifically stronger Paper-II outcome may be a no-go/representation theorem delimiting what any capability-accounting calculus can identify from operational behavior.