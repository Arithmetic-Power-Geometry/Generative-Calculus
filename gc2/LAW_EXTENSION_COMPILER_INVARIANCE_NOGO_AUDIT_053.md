# GC-II Audit 053 — Exact Compiler-Invariant Law-Extension Cost No-Go

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 052

## Target attacked

Audit 052 leaves open a law-extension deficiency: the minimum accounted cost for substrate S to emulate substrate T's future generator-realizer law under every admissible continuation after quotienting semantics-preserving interpreters. The strongest desired version would be (a) exact, (b) scalar, (c) nontrivial, and (d) invariant under semantics-preserving compiler changes while including structural/program-description or execution cost.

This audit proves that this combination is impossible for sufficiently universal computable substrates.

## Setup

Let U be a universal prefix description machine. For a finite semantic law object x, define the structural realization term

    K_U(x) = min{|p| : U(p)=x}.

More generally let Lambda_U(S->T) be any proposed law-extension scalar whose structural component dominates or exactly includes the minimum description length of a program implementing the target law on U.

A compiler-invariance requirement stronger than the ordinary invariance theorem would demand

    Lambda_U(S->T) = Lambda_V(S->T)

for every pair of semantics-preserving universal substrate descriptions U,V.

## Theorem 1 — Exact structural compiler invariance is impossible

For any universal machine U and any target law object x, construct a universal machine V_x with a distinguished short code that outputs x, while a disjoint prefixed code space simulates U. For example, choose a self-delimiting encoding with

    V_x(0) = x,
    V_x(1p) = U(p)

with ordinary prefix-coding details adjusted so the domain remains prefix-free. V_x is universal because it simulates U with fixed compiler overhead, but

    K_{V_x}(x) <= O(1),

whereas K_U(x) may be arbitrarily large as x ranges over incompressible objects for U.

Therefore no exact nonconstant structural cost based on minimum program description can be invariant under all semantics-preserving choices of universal compiler/substrate.

Status: PROVED by explicit universal-machine construction. Mechanism IMPORTED/KNOWN from the machine dependence and invariance theorem of Kolmogorov complexity.

## Corollary 1 — Quotienting interpreters cannot leave an exact absolute description cost

The classical invariance theorem gives only

    |K_U(x)-K_V(x)| <= c_{UV},

where the constant depends on the pair of universal machines, not on x. It does not yield exact equality. Hence an exact GC-II structural Omega term cannot simultaneously be an absolute semantic invariant and equal a shortest universal description length.

Possible repairs are only weaker objects, such as:

1. an equivalence class modulo O(1);
2. asymptotic rates where compiler constants vanish after normalization;
3. a cost relative to a physically frozen substrate/compiler;
4. Pareto accounting that explicitly includes compiler installation as part of the substrate boundary.

These are valid, but none creates a new absolute scalar merely by naming the term generative.

## Theorem 2 — Exact execution-cost invariance also fails generically

Even when semantic behavior is fixed, exact running-time/resource cost is representation/model dependent. Linear speedup permits fixed constant-factor acceleration in standard Turing-machine models under representation changes, and Blum speedup supplies computable functions for which no single asymptotically optimal program exists for broad Blum complexity measures.

Consequently an unrestricted exact scalar law-extension deficiency that mixes semantic equivalence with minimum execution cost cannot be fully compiler invariant over universal computational substrates.

Status: reduction to classical speedup results; IMPORTED/KNOWN mechanism.

## Combined no-go theorem

Assume a proposed law-extension scalar Lambda has all four properties:

(A) exact numerical value rather than an equivalence class/asymptotic rate;
(B) nontrivial dependence on shortest structural description and/or minimum execution cost;
(C) invariance under every semantics-preserving universal compiler/substrate representation;
(D) applicability to arbitrary computable law extensions.

Then A-D are mutually incompatible.

Proof: if Lambda contains a nontrivial shortest-description component, Theorem 1 violates exact compiler invariance. If it instead obtains nontriviality from unrestricted minimum execution cost, classical speedup phenomena violate an absolute representation-independent optimum in the general case. Removing both structural and execution dependence leaves Lambda extensional; Audit 052 and prior deficiency audits then reduce the object to ordinary operational equivalence/deficiency on the compiled transition system.

