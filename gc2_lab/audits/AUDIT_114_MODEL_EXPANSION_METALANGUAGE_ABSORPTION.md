# GC-II Audit 114 — Model-Expansion Metalanguage Absorption

## Question
Can the post-Audit-113 target — the minimum typed cost of acquiring a genuinely new generator/primitive whose semantics is not latent in the original operational closure — supply a standalone GC-II breakthrough quantity?

## Result
**Not in its generic finite/effective form.** Once a fixed external realization metalanguage is declared, internal non-definability and external acquisition separate sharply. A primitive may be absent from the internal closure while still being finitely describable, transmissible, synthesized, queried, or implemented from the external metalanguage. The cost of obtaining it then reduces to established description, program-synthesis, oracle/query, library-learning, or resource-transfer questions.

Let L be an internal generator library, Cl(L) its extensional closure under the declared composition rules, M a fixed external effective metalanguage with interpreter U_M, and p a candidate primitive.

Call p **internally new** when

p notin Cl(L).

Call p **externally describable** when there exists a finite code sigma such that

U_M(sigma; L) = p

under the declared extensional semantics.

Define the conditional description acquisition cost

D_M(p | L) = min{|sigma| : U_M(sigma; L)=p}.

### Theorem 114.1 — Metalanguage absorption
If p has a finite exact description sigma in the fixed external effective metalanguage M, then the expansion L -> L union {p} can be simulated by retaining L and supplying sigma together with the fixed interpreter U_M. The additional description overhead is at most

D_M(p | L) + c_M,

where c_M is the fixed interpreter/compiler overhead independent of p.

### Proof
By hypothesis there exists sigma with U_M(sigma;L)=p. Any use of p in the expanded system can therefore be replaced by invocation of U_M on sigma and the same arguments/context. The interpreter is fixed once M is fixed, so its encoding contributes only a p-independent constant c_M. Hence acquisition of p is representable as acquisition of finite side information/program text plus execution overhead. QED.

**Status: PROVED under the stated effective-description and exact-semantics assumptions.**

### Corollary 114.2 — Internal novelty is relative, not absolute
p notin Cl(L) does not imply that p is unavailable to the external realization model. It only establishes that p is not term-definable from the chosen internal basis. A positive scalar based solely on non-membership in Cl(L) measures basis-relative expressivity expansion.

**Status: PROVED.**

### Corollary 114.3 — Description-complexity collision
If Omega_G for model expansion is defined as the shortest exact external description needed to add p, then, up to the fixed choice of universal description language/interpreter, it is a conditional description/Kolmogorov-style complexity quantity rather than a new capability invariant. For universal effective description systems, standard invariance results already imply machine dependence only up to an additive compiler constant.

**Status: IMPORTED/KNOWN collision; not claimed as a new GC-II theorem.**

### Corollary 114.4 — Oracle collision
If p is not provided by finite code but is made available only through input-output access, then the expansion is naturally modeled as oracle access. The cost question moves to query/oracle complexity or identification/sample complexity depending on the interface.

**Status: IMPORTED/KNOWN collision.**

## Exact finite audit
A checker enumerates all 16 Boolean functions f:{0,1}^2->{0,1}. The internal library consists of projections x,y, constants 0,1, and AND/OR, closed under composition. Its two-variable extensional closure contains exactly 6 monotone Boolean functions. Therefore 10 Boolean functions are genuinely outside this internal closure.

However, a fixed external truth-table metalanguage describes every two-input Boolean primitive in exactly 4 bits. Thus all 10 internally new primitives are externally finitely describable despite being absent from the internal basis closure.

This is not evidence for a new law; it is a kill test demonstrating that **closure escape and acquisition cost are different notions**.

Exact result:
- total Boolean functions: 16
- internal extensional closure size: 6
- functions outside internal closure: 10
- externally truth-table describable outside functions: 10/10
- external exact table code length: 4 bits per function

**Status: EXACT FINITE ENUMERATION.**

