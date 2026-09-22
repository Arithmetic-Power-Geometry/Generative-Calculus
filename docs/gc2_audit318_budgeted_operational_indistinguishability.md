# GC-II Audit 318 — Budgeted operational indistinguishability closure

## Status

- Budgeted operational closure model with explicit transformations/resources/information/interfaces/rules: **FORMALIZED**.
- Budgeted indistinguishability equivalence under deterministic adaptive policies: **PROVED**.
- Closure-Escape equivalence (decision separation iff some admissible policy separates the relevant equivalence class): **PROVED but IMPORTED/KNOWN in mechanism**.
- No-free-capability consequence under unchanged admissible policy set: **PROVED but essentially monotonicity/reachability**.
- Claim of foundational novelty: **NOT MADE**.
- Stronger theorem beyond active testing/POMDP/reachability/experiment comparison: **OPEN**.

## 1. Operational specification

A finite budgeted operational specification is

`O=(X,U,Y,T,Z,c,R,I,A,L)`

where:

- `X` is the finite latent operational-state set;
- `U` is the primitive transformation/action alphabet;
- `Y` is the observation alphabet;
- `T_u:X->X` is the deterministic state transformation induced by action `u` (stochastic kernels can be added later);
- `Z_u:X->Y` is the observation returned after applying `u`;
- `c(u,x)>=0` is the resource charge of action `u` in state `x`;
- `R>=0` is the total resource budget;
- `I` is the initially admissible information available to the policy;
- `A subseteq U` is the exposed interface/action set;
- `L` is the rule predicate deciding whether a history/action extension is admissible.

A finite history is `h_t=(i,u_1,y_1,...,u_t,y_t)` with `i in I`. An adaptive policy `pi` maps admissible histories to either an action in `A` or `STOP`. A policy is `O`-admissible from state `x` when every realized prefix satisfies `L` and cumulative cost is at most `R`.

Let `Pi(O)` be the set of policies admissible for every state still compatible with their current history. This uniform requirement prevents a policy from presupposing the hidden state in order to justify an action.

For `pi in Pi(O)`, let `Tr_pi(x)` denote the complete action/observation transcript generated from `x`, including termination.

The budgeted operational closure is the transcript family

`Cl(O,x)={Tr_pi(x): pi in Pi(O)}`.

This is a typed object: physical resource units appear only in `c,R`; information is represented by histories/transcripts; actions by `A`; admissibility by `L`. No dimensional addition of these quantities is used.

## 2. Budgeted operational indistinguishability

Define

`x ~_O x'`

iff

`Tr_pi(x)=Tr_pi(x')` for every `pi in Pi(O)`.

### Proposition 318.1

`~_O` is an equivalence relation.

**Proof.** Reflexivity and symmetry are immediate from transcript equality. If `x~_O x'` and `x'~_O x''`, then every admissible policy has equal transcript on the first pair and on the second pair, hence equal transcript on `x,x''`; therefore `x~_O x''`. QED.

Thus `O` induces a quotient `X/~_O` consisting exactly of operationally distinguishable classes under the stated budget, information, interfaces and rules.

## 3. Decision resolution

Let `d:X->D` be an independently fixed required downstream decision.

Call `d` **resolved by O** when there exists `pi in Pi(O)` and decoder `g` on its terminal transcript such that

`g(Tr_pi(x))=d(x)` for every `x in X`.

### Theorem 318.2 — finite budgeted closure criterion

A necessary condition for exact resolution is

`x ~_O x' => d(x)=d(x')`.

If `Pi(O)` contains a single policy `pi*` whose transcript separates every pair of distinct `~_O` classes, the condition is also sufficient.

**Proof (necessity).** If `x~_O x'`, every admissible policy produces the same transcript on both states. A decoder receiving that transcript cannot return two different required decisions.

**Proof (sufficiency under the stated joint-separation hypothesis).** Define `g` on each terminal transcript of `pi*` as the common decision value of its compatible states. The hypothesis and class-homogeneity make this well-defined. QED.

The joint-separation hypothesis is essential: pairwise existence of distinguishing policies does not by itself imply that one budget-feasible policy can combine all distinctions. This blocks a common but invalid quantifier swap.

## 4. Closure escape

For an extension `O -> O'`, say that it is **uncharged** only when `Pi(O')=Pi(O)` and the transcript semantics of every old policy are unchanged. Otherwise the extension changes at least one operationally charged component (resource budget/cost law, admissible information, exposed interfaces/actions, transformation/observation law, or rules).

