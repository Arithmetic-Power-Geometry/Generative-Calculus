# GC-II Audit 057 — Cross-Obligation Gluing Collision

Status date: 2026-09-10
Branch: `gc2-capability-accounting-lab`
Parent audit: 056

## Question

Can GC-II obtain a new local-to-global capability invariant by arranging that every proper subfamily of obligations is jointly realizable with matched typed capability frontiers, while the full obligation family is not jointly realizable?

## Exact finite witness

Let binary variables x_1,...,x_n be arranged on a cycle. Associate to each edge e_i=(i,i+1) a local obligation

    q_i: x_i XOR x_{i+1} = b_i,

with indices modulo n. Choose b_1,...,b_n with XOR_i b_i = 1.

Every proper subset of these edge obligations is satisfiable: deleting at least one cycle edge leaves a forest/path system, and one may choose one root bit per component and propagate the parity equations along its edges.

The full family is unsatisfiable. XORing all n equations cancels every variable twice on the left, giving 0, while the right side is XOR_i b_i = 1. Hence no global assignment exists.

Status: PROVED.

This yields an arbitrarily high-order local/global separation: all proper obligation subfamilies admit exact realization while the complete family does not.

## Why this is not a GC-II breakthrough

The mechanism is a classical parity/Tseitin-style global-consistency obstruction. Local consistency versus global inconsistency is already central to constraint satisfaction, relational databases, probability marginal problems, and contextuality. Acyclic hypergraph schemas are precisely a major regime in which suitable local consistency implies global consistency; cycles support counterexamples. Tseitin parity constructions are a standard way to witness the obstruction.

Therefore the statement

    every proper obligation subfamily is feasible but the whole family is infeasible

is not novel enough to define Omega_G.

Status of cross-obligation gluing obstruction as a standalone breakthrough route: FALSIFIED.

## Typed-cost strengthening does not rescue the bare mechanism

Attach any fixed typed cost vector c_i=(R_i,I_i,A_i,L_i) to realizing edge obligation q_i. On every satisfiable proper subfamily the total/trace accounting can be made explicit. The global family remains infeasible because the logical compatibility constraint fails before resource optimization is relevant. Thus merely decorating the parity obstruction with typed costs does not create a new capability law.

If instead resources/actions can modify b_i, remove constraints, add communication, or change the evaluator, then the problem becomes a minimum augmentation/repair problem. Such repair formulations immediately collide with weighted CSP, deletion/relaxation problems, coding/syndrome correction, network optimization, and resource theories unless GC composition forces a genuinely new law.

## Domain and edge checks

- n>=3 gives the cycle construction directly.
- If XOR_i b_i=0, the full family is satisfiable; the obstruction vanishes.
- Removing any one edge makes the constraint graph acyclic and satisfiable.
- Relabeling variables or reversing cycle orientation preserves the obstruction.
- Parallel composition of independent odd-parity cycles gives multiple independent inconsistency certificates; this is ordinary direct-product behavior, not evidence of a new invariant.
- Allowing an oracle that supplies a violated-edge deletion imports an action/resource but does not change the underlying obstruction.
- Changing the success semantics from simultaneous satisfaction to per-obligation satisfaction destroys the conserved joint-obligation comparison and cannot count as free capability.

## Consequence for GC-II

High-order local-to-global failure alone is now ruled out as the breakthrough source, even when every proper subfamily agrees. Together with Audits 049, 050, 055, and 056, this removes a broad family of candidates based solely on hidden global compatibility, reusable representation, unsupported Pareto points, exchange structure, or gluing failure.

## Surviving target: cost of repairing a conserved obstruction

A potentially stronger object is not whether a global section exists, but the typed Pareto cost of converting an inconsistent obligation complex into a globally realizable one while preserving a fixed evaluator and admissible physical substrate:

    Repair_G(Q) = Min_Pareto { delta=(Delta R,Delta I,Delta A,Delta L) : Q is jointly realizable after an admissible augmentation of typed cost delta }.

This definition is VALID but its novelty is OPEN.

The next kill-first test is whether Repair_G is only a repackaging of weighted CSP repair / Max-CSP, minimum constraint deletion, syndrome decoding, contextual fraction/robustness, database repair, or network interdiction/augmentation. A genuine GC-II result would need a theorem in which task-scale-error-budget composition imposes a quantitative repair law not obtainable from those reductions.

## Classification

- Odd-cycle/general cycle parity proper-subfamily feasibility: PROVED.
- Full-family impossibility when XOR_i b_i=1: PROVED.
- Arbitrarily high-order local/global separation: PROVED.
- Mechanism: IMPORTED/KNOWN (Tseitin/CSP/database/contextuality family).
- Cross-obligation gluing as standalone Omega_G breakthrough: FALSIFIED.
- Typed obstruction-repair frontier Repair_G: OPEN, next target.
