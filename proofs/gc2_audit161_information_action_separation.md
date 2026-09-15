# GC-II Audit 161 — Information sufficiency does not imply operational realizability

## Candidate gate
Audit 160 left a proposed separation: hold local information and communication fixed at a level sufficient for ordinary global reconstruction/decision, but make a target capability unrealizable because interface/action/law constraints prevent the information from being operationalized.

## Formalization
Let a finite world have hidden state `x in X`, observation/communication transcript `tau(x)`, admissible action profiles `U(x,tau)` and target relation `G subseteq X x U`.

Define informational sufficiency for the target by existence of a decoder `d` such that `d(tau(x))` identifies all target-relevant information (in the strongest case, `d(tau(x))=x`). Define operational realizability by existence of an admissible policy `pi` satisfying

`pi(tau(x)) in U(x,tau(x))` and `(x,pi(tau(x))) in G` for every `x`.

These notions are distinct.

## Exact separation theorem — PROVED
There exist finite systems in which the transcript reconstructs the complete global state exactly, yet no admissible policy realizes the target capability.

Witness: `X={0,1}`, transcript `tau(x)=x`, action alphabet `{0,1}`, target `G={(0,0),(1,1)}`, and admissible action set `U(x,tau)={0}` for both worlds. Reconstruction is exact. Operational realization fails at `x=1` because the required action `1` is not admissible.

Thus

`information sufficient for target decision/reconstruction != capability realizability`.

The separation remains valid with nontrivial resource budgets by assigning both transcript acquisition and admissible action 0 costs within budget while action 1 is absent/forbidden by the interface/law rather than merely over budget.

## Necessary-and-sufficient finite criterion — PROVED
For a fixed transcript map and memoryless admissibility relation, a deterministic policy exists iff for every transcript class `T_y={x:tau(x)=y}`, the intersection

`A_y = intersection_{x in T_y} {u in U(x,y) : (x,u) in G}`

is nonempty.

Proof: necessity follows because one policy value `pi(y)` must work for every world sharing transcript `y`; sufficiency follows by selecting any element of each nonempty `A_y`.

When `tau` is injective (full reconstruction), this reduces to the pointwise condition that each world has at least one admissible goal-satisfying action. Hence full information removes observational ambiguity but cannot repair missing control authority.

## Edge cases / invariance / composition
- Singleton world: criterion reduces to existence of one admissible goal action.
- Unrestricted interface `U` containing every target action: full reconstruction is sufficient.
- Empty target-feasible action set at any injectively observed world: realizability fails regardless of communication budget.
- Relabeling worlds, transcripts, or actions preserves the criterion under transported `U` and `G`.
- Product composition is not automatically additive: shared actions/couplings can create or destroy feasible intersections.
- More communication refines transcript classes and can enlarge feasibility, but after transcripts are injective additional information cannot overcome a genuinely forbidden/missing action.

## Prior-art collision — DECISIVE
This separation is mathematically valid but is not an independent GC-II breakthrough. Distributed synthesis and distributed control already distinguish information architecture from realizability under allowed local outputs/actions. Classical distributed synthesis asks whether implementations respecting a fixed architecture can realize a temporal specification; general architectures with information forks are undecidable, while structured information-flow architectures admit synthesis results. Control communication complexity likewise studies control under finite-bandwidth communication constraints, explicitly coupling information exchange to control realizability. Information-flow-guided synthesis formulates requirements ensuring that information needed for an action is passed to the responsible component.

Therefore the statement 'enough information to reconstruct/decide, but insufficient operational authority to realize' is a clean GC-II accounting distinction but belongs to known distributed synthesis/control semantics.

## Ledger
- Informational sufficiency versus operational realizability distinction: **PROVED**.
- Exact two-world separation: **PROVED**.
- Transcript-class intersection criterion: **PROVED** for finite memoryless systems.
- Full reconstruction as sufficient for capability generation: **FALSIFIED**.
- Missing/forbidden action authority as the separating mechanism: **IMPORTED/KNOWN** from synthesis/control.
- Raw information-action separation as `Omega_G`: **FALSIFIED as independent novelty**.
- Nonlinear four-axis capability accounting beyond fixed architecture synthesis/control: **OPEN**.

## Breakthrough consequence
Audit 161 closes the most direct continuation of Audit 160. A viable `Omega_G` cannot be merely missing information, missing action authority, or their conjunction in a fixed architecture. The next gate should test whether capability creation has a path-dependent *joint enabling burden* that cannot be represented by a fixed augmented-state synthesis/control problem without changing the quantity being measured. Any candidate must be checked first against constrained planning, distributed synthesis/control, Petri/vector-addition systems, resource theories, and state-augmentation compilation no-go results from Audits 153–159.
