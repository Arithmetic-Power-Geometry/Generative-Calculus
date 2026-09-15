# GC-II Audit 150 — Sufficient-state explosion boundary

## Question
Can Paper II obtain a new Closure-Escape theorem merely by proving that the minimum exact operational sufficient-state quotient is exponentially larger than a succinct local description?

## Witness
For n>=1 let

L_n = { w in {0,1}* : the n-th symbol from the right of w is 1 }.

Interpret a prefix as an operational history and its right-language/residual as the exact future capability signature required by any deterministic sufficient-state compiler.

## Exact lower bound
There are 2^n strings x in {0,1}^n. Take distinct x,y and let j be a coordinate at which they differ (1-indexed from the left). Append z=0^(j-1). In xz and yz the n-th symbol from the right is exactly coordinate j of x and y, respectively. Hence exactly one of xz,yz lies in L_n. Therefore all 2^n length-n histories have distinct residuals.

By the Myhill-Nerode characterization, every exact deterministic sufficient-state quotient needs at least 2^n states.

## Upper bound
Remember the last n symbols, padding the initial history on the left with zeros. This gives 2^n states and decides L_n exactly. Thus

S_exact(L_n) = 2^n.

The description of the family is O(n) as an NFA (and n can itself be named succinctly), so the exact deterministic quotient can be exponentially larger than a natural operational representation.

## GC-II consequence
This proves that large compiler blow-up is a real obstruction to explicit state materialization, but it does NOT establish a new GC-II invariant or theorem. The witness is a canonical automata-theoretic state-complexity phenomenon: NFA determinization can require 2^n states, and this exact nth-symbol-from-right family is a standard tight witness. Therefore "minimum sufficient-state explosion" alone fails the novelty gate.

## Status ledger
- Exact 2^n deterministic sufficient-state requirement for L_n: IMPORTED/KNOWN (proof reproduced exactly).
- Exponential blow-up relative to succinct nondeterministic description: IMPORTED/KNOWN.
- Regression checker: NUMERICALLY SUPPORTED / PASS for tested finite n.
- State explosion alone as GC-II Closure-Escape novelty: FALSIFIED.
- Candidate requiring a lower bound that is operationally typed (resources/information/interfaces/rules) and is not reducible to automata/streaming/communication state complexity: OPEN.

## Next gate
Do not count compiler states alone. Search for two operational systems with the same minimal residual-state quotient/state complexity but different minimum typed realization cost under explicit R/I/A/L restrictions. A surviving Omega_G must distinguish realization burden that ordinary residual equivalence deliberately quotients away, while remaining invariant under representation changes.