Status: PROVED conditional on the explicitly stated universality/generality domain; the ingredients are classical.

## Dimension/domain checks

- K_U is measured in bits; it must not be added directly to physical energy/time or typed R/I/A/L quantities without a declared conversion law.
- Compiler constants have units of description bits and do not disappear for finite exact comparisons.
- Normalized asymptotic rates can remove O(1) description ambiguity but change the object and can erase finite installation effects.
- A frozen physical machine permits exact costs, but then invariance is only under cost-preserving representations of that machine, not arbitrary universal compilers.
- Non-universal finite substrates escape the universal-machine construction but fall under Audit 052's finite explicit compilation boundary.
- Oracle/noncomputable law extensions import an undeclared capability unless the oracle is part of the accounted substrate.

## Monotonicity and composition checks

Minimum description length is monotone only under carefully specified compiler constructions; it is not a resource monotone under arbitrary language redesign. Concatenating law descriptions yields subadditive upper bounds up to coding overhead, not exact additive composition. Execution costs can exhibit amortization, reuse and speedup. Thus a universal additive law-extension metric is not supported.

## Prior-art collision check

Strong collisions:

- Kolmogorov complexity and its invariance theorem: universal-machine choice changes exact complexity by machine-dependent additive constants.
- Algorithmic information: shortest descriptions are uncomputable in general.
- Universal simulation: fixed interpreters compile one computable law into another machine with fixed description overhead.
- Linear speedup and Blum speedup: exact/minimal execution complexity is not a universal semantic invariant in unrestricted models.
- Le Cam/simulation/resource-theory deficiencies: once structural representation cost is removed, directed extensional convertibility returns to known deficiency/simulation architectures.

No novelty is claimed for these mechanisms.

## Decisive classification

- Exact absolute compiler-invariant structural law-extension cost: FALSIFIED.
- Exact universal execution-cost law-extension invariant: FALSIFIED in the unrestricted universal domain.
- Relative law-extension cost on a frozen physical substrate: VALID but representation-relative.
- Asymptotic/equivalence-class structural cost: VALID, IMPORTED/KNOWN architecture.
- A standalone law-extension deficiency as the GC-II breakthrough: FALSIFIED in the unrestricted form attacked here.

## Surviving breakthrough target

The no-go result sharply changes the search. A defensible GC-II breakthrough cannot demand both arbitrary compiler invariance and exact absolute structural/execution cost. The remaining route is a physically anchored operational invariant:

    Omega_G^P(S,T | C)

relative to a conserved physical substrate P and declared context C, with typed cost vector (Delta R, Delta I, Delta A, Delta L), where the allowed representation changes are exactly the cost-preserving automorphisms/simulations of P.

The next target is to find a theorem whose value is invariant under that restricted physical equivalence, vanishes under independent-product decompositions, and yields a quantitative separation that cannot be reduced to shortest paths, Blackwell deficiency, ordinary simulation, communication/query complexity, coding, contextuality/marginal inconsistency, CSP/database width, or standard resource monotones.

A promising test object is an operational *boundary-crossing rank*: minimum number/rank of physically distinct capability channels that must cross the closed-substrate boundary to realize a target whole-envelope obligation, with exact finite witnesses and a dual certificate. This is OPEN and must be killed against cut/rank/min-cut, matroid, network coding, resource rank, and communication complexity before any novelty claim.

## Sources checked

- Kolmogorov-complexity invariance theorem: exact complexity depends on universal description language; differences are bounded only up to machine-dependent additive constants.
- Bauwens, Kozachinskiy & Shen (2025), `All Kolmogorov complexity functions are optimal, but are some more optimal?`, arXiv:2506.16180: discusses the non-canonical choice among optimal complexity functions.
- Blum (1967), `A Machine-Independent Theory of the Complexity of Recursive Functions`, Journal of the ACM: foundation for Blum complexity measures and speedup phenomena.

The audit uses these only as collision/boundary results; it does not claim them as GC-II discoveries.