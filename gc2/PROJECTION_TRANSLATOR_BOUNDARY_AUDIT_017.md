# GC-II Projection-to-Translator Boundary Audit 017

## Target
Test whether GC-I proper-projection irreducibility can by itself yield the requested GC-II operational local-to-global translator lower bound.

## Finite parity lift
Let the operational input be `x in {0,1}^n` and let the required whole-envelope output be

`y(x) = x_1 xor ... xor x_n`.

For every proper coordinate projection `pi_S`, `S proper subset {1,...,n}`, there exist `x,x'` with `pi_S(x)=pi_S(x')` but `y(x) != y(x')`: choose any omitted coordinate `j`, hold all coordinates in `S` fixed, and flip only `x_j`.

### Proposition (restricted deterministic specialization)
No deterministic shared translator whose complete visible information factors through any fixed proper coordinate projection `pi_S` can exactly realize the parity target on all inputs.

### Proof
If the translator factors through `pi_S`, then equal projected observations must produce equal outputs. The witness pair above has equal projected observation and opposite required outputs. Contradiction. QED.

## Query/interface lower bound
Suppose a translator may adaptively query individual coordinates and must output parity exactly on every input. Every root-to-leaf computation must query all `n` coordinates in the worst case. Otherwise, at a leaf omitting coordinate `j`, two inputs differing only in `j` reach the same leaf but have opposite parity. Therefore exact deterministic coordinate-query depth is at least `n`, and querying all coordinates attains `n`.

Thus the projection obstruction yields an exact linear local-to-global information/interface lower bound in this specialization.

## Why this is not the Paper-II breakthrough
The proof is a standard decision-tree indistinguishability argument for parity. It does not exploit vector resource budgets, endogenous changes to admissible actions/rules, task-scale-error envelopes, or a GC-specific translator model. Classical decision-tree/circuit/communication-complexity theory already supplies stronger parity lower bounds in many restricted models. Therefore:

- `proper-projection irreducibility => no fixed proper-projection exact translator`: **PROVED** in this finite deterministic specialization;
- exact coordinate-query depth of parity is `n`: **IMPORTED/KNOWN mechanism**;
- claiming this alone as a novel GC-II local-to-global lower bound: **FALSIFIED as a novelty route**;
- a GC-II-specific lower bound must survive comparison with decision trees, communication complexity, branching programs/OBDDs, circuit lower bounds, database/CSP locality, and contextuality/marginal reconstruction: **OPEN**.

## Stronger target retained
Seek a family of operational worlds with coupled vector budgets and endogenous `R/I/A/L` transformations such that prescribed low-order projections remain identical while every admissible whole-envelope translator incurs a provable resource/information/interface/rule cost that cannot be reduced to an existing parity/query/communication lower bound.

A useful candidate invariant must therefore depend on the operational transformation structure, not merely on the Boolean target function.

## Status
No breakthrough claim. This audit closes another false-positive route and prevents GC-I parity irreducibility from being repackaged as new translator complexity without additional operational structure.
