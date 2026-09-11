# GC-II Audit 084 — Relative Common-Class Closure Deficiency

## Scope
Branch-only Paper-II audit. GC-I foundations on `main` remain frozen.

## Inspected parent
`cce83b47ecc637f2a3232b32b580d61ce03907d7` (Audit 083).

## Candidate inherited from Audit 083
For systems `S,T`, task `q`, one common realization class `P`, and a family of dimensionally valid scalarized decision criteria `Lambda`, consider

\[
\delta_{\mathcal P}^{\Lambda}(S\Vert T;q)
=\sup_{\lambda\in\Lambda}
\big[V_{\lambda,\mathcal P}(S,q)-V_{\lambda,\mathcal P}(T,q)\big]_+.
\]

The hope was that subtracting optimal values inside the same physical realization class might cancel shared realization overhead and leave a GC-specific directed capability deficiency.

## Result
**FALSIFIED as a standalone breakthrough invariant in this form.**

The object is a restricted worst-case decision-value/risk gap. Once the admissible decision problems, losses, randomizations/simulations, boundary conditions, and realization class are fixed, its mathematical content is already the comparison-of-experiments / directed-deficiency architecture, or a restricted regret/IPM-like variant when `Lambda` is restricted.

### 1. Restricted decision-gap identity — PROVED
Define for each admissible criterion `lambda`

\[
G_\lambda(S,T;q)
:=V_{\lambda,\mathcal P}(S,q)-V_{\lambda,\mathcal P}(T,q).
\]

Then by definition

\[
\delta_{\mathcal P}^{\Lambda}(S\Vert T;q)
=\sup_{\lambda\in\Lambda}[G_\lambda(S,T;q)]_+.
\]

Thus the proposed scalar contains no additional structure beyond the family of decision-value differences supplied to it. If `Lambda` is enlarged, the value cannot decrease. If `Lambda` is a singleton, it is merely one positive regret gap. If all criteria agree, the value is zero.

### 2. Common-overhead cancellation is conditional — PROVED
Suppose every scalarized value decomposes as

\[
V_{\lambda,\mathcal P}(X,q)=H_{\lambda,\mathcal P}(q)+W_{\lambda,\mathcal P}(X,q),
\]

with exactly the same additive overhead `H` for `X=S,T`. Then

\[
V(S,q)-V(T,q)=W(S,q)-W(T,q),
\]

so that overhead cancels. But if realization overhead depends on the system, interacts nonadditively with it, or changes the feasible policy set, subtraction does not isolate an intrinsic capability term. Therefore cancellation is not a theorem of the construction; it is an assumption on the realization model.

### 3. Blackwell/Le Cam collision — IMPORTED/KNOWN
In statistical comparison, one-sided deficiency already quantifies how well one experiment can simulate another by an admissible randomization, and randomization theorems relate this to worst-case excess risk over decision problems. Hence when `S,T` are information structures/experiments, `P` permits the relevant Markov kernels, and `Lambda` ranges over normalized losses/decision problems, the proposed worst-case directed value gap is precisely the kind of operational quantity deficiency theory was built to characterize (up to orientation and normalization conventions).

Consequently a GC-II novelty claim cannot be based on taking a supremum of common-class decision-value gaps alone.

### 4. Simulation/resource-preorder collision — PROVED reduction
If `S` simulates `T` under the declared free/admissible transformations and every `V_lambda` is monotone under that simulation preorder in the chosen orientation, then every positive-part gap in the dominated direction vanishes. Zero relative gap therefore need not mean physical identity; it means indistinguishability by the selected criterion family. Conversely, positivity witnesses failure of domination for at least one selected criterion. This is ordinary separation by monotones/decision functionals.

### 5. Restricted-family incompleteness — PROVED
For any proper criterion family `Lambda`, two operational objects can agree on all `V_lambda`, `lambda in Lambda`, yet differ on an omitted admissible criterion. Therefore

