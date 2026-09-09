# GC-II Budget-Truncation Bound Audit 022

## Scope

This audit attacks the open target left by Audit 021: whether GC accounting primitives can certify a finite future horizon without enumerating the full reachable quotient. GC-I on `main` is untouched. The result below is deliberately classified as a restricted theorem and novelty boundary, not a breakthrough claim.

## Setting

Let a deterministic operational world have a nonnegative vector budget `B=(B_1,...,B_k)`. Every admissible nonterminal transformation `e` consumes `c(e) in R_+^k`. Assume:

1. **No replenishment:** residual budget is componentwise nonincreasing along every execution.
2. **Uniform progress certificate:** there exists a weight vector `w in R_+^k` and `epsilon>0` such that `w·c(e) >= epsilon` for every nonterminal admissible transformation.
3. **Budget feasibility:** an execution is admissible only while cumulative consumption is componentwise at most `B`.
4. Zero-cost administrative/stuttering steps have already been quotiented out, or are terminal; otherwise no finite bound follows from budget alone.

Define the scalar potential `V(b)=w·b` for residual budget `b`.

## Theorem — budget-induced truncation

**Status: PROVED in the stated specialization / IMPORTED-KNOWN mechanism.**

Every admissible execution contains at most

`H_B = floor((w·B)/epsilon)`

nonterminal transformations.

Consequently, if future-capability equivalence compares all feasible continuations under the same represented task/scale/error/interface/rule semantics, agreement through depth `H_B` is exact all-future agreement: there are no longer feasible continuations to inspect.

### Proof

For an admissible execution `e_1...e_h`, feasibility gives

`sum_j c(e_j) <= B`

componentwise. Multiplying by nonnegative `w` preserves the inequality:

`sum_j w·c(e_j) <= w·B`.

By the progress assumption, the left side is at least `h epsilon`. Hence

`h epsilon <= w·B`,

so `h <= floor((w·B)/epsilon)`. Therefore no feasible continuation exceeds `H_B`, and equality of represented behavior on all continuations of length at most `H_B` is equality on all feasible continuations. QED.

## Coordinate form

If every nonterminal transformation consumes at least `epsilon_i>0` in one fixed resource coordinate `i`, choose `w=e_i` and obtain

`H_B <= floor(B_i/epsilon_i)`.

More generally, selecting `w` is a certificate problem: any nonnegative `w` satisfying `w·c(e)>=1` for all admissible nonterminal transformations yields `H_B <= floor(w·B)`. Minimizing `w·B` over such `w` gives the strongest bound available from this linear potential family.

## Critical edge cases and falsifications

- **Zero-cost productive cycles:** if a capability-changing cycle has zero `w`-cost, the theorem fails. Budget alone then cannot truncate future depth.
- **Replenishment:** if transformations can regenerate counted resources, residual potential need not decrease; the proof fails unless a different well-founded potential is supplied.
- **Negative costs/credits:** excluded. Allowing them destroys the monotone-potential argument unless cycles are controlled.
- **Unbounded information/action/rule creation at fixed counted cost:** the depth bound still holds if each generating transformation pays `epsilon`, but it does not bound branching factor or quotient size.
- **Continuous Zeno costs:** if positive costs have no uniform lower bound, infinitely many transformations can fit under finite budget; `epsilon>0` is essential.
- **Stuttering:** arbitrary zero-cost no-op steps make syntactic trace length unbounded but do not matter after quotienting by operational equivalence.
- **Multiple budgets:** a componentwise finite budget is not enough by itself; the progress certificate must hit every nonterminal transformation.

## Composition and monotonicity

`H_B` is monotone in `B` under componentwise budget increase. For concatenated executions, weighted consumption is additive even though capability effects need not commute. Thus the theorem does **not** assume path-independent capability, commutation of R/I/A/L transformations, or additive capability value; it uses additivity only of the certified consumed accounting quantity along a trace.

If budgets are concatenated as `B+B'`, the certificate gives `H_{B+B'} <= floor((w·B+w·B')/epsilon)`. Floor effects prevent exact additivity but give the expected sub-one rounding discrepancy.

## Relation to Omega_G and closure escape

This theorem does not define novelty. It supplies a finite certificate horizon for evaluating a trace-sensitive `Omega_G` or future-capability distortion when the assumptions hold. In particular, it does not imply that capability is a function only of aggregate `(Delta R,Delta I,Delta A,Delta L)`; Audit 016 already falsified that stronger claim in noncommuting worlds.

## Novelty boundary

The mechanism is a ranking-function / decreasing-potential argument familiar from termination proofs, bounded planning, shortest-path/resource-constrained reachability, and amortized analysis. The linear certificate can also be viewed as a simple dual weighting of resource-consumption vectors. Therefore **the bound `floor((w·B)/epsilon)` is not claimed as a GC-II breakthrough**.

The useful GC-II frontier is stronger: derive a nontrivial well-founded potential from coupled endogenous changes in resources, information, interfaces/actions, rules, and task-scale-error feasibility even when individual channels can replenish or expand. A genuine candidate should survive cases where no fixed nonnegative linear `w` decreases on every productive step.

## Next exact target

Search finite endogenous worlds for a **capability Lyapunov/ranking functional** `Psi_G(state,budget,envelope)` satisfying a strict decrease on every future-distinguishing transformation while permitting local R/I/A/L replenishment. Then test whether the induced horizon or accounting inequality is invariant under operational equivalence and whether it reduces to known ranking/supermartingale/resource-monotone constructions. If it does, classify IMPORTED/KNOWN; if the whole-envelope coupling is essential and yields a new quantitative consequence, promote only after collision checks.

## Status update

- Generic finite quotient horizon `N-1`: PROVED / IMPORTED-KNOWN (Audit 021).
- Budget-only horizon under no replenishment + uniform positive progress: PROVED / IMPORTED-KNOWN.
- Budget-only finite horizon without a progress/well-foundedness assumption: FALSIFIED by zero-cost productive cycles / Zeno-cost families.
- GC-specific truncation under endogenous replenishment and coupled R/I/A/L transformations: OPEN.
