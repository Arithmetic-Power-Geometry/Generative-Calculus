# GC-II Audit 105 — Action-Creation Monotone Collision

## Scope
Branch-only Paper-II audit. GC-I on `main` remains frozen. Inspected parent: `cbcc98a1fdf56f8c9809a382dce1d03cc3a9f732` (Audit 104).

## Target inherited from Audit 104
Test the surviving route: a boundary-flux theorem for creation of new admissible actions/transformations, with an independently measurable incoming witness that is not merely Blackwell information, divergence contraction, majorization, thermodynamic accounting, or generic resource-theory bookkeeping.

## Result
**DECISIVE FALSIFICATION of the generic action-creation-monotone route.** If the proposed incoming witness is defined only by (i) a class of free transformations and (ii) monotonicity under those transformations, then the resulting No-Free-Capability theorem is already an abstract resource theory. Calling the resource “action capacity”, “admissibility flux”, or “capability potential” does not escape this equivalence.

### Definition — operational object and action capability
Let an operational object be

\[
X=(S,\mathcal A,T,O,c,\varepsilon),
\]

where `S` is state, `A(s)` is the admissible action/interface set, `T` is transition structure, `O` observables/tasks, `c` typed resource accounting, and `epsilon` error structure. Let `Cap(X)` denote any declared extensional capability object (reachable task set, action relation, budgeted closure, or another explicitly specified operational image).

Let `F` be a class of transformations declared free.

### Theorem 1 — Generic action-creation monotone is a resource monotone (PROVED)
Suppose a scalar or vector witness `W` satisfies

\[
W(\Phi[X])\preceq W(X) \qquad \forall\Phi\in\mathsf F,
\]

for a preorder `preceq`, and suppose a claimed capability-creation event requires

\[
W(Y)\succ W(X).
\]

Then no free transformation can realize `X -> Y`.

**Proof.** If `Y=Phi[X]` for some free `Phi`, monotonicity gives `W(Y) preceq W(X)`, contradicting `W(Y) succ W(X)`. QED.

This theorem is mathematically valid but is exactly the generic resource-theory monotone argument. It cannot be the GC-II breakthrough without additional independently derived structure.

### Corollary 1 — Renaming the resource does not create novelty (PROVED)
Any witness such as

\[
W_A(X)=|\mathcal A_X|,\quad
W_{\rm img}(X)=\log |\operatorname{Im}(Cap(X))|,
\]

or a robustness/distance/entropy assigned to the action or capability object remains an ordinary resource monotone whenever the chosen free operations are precisely those that cannot increase it.

If the free class is *defined* by `W(Phi[X]) <= W(X)`, the No-Free theorem is additionally circular: the conclusion is built into the definition of freeness.

### Theorem 2 — Boundary-flux accounting needs an independent conservation law (PROVED as a logical requirement)
A non-tautological inequality of the form

\[
\Delta W_{\rm capability}\le J_{\partial}+G(\Delta R,\Delta I,\Delta A,\Delta L)
\]

cannot be inferred from action-set enlargement alone. To have explanatory content, at least one of the following must be supplied independently of the desired inequality:

1. a physical/dynamical law fixing `J_boundary`;
2. an independently fixed machine/interaction model from which the right-hand side is derived;
3. a conserved or contractive quantity proved from microscopic dynamics;
4. an operational duality showing that the witness equals an independently measurable task advantage.

Otherwise define the residual

\[
J_{\partial}:=\max\{0,\Delta W_{\rm capability}-G\},
\]

and the proposed law becomes true by construction. Such a definition is tautological and is rejected for Paper II.

### Corollary 2 — Pure action cardinality is especially weak (PROVED)
Action-set cardinality is representation-dependent. A single parameterized action can encode many named actions, while one named action can be split into many aliases without changing operational closure. Therefore `|A|` is not invariant under semantics-preserving interface refactorings. Any valid GC witness must quotient such presentation changes or be defined directly on operational equivalence classes.

### Edge/counterexample audit
- **Action aliases:** arbitrarily increase `|A|` at zero semantic capability gain.
- **Macro action:** arbitrarily decrease the number of named actions while preserving finite-horizon behavior when macro expansion is free.
- **Hidden parameterization:** one syntactic action may expose an arbitrarily large operational image.
- **Free catalyst:** if a catalyst changes reachable actions while being returned intact, the resource object must include the catalyst; omission produces false creation.
- **Composition:** ordinary resource monotones may be additive, subadditive, superadditive, or merely monotone; nonadditivity alone does not escape resource theory.
- **Typed costs:** attaching `(R,I,A,L)` to the transformation does not alter Theorem 1. A new result requires a derived coupling, not coordinate naming.
- **Stochastic operations:** replace deterministic maps by kernels/channels; the monotonicity argument is unchanged.
- **Open-world inputs:** genuinely exogenous additions can enlarge capability, but then the added object/input is an incoming resource unless a stronger physical law says otherwise.

## Prior-art collision
This candidate collides at the framework level with resource theories: free states/objects, free operations, convertibility, and monotones are precisely the standard machinery for proving that a resource cannot be generated by free processing. Dynamic/channel resource theories extend the same idea to transformations themselves and admit complete operational monotone families in important closed/convex settings.

It also collides with viability/control theory when “capability” is merely the set of admissible controls or viable/reachable states under state-dependent control constraints. Therefore action availability, constrained reachability, and monotonicity under a declared free class cannot by themselves establish GC-II novelty.

## Consequence for Paper II
The surviving route must be stronger than “new actions require resource.” The next valid target is:

**Independent boundary-balance problem (OPEN).** Fix a realization boundary and microscopic/operational dynamics independently; identify a quotient-invariant capability witness `W`; then derive, rather than define, a balance/inequality linking change in `W` to measurable boundary exchanges. The theorem must survive reduction to abstract resource monotones, Blackwell/deficiency, viability/reachability, thermodynamic monotones, communication/query/circuit lower bounds, and representation refactorings.

A breakthrough candidate would need a concrete finite model in which the independently derived balance predicts a nontrivial forbidden/required capability transition that is not already implied by those theories, followed by exhaustive counterexample search and prior-art collision checks.

## Status
| Claim | Status |
|---|---|
| Generic free-operation monotonicity implies No-Free-Capability | PROVED |
| Generic action/capability witness under free transformations | IMPORTED/KNOWN resource-theory mechanism |
| Free class defined by nonincrease of the desired witness | FALSIFIED as non-tautological theorem source |
| Raw action-set cardinality as invariant capability witness | FALSIFIED |
| Nonlinear/nonadditive typed weighting alone escapes resource theory | FALSIFIED |
| Independently derived boundary-balance law | OPEN |
| GC-II positive breakthrough | OPEN / NOT ESTABLISHED |

No numerical experiment is claimed in this audit; the generic candidate is settled analytically.