## Prior-art collision gate
1. **Clone theory / Post lattice.** Closure of primitive operations under superposition and the effect of adding operations are classical universal-algebraic expressivity questions. Boolean clones are completely classified by Post's lattice. Therefore 'primitive outside the generated closure' is not by itself a new mathematical mechanism.
2. **Algorithmic information / description complexity.** Shortest effective descriptions, conditional descriptions, universal interpreters, and invariance up to additive constants are established machinery. Therefore a shortest-description Omega_G collides directly with algorithmic information theory.
3. **Program synthesis / library learning.** DreamCoder, Stitch, LILO, Leroy and related systems explicitly grow libraries of reusable program components/abstractions to improve future synthesis. Therefore acquisition of reusable primitives from solved tasks is already an active established research program.
4. **Oracle/query complexity.** If the new primitive is available only as an external callable black box, standard oracle computation and query complexity already model the gain in computational power/cost.
5. **Resource-theory catalysis.** If an auxiliary resource enables a conversion while remaining available or approximately returned, catalytic resource transformations are established; merely renaming the auxiliary enabler as a 'new capability primitive' does not avoid that collision.

## Trilemma for the surviving route
For a proposed genuinely new primitive p under a fixed realization boundary, exactly one of the following broad cases must be defended:

1. **Finite effective description:** p can be finitely encoded in the declared metalanguage. Then generic acquisition reduces to description/program transfer plus realization cost.
2. **Black-box access:** p is available only through calls/experiments. Then generic acquisition reduces to oracle/query/identification structure.
3. **No finite effective description and no reproducible access model:** then p cannot be exactly implemented and independently reproduced by the finite software/experimental methodology required for GC-II, so it cannot presently support a validated computational breakthrough claim.

This trilemma does not rule out new science. It rules out claiming novelty merely from the phrase 'acquire a genuinely new primitive.' A viable GC-II theorem must add a quantitative structure not absorbed by these established models.

## Edge/domain checks
- If p already lies in Cl(L), model expansion is semantically redundant although it may shorten programs or reduce execution cost.
- If p is extensionally new but syntactically equivalent under another encoding, only the internal presentation changed.
- If approximation is allowed, D_M must include the error/tolerance semantics; exact and approximate acquisition cannot be conflated.
- If execution time, energy, memory, communication, embodiment, or interface access matters, description length alone is insufficient; those typed realization costs must be modeled independently.
- If M changes with p, the description measure becomes vacuous because the new primitive can be hidden in the interpreter. M must be fixed independently.
- Universal-language invariance is only up to an additive machine/compiler constant; it does not make finite small-instance values canonical.
- Kolmogorov complexity is not computable in general, so it cannot by itself serve as an exact executable GC-II accounting observable for arbitrary primitives.
- A finite truth table is practical only for finite domains; infinite/continuous primitives require a declared representation, approximation, oracle, or computability model.

## Status ledger
- Internal primitive novelty p notin Cl(L): **FORMALIZED / IMPORTED-KNOWN expressivity notion**.
- Metalanguage absorption theorem: **PROVED under effective finite-description assumptions**.
- Internal non-definability implying external indescribability: **FALSIFIED**.
- Shortest-description model-expansion Omega_G as standalone GC-II novelty: **FALSIFIED / COLLIDES with algorithmic information**.
- Black-box primitive acquisition as standalone novelty: **FALSIFIED / COLLIDES with oracle-query models**.
- Library growth as standalone novelty: **FALSIFIED / COLLIDES with program synthesis and library learning**.
- Existence of a typed, realization-sensitive expansion invariant beyond description/query/synthesis/resource-transfer reductions: **OPEN**.

## Stronger surviving target
The next viable route must keep the external realization boundary fixed and simultaneously account for at least two layers that cannot be collapsed into one another:

1. **semantic acquisition:** what new extensional operation/interaction becomes available; and
2. **realization burden:** the irreducible typed cost of physically/operationally instantiating that semantics under fixed interface, locality, information, resource, and error constraints.

The next kill test should ask whether a candidate joint invariant is merely a standard multi-resource convertibility problem. A genuine GC-II advance would require a theorem coupling semantic expansion to realization cost in a way that is invariant under basis/refactoring and is not derivable from clone theory, conditional description complexity, oracle/query complexity, program synthesis, communication complexity, or generic resource monotones.

No GC-II breakthrough is claimed by this audit.