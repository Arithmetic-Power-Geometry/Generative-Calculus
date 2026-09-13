# GC-II Audit 113 — Future-Capability Set Collapse

## Question
Can the post-Audit-112 target—two systems matched for present traces and conventional computation/communication costs but with unequal horizon-h future-capability sets K_h(z,B)—supply a standalone GC-II invariant?

## Result
**Not if K_h is defined entirely by admissible continuations of the fully specified operational state.** In a Markovized/augmented operational model, the horizon-h future-capability set is a derived reachable/viable object. A difference in K_h is therefore either (i) already a difference in future transition semantics, (ii) caused by omitted state/context, or (iii) caused by a new intervention/resource model that must itself carry the novelty.

Let an operational system be S=(Z,A,E,c,O), where Z is the complete operational state, A(z) the admissible actions, E(z,a) the successor relation (possibly set-valued), c(z,a) a typed nonnegative cost vector, and O the observable/capability interpretation. For budget B and horizon h define recursively

K_0(z,B) = {O(z)}

K_{h+1}(z,B) = {O(z)} union Union_{a in A(z), c(z,a)<=B} Union_{z' in E(z,a)} K_h(z', B-c(z,a)).

(For stochastic models replace set-valued reachability by the declared distributional/risk semantics; the same definitional dependence on the complete kernel remains.)

### Theorem 113.1 — Augmented-state determination
If two pointed systems (S,z) and (S',z') are related by a budget-preserving labelled bisimulation that preserves O, admissible action labels, typed edge costs, and successor matching, then for every finite h and budget B,

K_h^S(z,B) = K_h^{S'}(z',B).

### Proof
Induction on h. At h=0 equality follows from preservation of O. Assume equality for h. Bisimulation supplies a cost- and label-matched successor in the other system for every admissible transition, and conversely. The residual budget is therefore identical, and the induction hypothesis makes the corresponding successor K_h sets equal. Taking the same unions yields equality at h+1. QED.

**Status: PROVED.**

### Corollary 113.2 — Separation diagnostic
If K_h differs, then no equivalence preserving the complete budgeted transition semantics can relate the pointed systems. Hence K_h does not create a distinction beyond that semantics; it exposes a distinction already present in the future transition structure.

**Status: PROVED.**

### Corollary 113.3 — State-augmentation collapse
Suppose apparent capability-set deformation depends on a finite hidden variable Gamma (rules, tool inventory, interface permissions, learned program, topology, etc.). Replacing state z by (z,Gamma) makes K_h an ordinary budgeted reachable-set functional of the augmented transition system. Thus finite endogenous deformation alone does not evade Audit 111.

**Status: PROVED under the stated finite/representable augmentation assumption.**

## Exact finite counterexample to the weak matching criterion
Present-trace matching is too weak. Consider states p and q with the same present observation 0 and the same zero-cost action a. From p, a reaches r with observation 1; from q, a reaches s with observation 0. At horizon 0, p and q have identical observations and zero communication/computation cost. At horizon 1,

K_1(p,0)={0,1}, while K_1(q,0)={0}.

The unequal future-capability sets are real, but the distinction is exactly the ordinary one-step transition/trace distinction. No new invariant is needed.

## Edge/domain checks
- h=0: K_h reduces to the current capability observation; theorem is immediate.
- Zero budget: only zero-cost transitions contribute; proof is unchanged.
- Degenerate no-action state: K_h remains {O(z)}.
- Cycles: finite-h recursion remains well-defined; infinite horizon requires a least/greatest fixed-point convention.
- Vector budgets: subtraction/order must be defined componentwise or by the declared feasible cone; theorem requires the bisimulation to preserve that budget structure.
- Nondeterminism: successor sets are matched in both directions.
- Stochasticity: ordinary set equality is insufficient if probabilities/risk matter; use a probability-preserving behavioural equivalence and define the corresponding distributional K object.
- Approximation/error: tolerance must be part of O/equivalence; otherwise equality claims are invalid.
- History dependence: include sufficient history/controller memory in augmented state; if no finite/computable sufficient state exists, this corollary does not establish a finite compilation.

## Prior-art collision gate
Reachable sets, viability kernels, controlled invariant sets, temporal/fixpoint semantics, and process equivalences already encode future possibilities of a transition/control system. Viability theory explicitly studies state-dependent control constraints and future viable evolution. Possible-futures/decorated-trace semantics likewise enrich traces with information about future behaviour. Therefore a horizon future-capability set, by itself, is not a new mathematical species.

## Consequence for Omega_G
Candidates of the form

Omega_G(z,z';h,B) = d(K_h(z,B), K_h(z',B))

are useful diagnostics, but they are not standalone GC-II novelty when d is applied to reachable/viable future sets determined by the complete operational transition model. Under the theorem's behavioural quotient Omega_G must be zero.

## Status ledger
- Recursive budgeted future-capability set K_h: **FORMALIZED**.
- Bisimulation invariance of K_h: **PROVED**.
- Unequal K_h under merely equal present observations/costs: **PROVED by finite counterexample**.
- K_h as standalone GC-II novelty beyond complete budgeted transition semantics: **FALSIFIED**.
- Finite endogenous deformation as escape from augmented-state semantics: **FALSIFIED under representable augmentation**.
- Infinite/noncomputable endogenous state as automatic novelty: **NOT ESTABLISHED; OPEN and must be collision-tested against infinite-state semantics/computability**.

## Stronger surviving target
The next route cannot merely ask what futures are reachable from a fully specified state. It must identify a capability-accounting quantity that is not a functional of one fixed operational transition model. A defensible candidate must compare **model expansion itself under a fixed external metalanguage/realization boundary**: the minimum typed cost of acquiring a genuinely new generator/primitive whose semantics is not already present as a latent transition, macro, hidden state, oracle, communication channel, or program in the original closure. The immediate kill test is whether this reduces to program synthesis, oracle/query complexity, description/Kolmogorov complexity, library learning, option discovery, or resource-theory catalysis.

No GC-II breakthrough is claimed by this audit.
