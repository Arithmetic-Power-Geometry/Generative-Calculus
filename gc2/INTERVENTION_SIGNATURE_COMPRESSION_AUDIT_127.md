# GC-II Audit 127 — Exact Intervention-Signature Compression Gate

## Question
Can the full intervention-response signature from Audit 126 be replaced, for an unrestricted finite class, by a strictly smaller exact family of intervention coordinates or by an exact certificate carrying fewer distinguishability states?

## Setup
Let J={1,...,m} be a finite intervention family and let each system M have binary response signature

Sigma_J(M)=(r_1(M),...,r_m(M)) in {0,1}^m.

The binary case is deliberately minimal: any proposed general exact compression theorem must survive it.

For S subset J define the coordinate certificate C_S(M)=Sigma_J(M)|_S.

## Theorem 127A — no universal strict coordinate-subset compression
For the unrestricted signature class X={0,1}^m, C_S is complete for equality of full intervention signatures if and only if S=J.

### Proof
If S=J the statement is immediate. If S is proper, choose j in J\S. Let x be the all-zero signature and let y differ from x only at coordinate j. Then C_S(x)=C_S(y) but x != y. Hence every proper coordinate subset loses exact distinguishing power. QED.

Status: **PROVED**.

## Theorem 127B — cardinality lower bound for arbitrary exact certificates
Let C:X -> Y be any certificate such that C(x)=C(y) iff x=y for all x,y in X={0,1}^m. Then C is injective, hence |Y| >= 2^m. Consequently any fixed-length binary encoding of a universally complete exact certificate requires at least m bits.

### Proof
Completeness for equality is precisely injectivity. Since |X|=2^m, the pigeonhole principle gives |Y|>=2^m; a fixed-length L-bit code has at most 2^L values, so L>=m. QED.

Status: **PROVED**.

## Exact finite kill test
`gc2/experiments/audit127_intervention_signature_compression.py` enumerates m=4, all 16 binary intervention signatures, all 120 unordered distinct signature pairs, and all 15 proper intervention-coordinate subsets. Every proper subset has at least one collision; in fact the minimum is 8 colliding pairs. Across all subset/pair tests there are 520 collisions. There are zero falsely complete proper subsets.

Status: **EXHAUSTIVE FINITE VERIFICATION**.

## Edge and degeneration checks
- m=0: the unique empty signature needs zero bits; no distinction exists.
- m=1: dropping the sole intervention merges the two possible signatures.
- Duplicate/unrealizable signatures: compression can occur only after restricting the realizable system class; the lower bound is then log2 of the number of distinct equivalence classes, not necessarily m.
- Nonbinary responses: replace 2^m by the cardinality of the realizable response-signature set.
- Approximate certificates: outside this theorem; allowing error moves the question to lossy/sketching/information-theoretic approximation.
- Structured system classes: potentially compressible, but the gain comes from independently proved restrictions on realizable signatures.

## Prior-art collision
This result is not claimed as new mathematics. The quotient-by-indistinguishability/minimal-state principle is the same structural move underlying Myhill–Nerode minimization and behavioral/bisimulation quotients. Exact finite encoding lower bounds are elementary counting/information bounds. Bisimulation minimization and partition refinement explicitly compute smaller systems preserving a chosen behavioral equivalence.

## Consequence for GC-II
The proposed target "strict compression of the full intervention-response signature" is **FALSIFIED as a universal standalone breakthrough target**. Without extra structure, exact completeness forces preservation of every intervention-signature equivalence class; for the unrestricted binary class there are 2^m such classes and no universal exact bit saving is possible.

A scientifically viable next target must therefore identify a nontrivial operational class whose realizable intervention signatures obey independently derived constraints and then prove a compressed complete criterion that exploits those constraints. Merely assigning an equivalence-class ID is not a new capability law.

## Status ledger
- No strict coordinate-subset compression on unrestricted binary signatures: **PROVED**.
- m-bit lower bound for arbitrary exact fixed-length certificates on {0,1}^m: **PROVED**.
- Exhaustive m=4 regression: **PASS**.
- Universal strict exact compression as GC-II novelty: **FALSIFIED**.
- Quotient/minimization machinery: **IMPORTED/KNOWN**.
- Structured-class compressed complete monotones: **OPEN**.
