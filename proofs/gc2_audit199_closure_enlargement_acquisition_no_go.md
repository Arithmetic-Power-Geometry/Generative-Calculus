# GC-II Audit 199 — Closure enlargement does not force acquisition change

Status: **PROVED (finite counterexample) / decisive falsification of the unrestricted implication**

## Candidate implication under test

Audit 198 left the question whether a strict operational-closure enlargement must force a nonzero change in at least one acquisition-relevant component: response distinguishability, admissible probes/actions, physical cost, or uncertainty.

The unrestricted implication is false.

## Construction

Fix a complete acquisition experiment

\[
E=(W,Q,P,\Pi,c,T,\varepsilon),
\]

where `W` is the uncertainty set, `Q` the probe/interface set, `P` the response kernel, `Pi` the admissible policy class, `c` the operational cost, `T` the decision task, and `epsilon` the allowed error.

Take two operational systems S0 and S1 with exactly the same acquisition experiment E. Let their capability closures be

\[
\mathcal C_0=\{x\},\qquad \mathcal C_1=\{x,y\},
\]

where `y` is generated in S1 by a deterministic zero-query transformation that neither changes W nor Q, P, Pi, c, T, or epsilon. Hence

\[
\mathcal C_0\subsetneq\mathcal C_1
\]

but

\[
E_0=E_1.
\]

Since minimum acquisition cost is a functional only of the complete experiment,

\[
AC(E_0)=AC(E_1).
\]

All response distinguishabilities are also identical because P is identical; admissible probes/actions used by the acquisition problem are identical; costs and uncertainty are identical.

Therefore

\[
\boxed{\mathcal C_0\subsetneq\mathcal C_1\not\Rightarrow \Delta E\ne0.}
\]

Strict closure enlargement alone does **not** force any acquisition change.

## Why this is not a degenerate equality trick

The new capability y is operationally real: it is reachable in S1 and not reachable in S0. The failure arises because capability closure and acquisition experiment answer different questions. Unless the enlarged capability is required to be decision-critical for T, or required to modify the experiment through a coupling axiom, closure can grow orthogonally to epistemic acquisition.

A positive theorem therefore requires an explicit coupling condition. A minimal candidate is task-relative:

> If every newly reachable capability changes the required decision on at least one pair of worlds still confusable under the old experiment, then some acquisition-relevant structure must change before that capability can be certified/used with the required error.

This candidate is **OPEN** and must be checked against Blackwell/Le Cam deficiency, query complexity, active learning and decision theory before novelty can be claimed.

## Edge cases and checks

- Empty uncertainty set: excluded as operationally vacuous; the counterexample works for any nonempty finite W.
- Singleton W: still valid; acquisition may cost zero in both systems.
- Nonzero acquisition cost: valid by choosing any E with AC(E)>0; equality remains because E is unchanged.
- Noisy responses: valid; P may be arbitrary and identical in both systems.
- Composition: adjoining an acquisition-orthogonal capability to either factor preserves the counterexample under product composition whenever the acquisition experiment factors independently.
- Units/dimensions: no heterogeneous scalar is formed; AC retains the units assigned by c.

## Prior-art boundary

Blackwell comparison already characterizes decision usefulness of experiments via garbling/decision performance. Le Cam deficiency quantifies approximate simulability/risk gaps. Thus any repaired theorem stated solely as a change in statistical-experiment informativeness is likely IMPORTED/KNOWN. GC-II novelty, if any, must come from a defensible generative coupling axiom linking closure creation to decision-critical changes in the acquisition experiment, followed by a bound not reducible to standard deficiency/query-complexity statements.

## Ledger

- strict closure enlargement => nonzero acquisition-experiment change: **FALSIFIED**.
- acquisition-orthogonal strict closure enlargement with identical complete experiment: **PROVED**.
- equal complete experiment => equal minimum acquisition cost: **PROVED** (Audit 198, reused).
- Blackwell/Le Cam experiment comparison mechanisms: **IMPORTED/KNOWN**.
- decision-critical generative coupling theorem: **OPEN**.
