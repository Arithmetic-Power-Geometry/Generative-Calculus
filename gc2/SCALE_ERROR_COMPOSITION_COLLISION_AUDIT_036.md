# GC-II Audit 036 — Scale–Error Composition Collision

## Purpose

Audit 035 left a deliberately harder target: hold the ordinary joint-demand problem fixed and seek a separation caused only by scale-indexed error–budget compatibility under composition. This audit tests whether **that ingredient by itself** can support a GC-II novelty claim.

## Status summary

- Scale-indexed joint error/budget feasibility: **IMPORTED/KNOWN as a general mechanism**.
- “A whole-envelope escape caused by simultaneous error budgets across scales is sufficient evidence of GC-II novelty”: **FALSIFIED**.
- GC-II-specific residual after strongest neighboring-theory embeddings: **OPEN**.
- No new theorem is claimed here beyond the reduction/collision statement below.

## 1. Controlled formulation

Fix a common action/translator set `P`, a finite obligation index set `Q`, and for each obligation `q` an error functional

\[
e_q:P\to[0,\infty]
\]

with admissible threshold `epsilon_q`. Let resource cost be

\[
c:P\to \mathbb R_+^m,
\]

with budget vector `B`. A whole-envelope feasible translator is exactly an element of

\[
\mathcal F(\epsilon,B)
=
\{p\in P: e_q(p)\le \epsilon_q\ \forall q\in Q,\ c(p)\preceq B\}.
\]

Scales can be included by taking `q=(task,scale)`; composition-dependent errors can be included by defining `e_q` on composed policies/programs rather than primitive actions.

Closure escape under augmentation `u` is then the event

\[
\mathcal F_0(\epsilon,B)=\varnothing,
\qquad
\mathcal F_u(\epsilon,B)\ne\varnothing.
\]

This is a clean GC-compatible object, but the question is whether its mathematical mechanism is distinct.

## 2. Reduction boundary

### Proposition 036.1 — Constraint compilation

For any finite family of declared scale/error obligations above, exact whole-envelope feasibility is a standard constrained feasibility problem with one constraint per obligation plus the resource constraints.

**Proof.** Define

\[
g_q(p)=e_q(p)-\epsilon_q,
\qquad
g_{R,j}(p)=c_j(p)-B_j.
\]

Then `p` is GC whole-envelope feasible iff every `g_q(p)<=0` and every `g_{R,j}(p)<=0`. Conversely every feasible point of that constraint system satisfies the declared GC obligations. The correspondence is identity on `p`, hence preserves feasibility exactly. QED.

This proposition is intentionally elementary. Its importance is negative: merely indexing constraints by task and scale does not create a new semantic class.

### Corollary 036.2 — Joint failure formulation

If each `e_q` is a violation probability, requiring all declared bounds simultaneously is a joint/chance-constrained or multi-constraint reliability problem. If `e_q` is a risk/error functional, the same construction is a multi-risk constrained optimization problem. If the constraints are robust over an ambiguity set, it is a distributionally robust joint-constraint problem.

Thus a strict separation between per-obligation feasibility and simultaneous whole-envelope feasibility can arise without any GC-specific machinery.

## 3. Minimal simultaneity witness

Let `P={a,b}` and two obligations `q1,q2`, with

\[
(e_1(a),e_2(a))=(0,1),\qquad
(e_1(b),e_2(b))=(1,0),
\]

and thresholds `epsilon_1=epsilon_2=0`.

Each obligation is individually feasible, but

\[
\mathcal F((0,0),B)=\varnothing
\]

for any nonbinding `B`. Add a third policy `c` with `(e_1(c),e_2(c))=(0,0)` and whole-envelope feasibility appears.

The phenomenon is real, but it is nothing more than simultaneous constraint satisfaction. Therefore “individual tasks/scales agree while the whole envelope differs” remains insufficient unless the construction controls for the full joint constraint system.

## 4. Composition does not rescue novelty by itself

Suppose policies compose with `\circ` and the error law is

\[
e_q(p\circ r)\le \Phi_q(e(p),e(r))
\]

for declared composition maps `Phi_q`. Once the composition law is specified, it can be incorporated into the feasible-set definition or an augmented state. Nonadditive, multiplicative, max-type, and risk-sensitive error propagation therefore do not by themselves evade the reduction.