\[
\delta_{\mathcal P}^{\Lambda}=0
\]

does not imply complete convertibility/equivalence unless `Lambda` is independently proved complete. Declaring `Lambda` to be all admissible decision problems restores completeness only by importing the universal decision-problem comparison architecture.

### 6. Scalarization caveat — PROVED
For typed `R,I,A,L` frontiers, scalarization can erase Pareto distinctions. Equality for a finite or restricted family of weights does not imply equality of nonconvex attainable sets. If all nonnegative linear scalarizations are used, they characterize only the appropriate closed convex upper hull without additional hypotheses. Thus a scalar relative deficiency cannot silently serve as a complete typed closure invariant.

## Edge-case audit
- `S=T`: deficiency is zero.
- `Lambda` empty: supremum requires a convention and carries no capability content.
- `Lambda` singleton: positive regret gap only.
- `Lambda` enlarged: deficiency is monotone nondecreasing.
- Identical additive overhead: cancels exactly.
- System-dependent/nonadditive overhead: does not cancel in general.
- Free simulation `S -> T`: monotone decision gaps vanish in the dominated orientation.
- Incomplete criterion family: zero does not imply equivalence.
- Rescaling losses without normalization: numerical deficiency can be arbitrarily rescaled; normalization is essential.
- Typed incommensurate ledgers: scalarization must be declared and dimensionally valid.
- Randomization/catalysis/advice: must be inside the common admissible class or comparisons change.

## Prior-art collision boundary
Classical Blackwell comparison ranks experiments by performance across decision problems. Le Cam deficiency quantifies approximate comparison through randomizations and has equivalent risk interpretations under its hypotheses. Comparison theory also permits deficiencies relative to restricted classes of decision problems. Quantum generalizations similarly characterize channel/experiment comparison through post-processing and decision success probabilities. Therefore the proposed relative common-class decision gap lies directly inside an established mathematical architecture unless GC-II supplies additional structure not reducible to decision-risk comparison.

## Consequence for Paper II
Audits 072–084 now rule out a broad family of tempting definitions: neither absolute implementation cost nor a worst-case relative decision-value gap becomes a new generative invariant merely by placing it inside the GC ledger.

The useful surviving direction is not another scalar deficiency. It is a **typed closure-separation theorem** asking whether the full task-scale-error-budget attainable correspondence contains operational distinctions that provably cannot be represented by any fixed family of ordinary experiment-deficiency, simulation-preorder, resource-monotone, or scalarized-risk comparisons under the same admissible transformations.

A candidate must provide an explicit pair/family of finite operational systems and prove both:

1. agreement under the imported comparison structures being quotiented out; and
2. a remaining GC closure distinction with a computable operational consequence.

Without such a separating witness, the Paper-II breakthrough remains OPEN.

## Next executable attack
Construct small finite controlled systems and search for a separating witness. For each pair, compute: exact reachability/simulation relation; all normalized binary decision risks; directed Blackwell/Le Cam deficiency where applicable; typed Pareto closure over budgets; and candidate GC closure descriptors. Any candidate distinction that is a function of the imported quantities is rejected. Only a collision-surviving residual proceeds to theorem status. No numerical result is claimed in this audit because that exhaustive experiment has not yet been executed.

## Status table
| Claim | Status |
|---|---|
| Relative common-class decision gap is standalone GC-II novelty | FALSIFIED |
| Restricted decision-gap identity | PROVED |
| Exact additive common overhead cancels | PROVED |
| Generic common-overhead cancellation | FALSIFIED |
| Blackwell/Le Cam risk-gap architecture | IMPORTED/KNOWN |
| Restricted `Lambda` is automatically complete | FALSIFIED |
| Scalarization preserves every typed Pareto distinction | FALSIFIED |
| Typed closure-separation residual beyond imported comparisons | OPEN |
| GC-II positive breakthrough | OPEN / NOT ESTABLISHED |
