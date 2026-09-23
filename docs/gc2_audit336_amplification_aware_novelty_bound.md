# GC-II Audit 336 — Amplification-aware novelty bound after the four-coordinate no-go

## Purpose

Audit 335 falsified any finite dimension-independent bound on raw newly reachable ordered pairs that depends only on schema-level `(Delta R, Delta I, Delta A, Delta L)`: one reusable successor rule can be applied repeatedly and generates quadratically many reachability pairs as the state domain grows.

This audit asks for the weakest explicit structural coordinate that repairs that failure without pretending that a rule schema and all of its grounded/composed consequences are the same object.

## Setup

Let `X` be a finite set of operational states and let `<=_0` be the baseline reachability preorder. Work on any chosen finite quotient `Q` of operational states for which baseline reachability and the newly admitted transformations are well-defined. Write `q=|Q|`.

A **new macro-step** is: any amount of baseline motion, followed by exactly one newly admitted transformation, followed by any amount of baseline motion. This definition deliberately absorbs free/baseline repositioning into the step, so the theorem does not accidentally ignore amplification supplied by the old system.

For `x in Q`, let

`N(x) = { y in Q : y can be reached from x by one new macro-step }`.

Define the **operational branching/amplification coordinate**

`beta = max_x |N(x)|`.

For an ordered pair `(x,y)` that is newly reachable after the extension, define its **new-action depth** as the minimum number of new macro-steps in a witnessing path. Fix a depth horizon `h` and let `Omega_pair^(h)` be the number of ordered pairs that were not baseline-reachable but become reachable with new-action depth at most `h`.

The quantities are dimensionless counts. `beta` counts distinct operational successor classes, not syntax-level schemas, and is therefore insensitive to duplicating a rule name without changing its operational successor relation.

## Theorem 336.1 — finite-horizon amplification bound

For every finite system above,

`Omega_pair^(h) <= q * min(q-1, sum_{ell=1}^h beta^ell)`.

For `beta=0` the sum is zero. For `beta=1` it is `h`. For `beta>1`,

`sum_{ell=1}^h beta^ell = beta (beta^h - 1)/(beta-1)`.

### Proof

Fix a start class `x`. Every target newly reachable with minimum new-action depth at most `h` has a witness consisting of `ell` macro-steps for some `1 <= ell <= h`. At each macro-step there are at most `beta` distinct successor classes by definition. Therefore the number of endpoint classes represented by all such words is at most

`sum_{ell=1}^h beta^ell`.

Independently, there are at most `q-1` targets different from `x`; counting baseline-novel pairs can only reduce this number. Hence the number of novel targets from `x` is at most

`min(q-1, sum beta^ell)`.

Summing over the `q` possible starts proves the claim. Collisions between words, cycles, baseline-reachable endpoints, and repeated endpoints only decrease the count. QED.

## Corollary 336.2 — no-free-capability form

If `Omega_pair^(h) > 0`, then necessarily `q>1`, `h>=1`, and `beta>=1`. More quantitatively, for fixed `(q,h)` the raw finite-horizon novelty is controlled by operational successor amplification rather than by schema count alone.

This is intentionally modest: it is a counting theorem, not a thermodynamic or information-theoretic conservation law.

## Corollary 336.3 — Audit 335 is explained, not contradicted

For the Audit-335 successor family `X_n={0,...,n}` with identity baseline and the reusable rule `i -> i+1`, we have

- `q=n+1`,
- `beta=1`,
- maximum required new-action depth `h=n`.

The theorem gives

`Omega_pair <= (n+1) min(n,n) = n(n+1)`,

while the exact novelty is `n(n+1)/2`.

Thus the missing amplification was not branching but reusable **depth/domain opportunity**. A constant schema count does not imply constant operational depth.

## Why beta must be defined after baseline closure

A tempting alternative is to count only the number of syntactically new actions applicable at a state. That is unsafe when baseline motion can freely reposition the system before a new action. The macro-step definition explicitly closes around baseline reachability, so `beta` measures distinct operational consequences available per charged/new step.

## Edge and degeneracy checks

- `h=0`: no new macro-step is permitted, so novelty is zero.
- `beta=0`: no new macro-step has an operational successor, so novelty is zero.
- `q=1`: no distinct ordered pair exists.
- cycles: do not break the bound; repeated words/endpoints only reduce distinct targets.
- nondeterministic new actions: allowed, because `N(x)` counts distinct successor classes rather than action labels.
- duplicated rule syntax: does not change `N(x)` and therefore does not change `beta`.
- relabeling of quotient states: leaves `q`, `beta`, `h`, and the bound invariant.
- serial composition: increasing the admitted depth horizon can increase the bound geometrically when `beta>1` and linearly when `beta=1`.

## Tightness and limitations

The word-count part is attained locally by a rooted `beta`-ary tree before the finite-state cap becomes active. The global `q` factor need not be simultaneously tight for every finite transition geometry because trees rooted at different starts can share states. The theorem is therefore a universal upper bound, not a claim of universal equality.

The theorem does **not** yet give a universal `Omega_G <= F(Delta R,Delta I,Delta A,Delta L)` using only the original four coordinates. Audit 335 proved that impossible under schema-level accounting. Audit 336 instead identifies explicit amplification variables `(q,beta,h)` that make a finite raw-pair bound possible:

`Omega_pair^(h) <= F_amp(q,beta,h) = q min(q-1, sum beta^ell)`.

A future GC-II bound can couple resource/information/interface/rule changes to constraints on `beta` and `h`; without such a bridge, inserting the original four deltas into this theorem would be cosmetic rather than proved.

## Prior-art boundary

The counting mechanism is classical. Words over finite generators, balls in Cayley/transition graphs, bounded-depth reachability, and exponential growth with branching are established mathematics/computer science. This audit does **not** claim novelty for geometric-series path counting. Its GC-II role is narrower: it isolates the exact structural variable omitted by the falsified four-coordinate raw-gap proposal and provides a representation-resistant operational repair target.

## Status

- Finite-horizon amplification bound: **PROVED**.
- Need for an amplification/opportunity coordinate after Audit 335: **PROVED for raw pair-count novelty under schema-level accounting**.
- Generic path/word-growth mechanism: **IMPORTED/KNOWN**.
- Original four-coordinate dimension-independent raw-pair bound: **FALSIFIED (Audit 335)**.
- Universal bridge from `(Delta R,Delta I,Delta A,Delta L)` to `(q,beta,h)`: **OPEN**.
- Representation-stable normalized or task-weighted `Omega_G` beyond pair counts: **OPEN**.
