# GC-II Audit 094 — Minimal Capability-State Quotient Collision

## Scope

This audit follows the exact history-state compilation result in Audit 093. It tests whether the quotient of histories by equality of all future operational consequences can itself serve as a novel GC-II invariant.

## Candidate

Let H be the set of admissible histories. For histories h,h', define

h ~_C h'

iff for every admissible continuation policy pi, every remaining typed budget b=(R,I,A,L), every task/scale/error query, and every finite continuation horizon, the induced attainable outcome/error laws coincide.

Call K_C = H/~_C the exact capability-state quotient.

## Theorem 094.1 — Quotient sufficiency and coarsest exactness

STATUS: PROVED.

Assume the continuation semantics are well-defined on histories. Then:

1. The class [h]_C is sufficient for every continuation question included in the definition of ~_C.
2. Any exact state representation phi:H->Z that preserves all of those continuation semantics refines ~_C: phi(h)=phi(h') implies h~_C h'.
3. Hence K_C is the coarsest partition of histories preserving the specified complete continuation semantics, unique up to relabeling of equivalence classes.

Proof. (1) is immediate because all members of a class have identical continuation semantics. For (2), if phi(h)=phi(h') but h and h' differ under some admissible continuation, then phi cannot be an exact sufficient operational state. Thus equality under phi implies h~_C h'. Item (3) follows because every exact representation refines the quotient. QED.

This theorem is mathematically valid, but its form is a generic quotient-by-future-behavior construction.

## Theorem 094.2 — Recursive update under right-congruence

STATUS: PROVED / CONDITIONAL ON SEMANTIC CLOSURE.

If equivalent histories remain equivalent after appending the same admissible action-observation symbol whenever that extension is defined, then ~_C is a right congruence and there is a well-defined recursive update

U([h]_C, y) = [hy]_C.

Proof. Right-congruence makes the right-hand side independent of the representative h. QED.

If right-congruence fails because the continuation boundary silently depends on information omitted from h, the remedy is to enlarge the history/state description; failure alone is not a new capability law.

## Collision result

STATUS OF `minimal capability-state quotient as standalone GC-II novelty`: FALSIFIED.

The construction collides with several mature ideas:

- Myhill–Nerode style future-equivalence: histories/strings are quotiented when no continuation distinguishes them, yielding a canonical minimal state representation in automata theory.
- Computational mechanics causal states: past histories are grouped when they induce the same conditional distribution over futures; causal states are minimal sufficient predictive statistics and admit recursive state updates.
- Predictive-state representations: controlled systems can be represented through predictions of future observable tests rather than latent histories.
- MDP/process bisimulation and state abstraction: states are identified when their future operational behavior is equivalent (or approximately equivalent), with quantitative bisimulation metrics supplying approximate variants.
- Minimal sufficient robot-brain formulations explicitly seek the weakest internal transition system sufficient for passive and active tasks over action/observation histories.

Therefore naming H/~_C a `Generative capability state` does not create a distinct theorem. Its minimality follows from the equivalence relation itself and is structurally the same canonical-quotient move used in these areas.

## Important non-result

The cardinality or entropy of K_C is not automatically a new No-Free-Capability law. A lower bound such as memory >= log2 |K_C| is an encoding/counting statement only after the representation model, exactness criterion, coding assumptions, and accessibility requirements are fixed. Similar memory/state-complexity interpretations already occur in automata, computational mechanics, control, and robotics.

## What survives

The next defensible target is not another complete behavioral quotient. It is a **typed constrained realization theorem**:

Given a fixed operational boundary and a required exact/epsilon-approximate capability semantics, characterize the Pareto-minimal physical/computational resources needed to *realize* an adequate recursive state representation, while keeping representation cost distinct from task-execution cost.

A candidate object is the realization region

M_X(epsilon) = Pareto { (R_mem, I_update, A_access, L_latency) : exists recursive representation Z preserving the specified capability semantics to error <= epsilon }.

This is only a DEFINITION / OPEN candidate. It must be collision-tested against minimal automata, rate-distortion and information bottleneck, predictive rate-distortion, epsilon-machines/statistical complexity, bisimulation compression, sufficient MDP abstractions, communication complexity, streaming-space lower bounds, and minimally sufficient robot brains. No novelty is claimed.

## Breakthrough gate

A Paper-II advance would require a theorem about M_X(epsilon) that is not merely:

- cardinality of a canonical quotient;
- entropy of a predictive state;
- ordinary lossy compression/rate-distortion;
- a standard memory/query/communication lower bound;
- bisimulation/state-abstraction error;
- or a relabeling of a known resource tradeoff.

The strongest candidate would couple typed realization resources to operational capability loss through a proved bound that survives those reductions and has a finite exact witness where existing scalar/standard summaries provably cannot recover the bound.

## Status table

- exact capability-state quotient sufficiency: PROVED
- coarsest exact partition property: PROVED
- recursive update: PROVED conditional on right-congruence / semantic closure
- minimal quotient as standalone GC-II novelty: FALSIFIED
- quotient cardinality as new No-Free-Capability theorem: FALSIFIED as a standalone claim
- typed constrained realization region M_X(epsilon): OPEN
- quantitative non-imported realization/capability law: OPEN

## Scientific conclusion

Audit 093 removed path dependence as a novelty source. Audit 094 now removes the immediate fallback of declaring the minimal future-equivalence quotient itself to be the breakthrough. GC-II must move one level deeper: from canonical behavioral state compression to a genuinely new, typed, constrained realization law—or abandon this route if that law reduces to established compression, abstraction, or complexity theory.
