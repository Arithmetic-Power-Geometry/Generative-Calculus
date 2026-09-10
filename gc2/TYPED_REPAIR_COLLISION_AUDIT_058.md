# GC-II Audit 058 — Typed Repair Frontier Collision

Status date: 2026-09-11
Branch: `gc2-capability-accounting-lab`
Parent audit: 057

## Question

Does the typed minimum cost of repairing a jointly unrealizable obligation family provide a new GC-II invariant?

## Candidate

For a fixed physical substrate S, conserved evaluator E, obligation family Q, and declared typed augmentations a=(Delta R,Delta I,Delta A,Delta L), define

    Repair_G(Q) = Min_Pareto { a : Q is jointly realizable in the augmented substrate S+a }.

No scalar addition of unlike resource coordinates is assumed.

## Exact reduction theorem

Consider any finite GC repair instance for which each allowed augmentation can be represented by a finite Boolean/discrete activation variable y_j, and joint realizability after choosing y is decidable by a finite constraint system C(x,y), where x denotes execution/state variables. Then the repair problem is exactly a multiobjective valued constraint/partial-MaxSAT style optimization:

    find y such that exists x C(x,y),
    minimize_Pareto c(y),

where c(y) is the declared typed cost vector of activated relaxations/augmentations.

Proof: introduce one activation/relaxation variable per admissible repair operation. Encode the original operational constraints as hard constraints and gate each repairable restriction by its activation variable. A repair is feasible iff the resulting hard system has a satisfying assignment. The map between feasible GC repairs and satisfying activation vectors is bijective after quotienting duplicate activations with identical declared physical effect. Typed costs are carried as a vector objective rather than summed. Hence the complete Pareto repair set is precisely the Pareto set of the corresponding multiobjective finite constraint optimization instance.

Status: PROVED for the stated finite explicit class. The optimization architecture is IMPORTED/KNOWN.

## XOR-cycle specialization

For Audit 057's inconsistent parity cycle, allowing obligation deletion at unit cost reduces repair to a correction-set problem. Removing any one parity equation breaks the inconsistent cycle and yields satisfiability, so the minimum deletion repair cost is exactly 1. If repair instead permits bit flips of the syndrome b, the minimum repair is the minimum-weight vector e satisfying the required parity correction; this is a syndrome/coset-leader decoding form.

Status: PROVED for the construction; mechanism IMPORTED/KNOWN.

## Why typed coordinates do not rescue novelty

Replacing a scalar penalty by (Delta R,Delta I,Delta A,Delta L) changes the optimization order from total to Pareto, but finite multiobjective combinatorial optimization already handles vector-valued objectives. Merely refusing to add unlike units is physically cleaner accounting, not a new mathematical obstruction. A scalarization is optional: the exact Pareto set can be defined without one.

## Contextuality/database collisions

The same conceptual move — quantify the minimum modification/noise/relaxation needed to enter a feasible/noncontextual/consistent set — is established in robustness measures of contextuality and in database repair. Therefore 'minimum repair needed to remove a gluing obstruction' is not by itself a unique GC mechanism.

## Edge/domain checks

- If Q is already jointly realizable, 0 belongs to the repair set and is the unique least element when all costs are nonnegative.
- If no declared augmentation can repair Q, Repair_G(Q) is empty/infinite according to the chosen completion convention; this must not be called positive novelty.
- Zero-cost augmentations must be included in the original closure or quotient; otherwise a fake positive/zero gap can be created by bookkeeping.
- Duplicate repair actions with the same physical effect and cost are representation artifacts and should be quotiented.
- Negative resource coordinates destroy the ordinary augmentation order unless an explicit conversion/replenishment law is supplied.
- Nonadditive interaction costs can be encoded by joint activation variables or higher-order cost functions in a finite instance; nonadditivity alone therefore does not escape the reduction.
- Continuous/infinite repair spaces are outside this finite theorem and remain OPEN, but continuity itself is not evidence of novelty.

## Decisive classification

- Typed Pareto repair frontier: VALID and potentially useful GC accounting object.
- Finite explicit repair optimization: REDUCES EXACTLY to known multiobjective constraint optimization architecture.
- XOR obligation-deletion repair: correction-set/MaxSAT form.
- XOR syndrome-flip repair: decoding/coset-leader form.
- Minimum repair as standalone source of Omega_G novelty: FALSIFIED for finite explicit systems.

## Surviving target

Audit 052 showed that finite explicit GC dynamics compile into an augmented transition system. Audit 058 now shows that finite explicit repair of such systems compiles into finite multiobjective constraint optimization. Therefore a breakthrough cannot come merely from (i) adding endogenous state, (ii) local/global inconsistency, or (iii) minimizing the cost of repairing that inconsistency.

The next kill-first target is **uniform compositional repair**: seek a theorem about a family of substrates/obligations under composition for which the repair frontier obeys a GC-specific law across task scale, error tolerance, budget and repeated composition, rather than merely solving one encoded optimization instance. Candidate quantities must be representation-safe and compared against asymptotic resource rates, amortized communication/complexity, direct-sum/direct-product theorems, resource-theory regularization, tensor rank/asymptotic spectrum, and parallel repetition. A finite-instance encoding is not sufficient evidence of novelty.