### Corollary 318.3 — no escape without operational change

If `x~_O x'` and `d(x)!=d(x')`, then no uncharged extension can resolve `d`.

**Proof.** Under an uncharged extension the admissible transcript family is identical, so `x~_{O'}x'`. Apply Theorem 318.2. QED.

This is a precise no-free-capability statement for this finite model, but it is deliberately not advertised as a novel theorem: once closure is defined by admissible experiments/policies, invariance under an unchanged policy/transcript family is close to definitional.

## 5. Monotonicity checks

If `Pi(O) subseteq Pi(O')` and every old policy keeps the same transcript semantics, then

`~_{O'} subseteq ~_O`.

So adding admissible experiments can split indistinguishability classes but cannot merge classes. Conversely, restricting policies can merge classes but cannot split them.

Increasing `R` is monotone only when `L`, action semantics and all other admissibility conditions are unchanged. Adding an interface is monotone only when old interfaces remain available. Adding information is monotone only when policies may ignore it. These qualifications are required; otherwise a nominal increase can simultaneously alter rules and destroy old policies.

## 6. Edge and degenerate cases

- If `Pi(O)` contains only `STOP`, all states sharing initial information are indistinguishable.
- If one zero-cost admissible action reveals the state exactly, every state is separated in one step.
- If `R=0`, positive-cost actions are unavailable, but zero-cost actions may remain admissible.
- If `d` is constant, it is resolved even when all states are operationally indistinguishable.
- Infinite looping zero-cost policies are excluded here by requiring finite terminating transcripts; relaxing this needs an explicit omega-trace semantics.
- State-dependent admissibility cannot be exploited by a policy unless admissibility itself is observable/justifiable from the current compatible history; this is why `Pi(O)` uses uniform branch admissibility.

## 7. Counterexample to a tempting stronger claim

**False claim:** `d` is resolvable iff every pair with different decisions can be separated by some budget-feasible policy.

Pairwise distinguishability does not guarantee a single adaptive policy that jointly resolves all decision classes within the same budget. Different pairs may require mutually exclusive experiments whose combined cost exceeds `R`. Therefore the converse in Theorem 318.2 is stated only under a joint-separating policy condition.

A minimal pattern is three states with two one-bit tests, each costing one, budget `R=1`: test `a` separates state 1 from 2 but not 3; test `b` separates state 1 from 3 but not 2. Pairwise witnesses can exist across a family while no single one-test policy identifies all three. Any stronger equivalence must encode adaptive decision-tree feasibility rather than pairwise separation alone.

## 8. Relation to Audit 317

Audit 317 assumed a decision-confusability graph externally. Audit 318 supplies an operational source for residual confusability: states inside one `~_O` class cannot be separated by any admissible policy. For a required decision `d`, an obstruction is therefore witnessed directly by

`exists x,x': x~_O x' and d(x)!=d(x')`.

This removes one degree of arbitrariness from the translator bridge, but the decision map `d` is still externally specified. A genuinely stronger GC-II theorem would need the relevant decision/capability witness to arise from conversion structure itself rather than being selected after the fact.

## 9. Prior-art collision audit

The mechanism overlaps established finite-state experiment distinguishability, adaptive testing, reachability/viability, automata observational equivalence, POMDP belief-state refinement, Blackwell-style experiment comparison, and zero-error decision/communication theory. Consequently:

- observational equivalence under an experiment family: **IMPORTED/KNOWN**;
- monotone refinement when experiments are added: **IMPORTED/KNOWN**;
- impossibility of deciding differently on observationally equivalent states: **IMPORTED/KNOWN**;
- finite adaptive-policy formulation as GC-II bookkeeping: **VALID but not claimed novel**.

No breakthrough claim is made from this audit.

## 10. Next attack

The missing non-tautological target is now sharp: define a conversion capability functional from the operational transformation system itself, then prove that escaping a budgeted closure forces a quantitatively nonzero change in at least one charged component. Candidate route: formulate the minimum charged extension required to split a conversion-critical `~_O` class and compare it against directed deficiency / active experiment design. Any candidate must survive reductions to Blackwell-Le Cam deficiency, constrained reachability, adaptive distinguishing sequences, and resource-theoretic monotones before being labeled novel.