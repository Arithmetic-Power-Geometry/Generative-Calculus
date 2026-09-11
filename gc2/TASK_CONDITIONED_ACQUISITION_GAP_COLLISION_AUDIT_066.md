# GC-II Audit 066 — Task-Conditioned Physical Acquisition Gap Collision

## Scope
This audit attacks the surviving candidate from Audit 065: whether a task-conditioned minimum typed physical augmentation needed to acquire missing information and thereby enable a task can itself define a novel GC-II invariant.

## Status summary
- Task-conditioned acquisition frontier: **PROVED well-defined** for finite explicit acquisition models.
- Zero-gap and monotonicity properties: **PROVED**.
- Reduction to finite decision/experiment optimization: **PROVED**.
- Generic novelty of this frontier: **FALSIFIED**.
- Stronger path-dependent acquisition/installation candidate: **OPEN**.

## 1. Operational model
Let a finite world have latent state \(\theta\in\Theta\), prior information state \(h\), task \(q\), admissible acquisition interventions \(e\in E\), observations \(y\in Y_e\), and post-observation actions \(a\in A\). An acquisition policy \(\pi\) may adaptively choose experiments from prior observations. Each realized acquisition history \(\gamma\) carries a typed nonnegative physical cost

\[
c(\gamma)=(R(\gamma),I(\gamma),A(\gamma),L(\gamma))\in\mathbb R_{\ge0}^4.
\]

Let \(\operatorname{Succ}_q(\pi;h)\) denote task success (or expected loss at most \(\epsilon\)). Define

\[
\Omega_{\rm acq}(q,\epsilon\mid h)
=\operatorname{Min}_{\rm Pareto}
\{c(\gamma):\exists\pi\text{ using }\gamma,\;\operatorname{Err}_q(\pi;h)\le\epsilon\}.
\]

No scalar addition of heterogeneous coordinates is assumed.

## 2. Elementary properties
### Proposition 066.1 — zero gap
If the task is already achievable from \(h\) at error \(\epsilon\) with no acquisition, then \((0,0,0,0)\) belongs to the frontier and dominates every positive augmentation.

**Status: PROVED.** Immediate from feasibility of the null policy.

### Proposition 066.2 — task relaxation monotonicity
For \(\epsilon'\ge\epsilon\), the feasible policy set for \(\epsilon'\) contains that for \(\epsilon\). Hence the relaxed frontier cannot require a coordinatewise larger minimum augmentation.

**Status: PROVED.** Set inclusion; no convexity or additivity required.

### Proposition 066.3 — free side-information monotonicity
If \(h'\) Blackwell-dominates \(h\) for the relevant finite experiment model and is supplied at zero charged boundary cost, any policy feasible from \(h\) can be simulated from \(h'\) by garbling/ignoring excess information. Thus acquisition requirements cannot increase.

**Status: IMPORTED/KNOWN mechanism + direct reduction.** This is the standard comparison-of-experiments architecture, not a GC-specific law.

## 3. Finite acquisition-collapse theorem
### Theorem 066.4 — finite task-conditioned acquisition collapse
For any finite explicit GC acquisition system with finite horizon, finite experiment/action alphabets, explicit observation kernels, explicit task loss, and explicit typed transition/acquisition costs, \(\Omega_{\rm acq}\) is exactly the Pareto image of a finite contingent decision/experiment optimization problem.

**Proof.** Expand every adaptive acquisition policy into a finite decision tree. A node records the complete observable history; outgoing experiment choices and observation outcomes define the next nodes. Leaves choose task actions. The original GC execution and this decision tree have identical conditional observation laws, identical task loss, and identical typed costs on every history. Conversely every such decision tree is an admissible acquisition policy. Therefore feasible cost vectors coincide exactly, and Pareto minimization preserves equality. QED.

**Status: PROVED.**

This theorem survives nonlinear costs: history-dependent interaction costs can be attached directly to nodes/edges or complete histories. It also survives adaptive experiment choice and nonadditive physical cost vectors.

## 4. Prior-art collision
The generic candidate overlaps established structures rather than escaping them:

1. **Value of sample information / value of information:** task utility improvement from additional observations is already a decision-theoretic object.
2. **Blackwell comparison:** finite experiments are ordered by whether one can simulate/garble another and by performance across decision problems.
3. **Bayesian optimal experimental design:** acquisition policies choose experiments to optimize expected utility/information under costs; expected information gain is a standard objective.
4. **Active/exact learning and query complexity:** minimum queries/observations required to identify a task-relevant target already admit combinatorial lower bounds.
5. **Finite constrained POMDP/MDP formulation:** once acquisition history, costs and belief/information state are explicit, task-conditioned sensing is ordinary contingent planning on the enlarged state.

Therefore the statement

\[
\text{“capability requires acquiring missing task-relevant information at positive typed cost”}
\]

is physically meaningful but not, by itself, a new theoretical phenomenon.

## 5. Important no-go: information amount does not determine acquisition frontier
No universal function

\[
\Omega_{\rm acq}=F(H(\Theta\mid h))
\]

or even \(F(I(\Theta;Y))\) exists without task, experiment family, loss, and physical implementation.

Counterexample schema: two one-bit latent variables may have equal entropy, while one is directly observable by a unit-cost sensor and the other is not observable under the allowed interface. Their information amounts match but their physical acquisition frontiers differ. Likewise an experiment can have high expected information gain about nuisance variables yet zero value for the task.

**Status: PROVED by construction.**

This blocks an invalid shortcut from information-theoretic quantity directly to typed physical capability cost.

## 6. Novelty verdict
**FALSIFIED:** the generic task-conditioned physical acquisition gap is not sufficient as \(\Omega_G\)'s breakthrough source for finite explicit models. It is a useful GC accounting layer, but it compiles to established decision/experiment/acquisition optimization.

## 7. Surviving target
The next candidate must not be merely “which observation should be purchased?” It must couple acquisition to an irreversible or persistent change in the future admissible operational closure in a way that cannot be removed by state augmentation.

A possible object is a **path-dependent acquisition-to-capability hysteresis**:

\[
\mathcal H_G(q;\gamma_1,\gamma_2)
= d\!\left(\mathcal C_G^{\rm future}(h_{\gamma_1}),
             \mathcal C_G^{\rm future}(h_{\gamma_2})\right),
\]

where \(\gamma_1,\gamma_2\) finish with observationally equivalent task beliefs and equal charged endpoint budgets but may have installed different persistent physical structures during acquisition.

Immediate kill test: if the installed structure can be included in the ordinary state, Audit 064 collapses it. Thus a breakthrough requires a representation-independent operational quotient plus a lower bound on future capability that is invariant under state re-encoding. This is **OPEN**, not claimed as novel or proved.

## 8. Required next collision checks
Before promoting the hysteresis direction, test against:
- POMDP sufficient statistics and belief-state augmentation;
- adaptive submodularity and active learning;
- irreversible computation / thermodynamic memory;
- causal interventions and experiment design;
- learning with stateful environments;
- self-modifying agents and metareasoning;
- resource-theoretic catalysts and memory channels;
- non-Markovian process tensors / combs;
- automata minimization and bisimulation quotients.

## Audit conclusion
Audit 066 narrows GC-II again: acquisition is not generative novelty merely because it is task-conditioned, adaptive, physical, typed, or nonadditive. In finite explicit settings it is exactly contingent decision/experiment optimization. The surviving scientific question is whether acquisition can leave a representation-independent, physically charged, persistent capability effect that cannot be compiled away as ordinary state.