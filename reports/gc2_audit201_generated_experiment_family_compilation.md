# GC-II Audit 201 — Generated experiment families compile to controlled sensing

## Target inherited from Audit 200
Test whether capability generation that changes the admissible experiment family or its cost geometry yields a GC-specific quantitative law.

## Finite model
Let W be a finite world set. A configuration is z=(s,m), where s is ordinary operational state and m is a finite mode encoding which probes/actions are currently admissible. At z, the system exposes a finite admissible experiment set Q(z). Executing q in world w produces observation o with kernel P(o|w,z,q), incurs cost c(w,z,q,o) (or its world-independent special case), and updates configuration by K(z'|w,z,q,o). Some actions may be generative: their update changes m and therefore changes Q(z') and future costs/kernels.

A policy maps histories to admissible experiments or a terminal decision. Define the budgeted closure/decision problem by any finite horizon H, budget B, terminal loss ell(a,w), and error/utility criterion.

## Compilation theorem
**Theorem (finite generated-experiment compilation).** Every finite system above is exactly representable as a finite controlled-sensing POMDP / history-dependent sequential experiment with augmented hidden/controlled state (w,z). The compiled model uses the same action q, observation o, transition K, observation kernel P, and cost c. Consequently there is a cost- and transcript-preserving bijection between admissible policies in the two descriptions.

Therefore, for every horizon H and budget B:

1. the distributions of complete transcripts coincide under corresponding policies;
2. accumulated resource cost coincides pathwise;
3. terminal decision risk coincides;
4. budget-feasible policy sets coincide;
5. optimal value, minimum Bayes risk, and minimum acquisition cost coincide.

### Proof
Induct on history length. At the empty history both models have the same initial augmented state distribution. Assume the joint law of (w,z,h_t) agrees. Both descriptions expose exactly Q(z); corresponding policies therefore choose the same conditional distribution over q. Conditional on (w,z,q), both generate o using P and z' using K and charge the same c. Hence the joint law of (w,z',h_{t+1}) and accumulated cost agrees. Induction gives equality for every finite history. Terminal decisions are functions/kernels of the same histories, proving equality of risk and value. The converse policy map is identity on histories and actions.

## Consequence
Merely allowing generation to change future admissible probes, observation kernels, or probe costs is **not sufficient** for a GC-II Closure-Escape theorem. In finite systems this is an alternative description of controlled sensing / POMDP / sequential experimental design with action-dependent information and costs.

This does **not** prove that every quantitative GC-II result is old. It proves a representation/no-go boundary: novelty cannot rest solely on endogenous finite experiment-family or cost-geometry change. A surviving theorem must impose structure that yields a new invariant/bound under the compilation, or move to a regime where the compilation loses the property being claimed (for example a uniform complexity/resource restriction, compositional interface restriction, or cross-system conservation law).

## Checks
- Domains: W,Z,Q,O finite; costs nonnegative extended reals or bounded nonnegative reals for finite expectations.
- Degenerate one-mode case reduces to ordinary fixed-family controlled sensing.
- Zero-cost actions are allowed; they do not break policy/transcript equivalence.
- Generative actions may add or remove probes and change costs/kernels; encoded by z/mode.
- Monotonicity is not assumed: generation may improve or worsen the experiment family.
- Composition: sequential composition is preserved because the augmented state carries the generated mode.
- Invariance: relabeling modes/actions/observations leaves the theorem unchanged.
- Infinite/uncomputable families are outside this exact finite theorem and remain OPEN.

## Prior-art collision boundary
Controlled sensing already permits action-dependent observations and non-uniform control costs, including Markovian observation structure. Value-of-information and Bayesian experimental-design frameworks already optimize costly observation acquisition for downstream decisions. POMDP state augmentation is the standard representation move for finite history-relevant modes. Thus the extensional finite mechanism is IMPORTED/KNOWN territory; GC-II must contribute a stronger structural theorem rather than rename it.

## Status ledger
- Finite generated experiment-family/cost compilation: PROVED.
- Transcript/cost/risk/value preservation: PROVED.
- Endogenous finite experiment-family change alone as GC-II novelty: FALSIFIED.
- Controlled sensing / value-of-information mechanism: IMPORTED/KNOWN.
- Non-additive universal Omega_G <= F(Delta R,Delta I,Delta A,Delta L) without additional coupling assumptions: still OPEN; this audit warns that arbitrary mode-dependent costs make a universal nontrivial F impossible unless the deltas are operationally defined strongly enough to dominate those costs.
- Candidate survivor: a representation-invariant *cross-system capability accounting law* under explicit matched admissible simulators and resource conversion rules, tested against resource theories and directed deficiency: OPEN.

## Reproducibility
`experiments/gc2_audit201_generated_experiment_compilation.py` exhaustively compares a small two-world generated-probe system against its augmented controlled-sensing compilation for all deterministic policies up to horizon 2, checking transcript and cost equality.