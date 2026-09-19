# GC-II Audit 256 — Structural reversibility defect: exact finite baseline

## Purpose
Audit 255 showed that equal forward/reverse shortest-path costs do not imply operational reversibility. This audit introduces the weakest exact graph-level repair and deliberately treats it as a baseline rather than a novelty claim.

## Finite typed operational system
Let `X` be a finite state set and let an admissible operation edge be

`e=(u,v,t,c)`

with source `u`, target `v`, operation type `t` (e.g. R/I/A/L), and nonnegative cost `c`.

For this audit, an edge is **structurally invertible** when the system also contains an admissible reverse edge `(v,u,t,c')` of the same type. Cost equality is *not* required: structural invertibility and energetic/economic symmetry are distinct questions.

Define the edge defect

`kappa(e)=0` if such a same-type reverse edge exists, and `kappa(e)=1` otherwise.

For a directed path `P`, define `K(P)=sum_{e in P} kappa(e)`.

For mutually reachable states `x,y`, define the **structural reversibility defect**

`D_str(x,y)= min_{P:x->y, Q:y->x} [K(P)+K(Q)]`.

Because the two path choices are independent,

`D_str(x,y)=d_kappa(x,y)+d_kappa(y,x)`,

where `d_kappa` is directed shortest-path distance with 0/1 edge weights `kappa`.

If either direction is unreachable, `D_str=+infinity`.

## Theorem 256.1 — exact zero-defect criterion
For mutually reachable `x,y`, the following are equivalent:

1. `D_str(x,y)=0`.
2. There is an `x->y` path consisting only of structurally invertible edges.
3. `x` and `y` lie in the same connected component of the undirected graph obtained by retaining exactly those state pairs that possess a same-type edge in both directions.

### Proof
(1)->(2): nonnegative integer edge defects sum to zero only if every edge on a minimizing forward path has defect zero.

(2)->(3): each edge of the path survives in the retained bidirected graph.

(3)->(2): orient the component path from `x` to `y`; every retained adjacency has a same-type admissible edge in the required direction.

(2)->(1): reverse every edge of the forward path using its guaranteed same-type reverse edge. Both path defects are zero. QED.

## Theorem 256.2 — Audit-255 collision is separated
In the directed 4-cycle

`0->1->2->3->0`

with all edges type A and unit cost,

`d(0,2)=d(2,0)=2`, hence the Audit-255 scalar gap is zero, but every edge lacks a reverse edge. Therefore

`D_str(0,2)=4`.

Thus `D_str` distinguishes at least one pair of systems/states that ordinary forward/reverse cost asymmetry cannot distinguish.

## Theorem 256.3 — symmetry and invariance
`D_str(x,y)=D_str(y,x)` by definition. It is invariant under relabeling of states and under bijective renaming of operation types. Uniform positive rescaling of monetary/resource costs leaves `D_str` unchanged because `kappa` depends only on admissibility/type structure.

## Theorem 256.4 — independent-product additivity
Consider the asynchronous Cartesian product of two typed systems: each product edge changes exactly one component by one local edge and inherits its type. Assume type namespaces are preserved so inverse compatibility of a product edge is exactly inverse compatibility of its changed local edge. Then

`D_str((x1,x2),(y1,y2)) = D_str^1(x1,y1)+D_str^2(x2,y2)`.

Reason: every product path projects to local paths; its `kappa` cost is the sum of local projected `kappa` costs. Conversely, optimal local paths can be interleaved to attain the sum. Apply this in both directions.

## Edge and degenerate cases
- `D_str(x,x)=0` using the empty path.
- One-way reachability gives `+infinity`, not a finite defect.
- Zero-cost irreversible edges can have `kappa=1`; monetary cost and structural reversibility are intentionally independent.
- A reverse edge of a different type does not cancel the defect under the present typed semantics.
- Parallel edges are allowed; an edge is defect-free if at least one same-type reverse edge exists.
- `D_str=0` does **not** imply equal forward/reverse monetary costs.
- `D_str>0` does **not** quantify information loss, projection loss, or semantic regeneration cost; it only counts unavoidable locally unpaired operational steps.

## Collision / novelty audit
This construction is graph reciprocity / bidirected-subgraph structure plus shortest paths with 0/1 penalties. Those mechanisms are standard graph-theoretic objects. Therefore:

- structural defect definition: **PROVED / baseline definition**;
- zero-defect criterion: **PROVED / generic graph mechanism**;
- separation from Audit-255 scalar cost symmetry: **PROVED**;
- independent-product additivity: **PROVED under stated asynchronous-product assumptions**;
- generic mathematical novelty: **IMPORTED/KNOWN mechanism; NOT CLAIMED**;
- `D_str` as the final GC-II reversibility invariant: **FALSIFIED as a claim of semantic completeness** because it ignores what an operation destroys/reconstructs internally;
- GC-specific semantic regeneration defect over projection/information/interface/rule structure: **OPEN**.

## Consequence for Paper II
A credible GC-II reversibility invariant must refine this baseline. At minimum it should distinguish two systems having the same directed costs **and** the same edge-reciprocity pattern when their operations differ in destruction/regeneration of projection structure, information access, interfaces/actions, or rules. Audit 256 therefore supplies a falsification baseline for the next candidate rather than a breakthrough claim.