A candidate theorem must do more than show that errors accumulate nonlinearly. It must produce a conclusion that fails under the strongest faithful embedding into constrained optimization / reliability / risk / approximate-refinement formalisms.

## 5. Prior-art collision check

The relevant neighboring mechanisms include:

1. joint chance constraints and distributionally robust joint chance constraints;
2. multiobjective and robust optimization with reliability/vulnerability budgets;
3. risk measures and multiple error/risk constraints;
4. approximate simulation/refinement metrics where errors propagate under composition;
5. reliability allocation and compositional verification.

Fresh literature checks for this audit found explicit work on ambiguous joint chance constraints and optimization under probabilistic envelope constraints, including simultaneous probabilistic guarantees and violation magnitude. These are strong collisions with any claim based only on simultaneous scale/error budgets.

References checked during this audit:

- Hanasusanto, Roitch, Kuhn & Wiesemann, *Ambiguous Joint Chance Constraints Under Mean and Dispersion Information*, Operations Research 65(3), 2017, DOI 10.1287/opre.2016.1583.
- Xu et al., *Scenario-Based Multiobjective Robust Optimization and Decision-Making Framework for Optimal Operation of a Cascade Hydropower System Under Multiple Uncertainties*, Water Resources Research, 2022, DOI 10.1029/2021WR030965.
- Grechuk & Zabarankin, *Sensitivity Analysis in Applications with Deviation, Risk, Regret, and Error Measures*, SIAM Journal on Optimization 27(4), 2017, DOI 10.1137/16M1105165.

These citations do not prove equivalence to every GC model. They establish that the generic mechanism is already occupied and that novelty must rest on a sharper residual.

## 6. Edge and degeneracy checks

- `Q=empty`: feasibility reduces to resources only; no novelty gap can be attributed to error obligations.
- Infinite thresholds: the corresponding obligation is vacuous.
- Identical error functionals across scales: scale labels add no mathematical content.
- Zero resource cost: the collision remains; resource accounting is not needed for the simultaneity effect.
- Nonlinear `Phi`: still a declared constraint/composition law; nonlinearity alone is insufficient.
- Infinite `Q`: compilation becomes an infinite/semi-infinite constraint system; this can alter computability but does not by itself establish GC novelty.
- Adaptive policies: include histories/beliefs in `P` or state; adaptation alone is not a novelty certificate.

## 7. Consequence for Omega_G

A defensible `Omega_G` cannot assign novelty merely because

\[
\forall q\ \exists p_q: e_q(p_q)\le\epsilon_q
\quad\text{but}\quad
\nexists p\ \forall q: e_q(p)\le\epsilon_q.
\]

That quantifier gap is generic simultaneous feasibility.

Any positive GC-II candidate must instead compare systems after preserving the **entire joint obligation structure**, including error/risk functions, composition law, admissible policies, resource constraints, and ordinary uncertainty model.

## 8. Stronger surviving target

The next target should test **endogenous obligation generation** rather than a fixed indexed constraint family:

- admissible operation changes which future task/scale/error obligations become binding;
- those future obligations are not merely hidden members of a fixed pre-enumerated constraint set;
- the operational closure must account for the cost of creating the very tests/obligations under which future capability is judged;
- the candidate must be collision-tested against dynamic games, temporal logic/model checking, adaptive robust control, mechanism/design-of-experiments, and endogenous specification synthesis.

Even this is only a candidate direction: configuration compilation from Audits 026–027 warns that finite endogenous obligation generation may again compile to an augmented transition system. The scientific target is therefore a quantitative residual (representation, information, or operational cost) that survives that compilation and the prior-art embeddings.

## 9. Paper-II status update

The requested progression remains conservative:

- budgeted closure: formal finite models available, mechanisms largely imported;
- Omega_G: no breakthrough definition yet;
- Closure-Escape: exact restricted criteria exist, generic versions collide with known feasibility/reachability theory;
- No-Free-Capability: restricted information/rank bounds proved, mechanism imported;
- aggregate four-axis bound: universal structural version falsified in Audit 030;
- complete monotones: unrestricted finite/computable version falsified in Audit 031;
- local-to-global translator: parametric lower bound proved in Audit 032, coding mechanism imported;
- reversibility gap: remains without a validated GC-specific invariant;
- scale/error simultaneity: **this audit falsifies it as a standalone novelty route**.

No breakthrough claim is made.
