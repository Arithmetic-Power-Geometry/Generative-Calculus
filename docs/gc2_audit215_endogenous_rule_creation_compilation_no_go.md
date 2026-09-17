# GC-II Audit 215 — endogenous rule creation compilation no-go

## Question
Audit 214 leaves endogenous creation of admissible rules as a possible source of generative information not visible in minimum-cost closure.  Does finite endogenous rule creation, by itself, escape ordinary first-order transition semantics?

## Setup
A finite endogenous-rule system is

H = (X,Q,A,T,c),

where X is the physical/semantic state set, Q is a finite set of rulebooks (or admissibility regimes), A is the action alphabet, and

T : X x Q x A -> X x Q

is a partial deterministic transition map.  A transition may change q, so at the object description level the system can create/delete/modify which transformations are subsequently admissible.  Let c(x,q,a) >= 0 be any transition cost.  Nondeterministic systems use a transition relation and the same construction below.

## Theorem 215.1 — configuration-state compilation
Define the ordinary first-order state space S = X x Q and compiled transition map

D((x,q),a) = T(x,q,a)

where defined, with compiled cost c_D((x,q),a)=c(x,q,a).

Then for every initial configuration s0 and every finite action word w:

1. w is executable in H iff it is executable in D;
2. the complete configuration trace is identical;
3. every prefix accumulated cost is identical;
4. therefore every budgeted reachable set in configuration space is identical;
5. any observation map h:X x Q -> O yields identical observable traces after compilation.

### Proof
Induct on |w|.  Length zero is immediate.  Assume equality after prefix u at configuration s.  For the next action a, H permits exactly T(s,a), while D was defined to permit exactly D(s,a)=T(s,a), and assigns the same edge cost.  Hence the next configuration and accumulated cost agree.  Induction gives all claims.  For nondeterministic T, replace equality of next states by equality of successor sets and induct on the trace tree.  QED.

## Corollary 215.2 — rule-creation-only novelty no-go
No invariant depending only on finite execution behaviour, full configuration traces, costs, or budgeted configuration reachability can distinguish finite endogenous rule creation from its first-order compiled transition system if arbitrary configuration-state augmentation is allowed.

Thus `new rules appeared during execution` is not, by itself, a representation-invariant Generative Novelty Gap.

## Important boundary
This theorem does **not** show that rule generation is operationally irrelevant.  It shows that novelty cannot rest on the syntactic distinction between `changing rules` and `changing state`.  A surviving GC-II quantity must impose an independently justified representation/resource restriction and measure the cost of compilation, e.g. bounded state/memory, locality, interface constraints, description length, online information, or translator complexity.  For unbounded/generated rule languages, S may be infinite and compilation may incur decisive representation or computational overhead; Audit 215 makes no free-efficiency claim.

## Exact collision test
`experiments/gc2_audit215_endogenous_rule_compilation.py` exhausts all 2^8 = 256 deterministic systems in a 2-world x 2-rulebook x 2-action family and checks every initial configuration and every action word through length four.  It verifies exact trace and accumulated-cost equality with the compiled first-order system.  This finite experiment illustrates the theorem; the theorem itself is structural and does not depend on enumeration.

## Prior-art collision
This compilation is not claimed as novel.  It is the standard configuration-state move used throughout transition-system semantics.  More specifically, reflective rewriting logic represents rewrite theories and terms at the metalevel: Maude's universal theory can represent a pair (R,t) and simulate R-rewriting as rewriting of that represented pair.  Dynamic epistemic logic likewise uses product update, whose updated worlds are world-event pairs.  These are strong warnings that `rules/actions become state` is established machinery rather than a GC-II invention.

## Status ledger
- Configuration-state compilation theorem: **PROVED**.
- Exact preservation of traces and transition costs: **PROVED**.
- Preservation of budgeted configuration closure: **PROVED**.
- Finite endogenous rule creation as an intrinsic Omega_G merely because rules change: **FALSIFIED**.
- State/product/metalevel representation mechanism: **IMPORTED/KNOWN**.
- Efficient compilation under bounded representation/resources: **OPEN**.
- Lower bound on compiler/translator overhead forced by GC-I projection irreducibility: **OPEN** and now the strongest route.

## Consequence for Paper II
Audit 214's surviving direction must be refined.  Path provenance or rule provenance is scientifically useful only if GC-II specifies which provenance distinctions cannot be compiled away within the allowed operational budget.  The next target should therefore be a **resource-bounded endogenous-rule compilation gap**: minimum memory/description/communication/locality overhead required for a fixed-rule simulator to reproduce a rule-generating system under the same external interface.  That target connects directly to the requested local-to-global translator lower bound and admits exact finite adversarial searches.
