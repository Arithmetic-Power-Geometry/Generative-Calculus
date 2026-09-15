# GC-II Audit 159 — endogenous task formation compilation no-go

## Candidate attacked
Audit 158 left open *closure creation under endogenous task formation*: two systems can have the same present operational conversion structure while differing in the tasks/specifications they can subsequently generate, potentially exposing different future closure obligations.

## Formal setting
Let an operational configuration be

`z_t = (x_t, R_t, I_t, A_t, L_t, G_t, H_t)`

where `x_t` is physical/semantic state, `(R,I,A,L)` are typed resource/information/interface/rule components, `G_t` is the currently active task/specification set, and `H_t` is a sufficient internal state of the task generator. An admissible step may both act on the world and generate/retire tasks:

`(z_t,a_t) -> (z_{t+1}, o_{t+1})`, with `G_{t+1}=Phi(H_t,x_t,G_t,a_t,o_{t+1})` and `H_{t+1}=Psi(H_t,x_t,G_t,a_t,o_{t+1})`.

Assume `H,G` have effective exact representations and `Phi,Psi`, enabledness, observation law, and world/resource update are effective from the augmented state.

## Proposition — endogenous-task compilation
Under these assumptions, endogenous task formation does **not** by itself imply Closure-Escape. There is an ordinary augmented transition system on `Z` whose paths are in one-to-one correspondence with the original histories and which preserves, at every prefix, world state, typed budgets, generated task set, enabled actions, observations, and therefore every closure obligation that is a function of the represented augmented state.

### Proof
Take the augmented configuration itself as the compiled state. The initial compiled state equals the original initial tuple. Suppose the compiled and original states agree after a history `h`. Because enabledness and transition/observation laws are functions of the same sufficient tuple, they expose the same admissible next actions and observation distributions/branches. Applying a matched action/observation invokes the same world/resource update and the same `Phi,Psi`, hence produces equal successor tuples. Induction over finite histories gives exact path correspondence. Any task-indexed closure predicate evaluated from the tuple is consequently preserved. The argument also covers task creation that depends on the entire past whenever `H_t` is an exact sufficient history summary.

## Consequence
`task generation changes what must later be achieved` is not sufficient for a non-tautological GC-II Closure-Escape theorem. The obstruction can only survive this compilation if at least one required sufficient component is unavailable under the claimed operational interface, is not finitely/effectively representable, or the proposed GC observable deliberately restricts access to it. Those alternatives immediately create new collision obligations with partial observability/belief-state constructions, automata/streaming lower bounds, undecidability, and representation-relative complexity.

## Prior-art collision
This boundary is already strongly occupied. Goal-reasoning/planning work explicitly handles dynamic goals and anticipatory planning; learning-driven goal generation predicts future goals and plans for them. Intrinsically Motivated Goal Exploration Processes explicitly self-generate, select, order, and experiment with goals, and adversarial goal-generation methods similarly learn goal generators. BDI/procedural reasoning architectures represent goals and deliberation state at runtime. Therefore endogenous goal/task formation itself cannot carry a GC-II novelty claim.

Relevant collision anchors checked in this audit:
- Pozanco, Fernandez & Borrajo, *Learning-driven goal generation*, AI Communications 31(2), 2018, DOI 10.3233/AIC-180754.
- Forestier, Portelas, Mollard & Oudeyer, *Intrinsically Motivated Goal Exploration Processes with Automatic Curriculum Learning*, arXiv:1708.02190.
- Campero et al., *Learning with AMIGo: Adversarially Motivated Intrinsic Goals*, arXiv:2006.12122.
- Probabilistic-hyperproperty planning work also shows that richer/generated obligations can be represented as richer specifications over augmented/self-composed models; expressivity alone is not an escape certificate.

## Verification checklist
- Domains: proposition requires exact effective representations of `G,H`; no finiteness assumption is needed for the semantic construction, but finite compilation requires finite reachable augmented state.
- Degenerate case: fixed `G` reduces to ordinary augmented-state compilation.
- History dependence: absorbed exactly when `H` is sufficient.
- Monotonicity: none assumed for task sets; tasks may be added or retired.
- Composition: preserved because matched one-step transitions inductively preserve concatenated histories.
- Invariance: semantic path correspondence is invariant to recoding of sufficient states; representation-size claims are not.
- Counterexample boundary: if no effective sufficient `H` exists in the chosen model, this proof does not establish compilation; that is OPEN rather than evidence of escape.

## Status ledger
- Endogenous-task augmented-state compilation: **PROVED under effective sufficient-state assumptions**.
- Task generation alone implies Closure-Escape: **FALSIFIED**.
- Dynamic/learned/self-generated goals: **IMPORTED/KNOWN**.
- Hyperproperty/richer-specification expressivity alone as novelty: **FALSIFIED as a sufficient route**.
- Finite compiler when reachable `(G,H)` is finite: **CONDITIONAL/PROVED under finiteness**.
- A nontrivial GC-II residual after sufficient-state augmentation: **OPEN**.

## Surviving gate
Stop treating *what changes* (actions, rules, information, costs, models, or tasks) as the escape mechanism: Audits 149–159 repeatedly show that any effectively sufficient evolving component can be lifted into state. The next candidate should attack a different axis: **operationally inaccessible but globally necessary coordination information**. Seek a local-to-global translator lower bound where (i) local agents/interfaces have fixed admissible observations and transformations, (ii) the global capability is realizable with a coordinator/transcript, (iii) every exact translator requires a provable amount of communication/information/resource, and (iv) the bound strengthens the GC-I proper-projection irreducibility witness quantitatively. Collision gate: deterministic/randomized communication complexity, distributed synthesis, CSP/database join width, marginal/contextuality consistency, and information complexity. A result is GC-II-worthy only if the GC structure yields a new quantitative theorem beyond a direct restatement of those imported lower bounds.
