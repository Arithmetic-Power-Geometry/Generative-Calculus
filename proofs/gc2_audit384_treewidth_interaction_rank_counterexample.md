# GC-II Audit 384: treewidth does not bound external interaction rank

Status: PROVED counterexample; generic mechanism IMPORTED/KNOWN; proposed shortcut FALSIFIED.

## Claim tested

Audit 383 requires a structural certificate controlling unobserved higher-order Mobius interactions. A natural candidate is bounded primitive locality plus bounded dependency/circuit treewidth.

This candidate fails.

## Theorem

For every n >= 2 there is a deterministic, monotone, acyclic, fan-in-2 mechanism whose undirected dependency graph has treewidth 1 but whose external capability function has interaction rank n.

Take a binary AND formula with inputs x1,...,xn. A chain is enough:

z2 = x1 AND x2
zk = z(k-1) AND xk, for 3 <= k <= n.

A balanced binary AND tree gives the same external map. The underlying formula graph is a tree, hence has treewidth 1.

Identify coalition S with xi=1 exactly when i is in S. Then

v(S) = 1 if S=N, and 0 otherwise.

For the Boolean-lattice Mobius transform,

m(N)=1 and m(T)=0 for every T != N.

Therefore interaction rank rho(v)=n.

Hence there is no system-size-independent function f such that rho(v) <= f(treewidth) for all such mechanisms: rank is unbounded already at treewidth 1.

## Residual magnitude

For any M>0, use output v_M(S)=M when S=N and 0 otherwise. Structure is unchanged while m_M(N)=M. Thus treewidth, even together with binary fan-in, monotonicity, determinism and acyclicity, cannot bound the magnitude of Audit 383's unseen residual E_q for q<n without an independent output normalization or gain condition.

## Stress checks

- n=2 already gives rank 2 at treewidth 1.
- Long depth is not responsible: a balanced binary tree has logarithmic depth and still yields rank n.
- No cycles, nondeterminism, cancellation, negative interaction coefficients, or stochasticity are used.
- Every primitive gate has fan-in 2.
- Reassociation of AND leaves the external result unchanged.
- Scaling M changes capability magnitude without changing graph structure.

## Composition lesson

Local binary maps can compose along a tree to create an external function whose unique multilinear pseudo-Boolean representation has an n-way term. Graph width can control important computational tasks without bounding algebraic interaction order of the represented input-output map.

## Prior-art boundary

The generic ingredients are known: pseudo-Boolean functions have unique multilinear representations; Boolean formulae are tree-like circuit structures; bounded treewidth is an established algorithmic structural parameter. None of these ingredients is claimed as GC novelty.

## Consequence

The implication

bounded primitive arity + bounded dependency width => bounded external interaction rank

is FALSIFIED.

Any GC-II certificate based only on local scope, dependency-cone topology, separators, treewidth, pathwidth, or related width summaries must survive this family before it can bound external Mobius rank or residual mass.

The surviving target is a composition-stable semantic quantity controlling interaction-order or interaction-mass amplification through composition, together with an independently normalized capability scale. It must be collision-tested against circuit/Fourier degree, influence and sensitivity, tensor/network ranks, communication complexity, CSP width, and graphical-model elimination.

## Ledger

- Binary locality -> bounded external interaction rank: FALSIFIED.
- Bounded treewidth -> bounded external interaction rank: FALSIFIED.
- Treewidth 1 can realize rank n for arbitrary n: PROVED.
- Adding monotonicity, determinism and acyclicity rescues the implication: FALSIFIED.
- Treewidth alone bounds unseen residual magnitude: FALSIFIED.
- Pseudo-Boolean representation and circuit-treewidth machinery: IMPORTED/KNOWN.
- GC-I-derived composition-stable semantic residual certificate: OPEN.
