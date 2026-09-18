# GC-II Audit 231 — Operational payload axioms collapse to directed cost geometry

Status: **PROVED boundary / IMPORTED-KNOWN collision / No-Free positivity OPEN**

## Question

Audit 230 showed that behavioral invariance alone cannot select a canonical payload. The next candidate is to derive payload from operational transformation cost rather than description syntax.

Let Q be the behaviorally quotiented operational state space. Let P(x,y) be the set of admissible finite protocols transforming x into y. Each protocol pi has cost c(pi) in [0,infinity]. Assume only:

1. identity: an empty protocol x->x exists with cost 0;
2. nonnegative cost;
3. sequential composability: if pi:x->y and rho:y->z are admissible then rho∘pi:x->z is admissible;
4. subadditive composition cost: c(rho∘pi) <= c(pi)+c(rho).

Define the intrinsic operational payload

    d(x,y) = inf { c(pi) : pi in P(x,y) },

with inf(empty)=infinity.

## Theorem 231.1 — Operational-cost closure theorem

Under assumptions 1–4,

    d(x,x)=0,
    d(x,z) <= d(x,y)+d(y,z).

Hence (Q,d) is an extended directed pseudometric (equivalently, a Lawvere cost space under the standard order convention).

### Proof

Identity gives d(x,x)<=0 and nonnegativity gives d(x,x)>=0. For finite d(x,y), d(y,z), choose epsilon-optimal protocols pi and rho. Composition gives

    d(x,z) <= c(rho∘pi)
           <= c(pi)+c(rho)
           <= d(x,y)+d(y,z)+2 epsilon.

Let epsilon->0. Infinite cases are immediate. QED.

No finiteness, symmetry, reversibility, convexity, Markov property, additivity, or deterministic dynamics is required.

## Corollary 231.2 — Candidate payload axioms are not GC-specific

Identity + nonnegative operational cost + sequential composition + infimal realization recover established directed cost geometry. Therefore these axioms cannot by themselves constitute a GC-II novelty claim.

## Theorem 231.3 — These axioms do NOT imply No-Free-Capability positivity

The implication

    x != y  =>  d(x,y)>0

is false under assumptions 1–4.

Counterexample A: Q={x,y}; include transformations x->y of cost 1/n for every n>=1. Then d(x,y)=0 although x!=y.

Counterexample B: include a literal zero-cost transformation x->y. Again d(x,y)=0.

Therefore a theorem of the form

    genuine capability escape => strictly positive payload

requires an additional separation/coercivity/discreteness axiom, or a physically justified lower bound on nontrivial operations. Positivity cannot be obtained from composition alone.

## Reversibility candidate

Define

    Gamma_rev(x,y)=d(x,y)+d(y,x).

This is nonnegative and symmetric, but is not a novel invariant: it is the standard symmetrization of a directed cost. Moreover Gamma_rev(x,y)=0 need not imply x=y without separation. A ratio d(x,y)/d(y,x) is ill-defined on zero denominators and unstable near zero.

Status: generic reversibility-gap-from-directed-cost route **IMPORTED/KNOWN**, not GC-specific.

## Dimensional and edge-case audit

- d has exactly the units of c.
- unreachable transformations have d=infinity.
- identity has zero cost.
- zero-cost cycles are allowed by the weak axioms.
- composition obeys triangle inequality, not necessarily equality.
- quotienting presentations before defining d removes purely syntactic duplication but does not enforce separation.
- parallel composition has no law here; imposing additivity/max/subadditivity would be an extra axiom and must be justified operationally.
- monotonicity under enlargement of the admissible protocol set holds: adding protocols can only decrease d.

## Prior-art collision

Lawvere metric/cost spaces are precisely the established structure obtained from [0,infinity]-valued directed costs with zero identity and triangle inequality. Resource convertibility represented by monoidal preorders and quantitative cost enrichment is also established compositional mathematics. Therefore Theorem 231.1 is retained as a boundary lemma, not claimed as a new mathematical theorem.

## Ledger

| Candidate | Status |
|---|---|
| Infimal admissible transformation cost d | PROVED well-defined extended cost |
| Identity + composition => directed triangle inequality | PROVED / IMPORTED-KNOWN structure |
| Operational axioms select a GC-specific payload | FALSIFIED as novelty |
| Weak operational axioms imply d(x,y)>0 for genuine change | FALSIFIED |
| Gamma_rev=d(x,y)+d(y,x) as generic reversibility gap | IMPORTED/KNOWN |
| GC-I projection irreducibility forces positive d after behavioral quotient | OPEN |
| Physically/operationally justified separation axiom derived from GC-I | OPEN |

## Consequence for Paper II

The next viable No-Free-Capability route cannot merely axiomatize cost composition. It must prove that GC-I proper-projection irreducibility forces a *separation property* for a carefully specified operational cost: some class of globally irreducible capability changes must remain at positive directed distance from their source even after all behaviorally equivalent presentations and zero-cost free transformations are quotiented out. That claim must then be collision-tested against resource-theory monotones, simulation distances/deficiencies, and enriched-category separation/completion before being treated as novel.
