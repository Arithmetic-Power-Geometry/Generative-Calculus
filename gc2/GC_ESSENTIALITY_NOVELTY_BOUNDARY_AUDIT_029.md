# GC-II Audit 029 — GC-Essentiality Is Necessary but Not Sufficient for Novelty

## Status
**DECISIVE METHODOLOGICAL FALSIFICATION.** Audit 028's GC-essentiality test is useful as a necessary filter, but it is not sufficient evidence of a GC-II breakthrough.

## Candidate being tested
Audit 028 proposed that a translator lower bound should collapse after deleting at least one essential GC semantic ingredient (vector-budget coupling, endogenous information/action/rule acquisition, or task-scale-error requirements). The intended purpose was to exclude generic graph/circuit/succinctness effects.

## Boundary proposition
Let a theorem T be formulated in a GC model and suppose T becomes false, trivial, or asymptotically weaker after deleting semantic ingredient S. Then S is essential to that formulation of T. This does **not** imply that T, its proof mechanism, or its quantitative bound is novel to GC.

### Proof
Novelty and semantic essentiality are logically different predicates. A result imported from an existing theory can depend essentially on exactly the semantic structure represented by S. Embedding that known theory into GC preserves both the theorem and the fact that deleting S destroys it. Therefore the GC-essentiality test can reject some generic lower bounds, but passing the test cannot distinguish a genuinely new GC theorem from an imported theorem expressed in GC notation. QED.

## Concrete collision witness
Resource-bounded dynamic epistemic logic already combines information-changing actions with resource/cognitive constraints. Solaki's resource-bounded DEL explicitly includes actions for learning, forgetting, and applying inference rules, with updates to epistemic accessibility, rule availability, and cognitive capacity. Dolgorukov, Galimullin and Gladyshev study resource-bounded information-mining agents whose information queries have costs and whose agents have budget constraints. Epistemic planning with attention as a bounded resource likewise couples information acquisition to a scarce resource.

Thus a GC theorem whose lower bound disappears when information acquisition, rule availability, or its budget is erased may pass Audit 028's essentiality test while still colliding directly with established epistemic logic/planning mechanisms.

## Corrected novelty gate
For a theorem candidate T in model M_G, require all of the following before calling it a breakthrough candidate:

1. **GC-essentiality:** deleting at least one claimed GC ingredient destroys or strictly weakens the result.
2. **Embedding audit:** identify strongest known neighboring models N_j and explicit embeddings/reductions E_j into M_G whenever possible.
3. **Mechanism separation:** prove that the quantitative conclusion cannot be obtained by applying a known theorem in any E_j(N_j) with only notation/encoding changes.
4. **Joint-structure necessity:** when novelty is claimed from coupling, show that no single neighboring ingredient alone yields the bound; the proof must use a specified interaction among at least two semantic axes.
5. **Quantitative surplus:** state the new inequality/separation/conservation law that is stronger or differently scoped than the imported bounds, not merely a richer ontology.
6. **Ablation witnesses:** provide finite or parametric countermodels showing exactly which conclusion fails when each claimed essential interaction is removed.

Passing these gates remains evidence for a candidate, not a proof of literature-wide novelty.

## Stronger target: interaction-essential accounting
A safer next object is an interaction term defined operationally by comparison with controlled ablations, rather than by arbitrary addition of unlike units. For a dimensionless normalized capability deficit D under a fixed observation family, define the two-axis interaction residue

`J_{S,T} = D(M_{-S,-T}) - D(M_{-S}) - D(M_{-T}) + D(M)`.

This is an inclusion-exclusion contrast, not yet a GC invariant. Its sign is not fixed in general and it is representation/ablation dependent. It is useful experimentally because `J_{S,T} != 0` witnesses non-additive interaction under the declared ablation semantics. It does **not** by itself establish novelty.

For physical or heterogeneous resource coordinates, keep the primitive accounting vector-valued/Pareto-valued; only compute such scalar contrasts after declaring a dimensionless task-level deficit or utility functional.

## Edge and counterexample checks
- A known theorem can pass GC-essentiality exactly; therefore essentiality is not sufficient.
- A theorem can fail the essentiality test yet still be mathematically new for another reason; essentiality is a project-specific novelty filter, not a logical definition of novelty.
- `J_{S,T}=0` does not prove independence; nonlinear effects can cancel in the chosen scalar deficit.
- `J_{S,T}!=0` does not prove causal interaction unless the ablations are operationally well-defined interventions.
- The interaction residue changes with normalization/utility choice; it is not dimension-free automatically.
- Higher-order interactions may exist even if every pairwise residue vanishes.

## Prior-art collision status
- Dynamic epistemic logic: **KNOWN** model-change framework for information/knowledge-changing actions.
- Resource-bounded DEL: **KNOWN** coupling of learning/forgetting/rule use to bounded cognitive resources.
- Costed information queries under budgets: **KNOWN** in resource-bounded information-mining DEL.
- Attention-bounded epistemic planning: **KNOWN**.

Accordingly, `information + action/rule change + budget` cannot be treated as a uniquely GC coupling.

## Status delta
- Audit-028 GC-essentiality test as a necessary anti-relabeling filter: **RETAINED**.
- GC-essentiality as sufficient novelty evidence: **FALSIFIED**.
- Generic information/rule acquisition under resource bounds as a GC-II novelty route: **IMPORTED/KNOWN**.
- Interaction-essential capability accounting with quantitative surplus beyond neighboring embeddings: **OPEN / highest-priority refinement**.
- Breakthrough status: **NONE YET**.

## Next exact experiment
Build a factorial finite-world ablation harness on a fixed underlying graph. Toggle information acquisition I, action/interface augmentation A, and rule augmentation L while holding graph topology and base resource coordinates fixed. For every world compute an explicitly declared dimensionless whole-envelope deficit D and all pairwise/third-order inclusion-exclusion residues. Search exhaustively for minimal worlds where a nonzero higher-order interaction is necessary for closure escape. Then attempt to reproduce each witness inside resource-bounded DEL, energy games, planning, and process semantics. Only witnesses that resist those reductions should advance to theorem search.

## Literature checked in this audit
- A. Solaki, *A Dynamic Epistemic Logic for Resource-Bounded Agents* (2019): learning, forgetting, inference-rule actions; updates to epistemic accessibility, rule availability and cognitive capacity.
- V. Dolgorukov, R. Galimullin, M. Gladyshev, *Dynamic Epistemic Logic of Resource Bounded Information Mining Agents* (2024): costed information queries and budget constraints.
- G. Belardinelli, R. K. Rendsvig, *Epistemic Planning with Attention as a Bounded Resource* (2021): bounded attention integrated with epistemic planning.
