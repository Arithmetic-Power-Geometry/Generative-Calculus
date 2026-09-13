# GC-II Audit 117 — Joint-compatibility local-to-global collision

Status date: 2026-09-13

## Question
Can GC-II escape Audit 116 by using several independently meaningful realization boundaries B_1,...,B_k such that every pair admits compatible/zero-residual translation while no globally compatible translator family exists?

## Abstract finite formulation
Let H=(V,E) be a hypergraph of boundary contexts. For every context e in E let R_e be the relation of locally admissible translator assignments on the variables/boundaries in e. Pairwise compatibility means

pi_{e cap f}(R_e) = pi_{e cap f}(R_f)

for every e,f. Global compatibility means that there exists a relation R on V whose projection to every e is R_e (or, for existence-only semantics, at least one global assignment whose restrictions lie in every R_e).

Under this formulation, the proposed GC-II obstruction is exactly a local-to-global consistency obstruction.

## Proposition 117.1 — Translator compatibility reduction
Any finite joint-translator problem whose constraints are completely specified by context-local admissibility relations reduces exactly to a relational join / CSP consistency instance: use one variable for each shared translator/interface degree of freedom and one relation R_e for each local compatibility context. Pairwise translator consistency is pairwise relational consistency; a globally compatible translator family is a global satisfying assignment/universal relation.

Proof. This is a direct encoding preserving assignments and restrictions in both directions. Every global translator assignment restricts to a tuple in each R_e. Conversely, every global tuple satisfying all R_e specifies a compatible family. Therefore feasibility and local/global failure are preserved exactly. □

Status: PROVED (exact finite reduction; not a novelty theorem).

## Proposition 117.2 — Pairwise-zero/global-impossible is not new
There exist cyclic context schemas with pairwise-consistent local relations that have no global realization. A minimal Boolean triangle is:

R_AB = {(0,0),(1,1)}
R_BC = {(0,1),(1,0)}
R_CA = {(0,0),(1,1)}.

Every pair agrees on its one-variable overlap (both project to {0,1}), but no triple (A,B,C) satisfies all three: R_AB and R_CA force B=A=C while R_BC requires B != C.

Status: PROVED.

This is the exact qualitative phenomenon sought after Audit 116: all pairwise compatibility checks pass while global compatibility fails. But it is a classical local-to-global consistency phenomenon rather than a new GC-II mechanism.

## Proposition 117.3 — Acyclic-schema collapse for ordinary relations
For ordinary relational compatibility constraints, alpha-acyclic schemas have the local-to-global property: pairwise-consistent relations are globally consistent. Thus any purely relational joint-translator obstruction of this form requires cyclic/non-acyclic context structure (or a richer annotation algebra for which ordinary acyclicity is not sufficient).

Status: IMPORTED/KNOWN theorem (Beeri-Fagin-Maier-Yannakakis lineage; reconfirmed in recent database-consistency literature).

## Quantitative excess-burden warning
Replacing feasibility by

Omega_joint = minimum cost of a global compatible family - an aggregate of pairwise minima

does not by itself rescue novelty. Once local relations and costs are fixed, this is a weighted global CSP/join/optimization problem. Moreover the aggregate of pairwise minima need not be a valid lower bound without a non-overlap or dual-feasibility argument, so an alleged positive 'excess' can be an accounting artifact caused by double counting or incompatible local minimizers.

Status: FALSIFIED AS STANDALONE NOVELTY.

## Edge and invariance checks
- One context: local = global; obstruction zero.
- Two contexts: pairwise compatibility is already global compatibility for the two-context family.
- Acyclic ordinary relational schema: pairwise consistency implies global consistency.
- Cyclic triangle: pairwise consistency can fail globally, as the Boolean example proves.
- Renaming variables/translator implementations: relational feasibility is invariant under bijective renaming.
- Duplicate contexts: do not create a genuine obstruction.
- Empty local relation: immediate local failure, not a local-to-global phenomenon.
- Universal relations: obstruction zero.
- Costs: typed coordinates must remain vector-valued unless exchange rates/scalarization are independently justified.

## Prior-art collision gate
- relational database local-to-global consistency / join dependencies: DIRECT COLLISION
- CSP local consistency versus global satisfiability: DIRECT COLLISION
- marginal consistency/contextuality: DIRECT STRUCTURAL COLLISION for probabilistic/context-indexed variants
- sheaf/cocycle obstruction: DIRECT STRUCTURAL COLLISION for gluing formulations
- distributed agreement: possible application-level collision, not needed for the no-go
- resource convertibility: possible weighted specialization

Recent literature continues to characterize local-to-global consistency by hypergraph structure, including ordinary relations, bags, and positive-commutative-monoid annotations. Therefore pairwise-zero/global-nonzero compatibility is not sufficient for a GC-II breakthrough claim.

## Decision
DECISIVE FALSIFICATION: the generic joint-translator compatibility route proposed after Audit 116 collapses exactly to established local-to-global consistency / relational join / CSP machinery whenever finite compatibility is completely context-local.

A surviving GC-II target must violate at least one premise of Proposition 117.1 in an independently operationally meaningful way, rather than by notation. Candidate directions must require a capability consequence that cannot be represented as static context-local relations over a fixed variable set—for example, a theorem coupling capability creation to endogenous change of the *type/signature of future compatibility constraints* with an irreducible realization lower bound. But Audit 111 already shows that finite endogenous state enlargement alone is absorbable, so this candidate remains OPEN and must be killed against dependent/type-changing CSPs, dynamic constraint systems, categorical/sheaf semantics, and program-state augmentation before promotion.

No breakthrough is claimed.
