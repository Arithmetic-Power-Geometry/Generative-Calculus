# GC-II Audit 290 — Worst-case operational distortion is a feasible-set cover

Status: PROVED (finite deterministic setting); IMPORTED/KNOWN at generic lossy/source-coding and set-cover level; graph shortcut FALSIFIED.

## Setup
Let `Y` be a finite attainable capability set, `A` a finite decoder/action set, and `ell:Y x A -> R_+` an operational loss. For tolerance `eps>=0`, define the feasible set of action `a`

`B_eps(a)={y in Y : ell(y,a)<=eps}`.

A deterministic account/decoder pair is `L:Y->S`, `g:S->A`, with worst-case operational fidelity when `ell(y,g(L(y)))<=eps` for every `y`.

Define

`N_eps(Y,A,ell)=min{|C| : C subseteq A and union_{a in C} B_eps(a)=Y}`.

## Theorem 290.1 — exact finite worst-case lossy accounting
The minimum possible number of account states among all deterministic worst-case-eps-faithful accounts is exactly

`N_eps(Y,A,ell)`.

Hence fixed-length binary memory needs exactly `ceil(log2 N_eps)` bits (up to unused binary codewords).

### Proof
Any faithful pair `(L,g)` uses the action set `C=g(L(Y))`. Every `y` lies in `B_eps(g(L(y)))`, so `C` covers `Y`; therefore `|L(Y)| >= |C| >= N_eps` after merging account states decoded to the same action. Conversely, choose a minimum cover `C`; assign each `y` to any covering action and encode that action. This uses `N_eps` states.

This reduces to Audit 289 at zero loss when decoder actions are exact decision signatures and `ell` is 0/1 disagreement.

## Proposition 290.2 — monotonicity and invariance
- If `eps' >= eps`, then `N_eps' <= N_eps`.
- Enlarging the decoder/action set cannot increase `N_eps`.
- Relabeling `Y`, `A`, or account states while preserving the loss table leaves `N_eps` invariant.
- `N_eps=1` iff one action is eps-feasible for all attainable states.
- For `Y` nonempty and no feasible action for some `y`, no faithful account exists; use `N_eps=infinity`.

## Decisive anti-shortcut: pairwise compatibility is insufficient
A tempting reduction is to form a graph joining two targets whenever some single decoder action can serve both, then infer that a clique can share one account state. This is false without a Helly/common-witness property.

Take `Y={1,2,3}` and three actions with zero-loss feasible sets

`B(a12)={1,2}`, `B(a23)={2,3}`, `B(a13)={1,3}`.

Every pair of targets is compatible, so the pairwise compatibility graph is complete. Nevertheless no single action serves all three targets, and the exact cover number is `N_0=2`.

Therefore pairwise compatibility/confusability graphs do not characterize general worst-case lossy operational accounting. The correct finite object is the action-feasibility hypergraph/set system. Graph coloring becomes exact only under additional structure that guarantees common witnesses.

## Composition
For product systems with additive/max loss, unrestricted joint decoder actions can create cross-system synergies, so multiplicativity is not claimed. If the action family and feasible sets factor exactly as Cartesian products and no coupled actions are allowed, product-cover upper bounds follow; equality requires additional assumptions and remains OPEN.

## Prior-art collision audit
The generic optimization is a finite covering formulation of deterministic worst-case lossy compression and is therefore not claimed as new. It collides directly with rate-distortion/task-oriented compression and minimum set cover. Recent task-oriented compression work explicitly optimizes rate under task distortion constraints. The GC-II value is architectural: it supplies the correct approximate continuation of Audit 289 and blocks an invalid graph-only simplification.

## Consequence for Omega_G
A non-tautological GC-II novelty/accounting bound cannot merely replace the exact quotient size by a pairwise incompatibility graph parameter. The operational lossy charge is controlled by a feasible-action cover number (or a probabilistic/rate-distortion analogue when distributions/randomized encoders are admitted). Connecting this quantity to independently measurable increments `Delta R, Delta I, Delta A, Delta L` remains OPEN.