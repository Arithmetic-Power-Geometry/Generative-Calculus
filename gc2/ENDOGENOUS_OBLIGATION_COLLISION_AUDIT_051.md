# GC-II Audit 051 — Endogenous Obligation Generation Collision

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 050

## Question

Does replacing a fixed obligation family Q by a history-dependent generator h -> q_h create a nontrivial GC-II novelty mechanism?

## Formal model

Let H be the set of finite admissible interaction histories. Let G:H->Q be an obligation generator and let R(q,h) denote an admissible realization policy for q after history h. Typed costs are kept separate as c=(R,I,A,L); no scalar addition is assumed. The coupled process is

    h -> G(h)=q_h -> R(q_h,h).

The candidate novelty claim would require this endogenous generation-realization process to escape compilation into an ordinary fixed operational machine without hiding unaccounted resources.

## Compilation theorem

Assume (i) G is a fixed computable transducer, (ii) the realization rules are fixed and computable, and (iii) the history alphabet and machine description are part of the declared substrate. Then the coupled process compiles into a single ordinary interactive machine M whose state contains the current history/transducer state. On each history prefix M computes G(h), then invokes the declared realization transition relation.

Therefore history dependence alone does not create a new closure notion. The reachable pairs (h,q_h) are simply reachable states/outputs of M. If costs of G and R are explicitly charged, the compilation preserves the same typed execution trace costs up to the declared compiler convention; if G is declared free, any apparent novelty can instead be an accounting artifact.

Status: PROVED as a direct machine construction; mechanism IMPORTED/KNOWN.

## Finite-world exact form

For finite H, define the graph with vertices (h,s) where h is an admissible history and s is the realization state. Add a transition for every allowed observation/action update and label each reached vertex with q=G(h). Exhaustive graph traversal enumerates exactly every generated-obligation/realization pair. Hence finite endogenous obligation creation is ordinary reachability in the expanded state space.

Status: PROVED.

## Stronger computable/infinite form

When H is countably infinite but G and the operational rules are computable, a universal machine can simulate the coupled generator-realizer. The set of generated obligations may be impossible to enumerate within a finite resource bound, and reachability may become undecidable, but those facts are ordinary computability/complexity phenomena. Undecidability or open-ended output growth alone therefore cannot certify Omega_G>0.

Status: reduction architecture IMPORTED/KNOWN; no novelty claim.

## Collision checks

- Online/adaptive algorithms already choose future computations/actions from interaction history.
- Active information-seeking agents generate queries conditioned on history and learned state.
- Program synthesis maps specifications/queries to programs and can operate iteratively with feedback.
- Adaptive query processing changes computation using runtime feedback.
- Recent curiosity/task-synthesis systems explicitly generate new training tasks from environment interaction; therefore "the system generates what to learn next" is not a unique GC-II mechanism.
- Universal computation absorbs any fixed computable generator-realizer into one machine description.

These collisions do not make GC-II useless; they show that endogenous q_h by itself is insufficient as the distinguishing theorem ingredient.

## Exact kill test

If there exists a fixed computable machine M that, from the conserved history interface, reproduces both the generated obligation q_h and its admissible realization with the same declared typed cost trace (or a declared compiler-equivalent trace), then any Omega_G depending only on endogenous generation-realization behavior must assign zero extra generative novelty beyond the ordinary operational/computational costs.

## Edge/domain checks

- Constant G reduces immediately to a fixed obligation.
- Finite-range G reduces to a fixed finite query family plus online query selection.
- Infinite-range computable G does not evade universal simulation.
- Randomized G is represented by including the random seed/source in the operational state and accounting for its information/resource status.
- Oracle/noncomputable G can escape computable compilation only by importing an oracle; the oracle must be charged as an external capability and cannot establish a no-free-capability theorem by assumption.
- Self-modifying code remains simulable by a universal interpreter when the modification semantics are computable.
- Evaluator drift must be represented explicitly; silently changing what counts as success invalidates conserved-obligation comparisons.
- Typed R,I,A,L components remain incomparable without conversion laws.

## Consequence for Omega_G

History-dependent obligation generation, even with an unbounded computable obligation range, is not sufficient for Omega_G>0. A scalar count of newly generated obligations is also representation-dependent and can be inflated by renaming or syntactic refinement.

Status: endogenous-obligation generation as standalone GC-II novelty route FALSIFIED.

## Surviving target

The remaining candidate must compare not merely outputs or generated tasks but the minimum accounted cost of *changing the effective generator/operational law itself* under a conserved meta-interface, while excluding free oracle injection and mere program rewriting. A possible object is a law-extension deficiency: the minimum typed cost required for one substrate to emulate the other substrate's future generator-realizer under every admissible continuation, after quotienting semantics-preserving interpreters.

This is NOT a breakthrough claim. Immediate collision classes are universal simulation, algorithmic information/Kolmogorov complexity, reflective interpreters, proof-system extension, meta-learning, nonstationary online learning, resource theories of channels/processes, and logical induction. The next kill test is whether any proposed law-extension deficiency is just description length plus simulation overhead under a chosen universal machine.

## Final classification

- Coupled h -> q_h -> realization model: VALID definition.
- Finite expanded-state compilation: PROVED.
- Computable transducer compilation: PROVED.
- Endogenous obligation generation as standalone novelty: FALSIFIED.
- Noncomputable/oracle escape: IMPORTED capability, not free novelty.
- Law-extension deficiency: OPEN, next target.