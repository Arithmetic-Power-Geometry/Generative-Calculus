# GC-II Audit 082 — Capability-Witness Realization Lower Bound

## Scope
Branch-only Paper-II audit. GC-I foundations on `main` are not modified.

## Candidate
A proposed architecture-independent theorem would assign every capability witness `w` for task `q` a strictly positive typed augmentation lower bound

\[
\Omega_{\rm wit}(w,q) \succeq L(w,q)>0,
\]

in the physical ledger `(R,I,A,L)`, invariant under admissible recompilation/re-encoding.

## Result
**FALSIFIED as a universal GC-II breakthrough candidate.**

### Realization-dependence theorem — PROVED
Let `W` be an abstract witness and let `rho` be a physical realization map from abstract witness executions into histories of a declared substrate. A typed physical lower bound is a property of `(W,rho,M)`, not of `W` alone.

If the operational model permits two admissible realization maps `rho_1,rho_2` for the same abstract witness, with distinct charged histories, then the witness semantics alone cannot determine a unique nonzero vector lower bound in `(R,I,A,L)`.

**Proof.** The abstract input/output relation and verification predicate are identical under `rho_1` and `rho_2`, while the charged physical histories differ. Any bound inferred solely from the abstract witness must assign the same value to both. Therefore a realization-sensitive physical quantity cannot be recovered from witness semantics alone. A universal strictly positive bound additionally fails whenever the declared model contains a reversible/free realization of the witness or treats the relevant physical resource as uncharged. QED.

### Dimensional audit — PROVED
Bits, queries, gates, description length and time steps cannot be inserted directly into a physical `(R,I,A,L)` inequality unless a substrate map supplies the corresponding physical dimensions. Thus a statement such as

\[
\Omega_G \le F(\Delta R,\Delta I,\Delta A,\Delta L,K)
\]

is ill-typed when `K` is an abstract complexity measure and the other coordinates are physical quantities, unless the model explicitly defines a dimensionally valid conversion/realization map.

### Conditional physical bounds — IMPORTED/KNOWN
Once a substrate and thermodynamic protocol are fixed, genuine implementation lower bounds can exist. Landauer-type bounds constrain logically irreversible erasure; modern work also studies process work costs and complexity-constrained thermodynamic implementation. These are important ingredients for GC-II but cannot be relabeled as a new universal witness theorem.

## 2026 collision check
1. Wang et al. (2026), *Quantum Landauer erasure using magnetic tunneling junctions*, experimentally reports quasi-adiabatic bit-reset dissipation approaching `kT ln 2` in an STT-MTJ implementation. DOI: 10.1039/d5na01057h.
2. Shimizu et al. (2026), *Thermodynamic Constraints in Dynamic Random-Access Memory Cells*, Phys. Rev. Lett. 136, 117103, experimentally finds implementation-specific constraints preventing DRAM erasure from reaching the Landauer limit. DOI: 10.1103/1sgm-dhys.
3. Whitelam (accepted 18 Aug 2026), *Evolutionary design of thermodynamic logic gates and their heat emission*, emphasizes that practical thermodynamic cost depends strongly on the physical control implementation.
4. Faist et al. (2025), *Complexity-Constrained Quantum Thermodynamics*, PRX Quantum 6, 010346, explicitly links process-complexity restrictions to thermodynamic work tradeoffs. DOI: 10.1103/PRXQuantum.6.010346.
5. Meier & Yamasaki (2025), *Energy-Consumption Advantage of Quantum Computation*, PRX Energy 4, 023008, develops model-specific links between query/information structure and energy-consumption lower bounds. DOI: 10.1103/PRXEnergy.4.023008.

These collisions are decisive against novelty of the generic statement “executing a computational witness necessarily has a physical lower bound.”

## Edge and degenerate cases
- Identity/no-op witness: strict positive universal bound fails.
- Reversible realization: logical irreversibility cannot be assumed from witness semantics.
- Free-oracle/advice interface: witness-generation cost can be shifted outside the declared boundary.
- Preinstalled lookup table: online computation cost can collapse while preparation/storage cost moves elsewhere.
- Amortized repeated use: one-time construction cost need not remain a per-instance lower bound.
- Different temperatures/substrates: energy bounds change, so an architecture-free numerical energy invariant is impossible.
- Randomized witness: correctness/error must be included in the operational task definition before comparing costs.
- Catalyst/ancilla returned unchanged: gross use and net consumption must be distinguished.

## Consequence for Paper II
The sequence of Audits 072–082 now identifies a recurring no-go boundary:

> Abstract capability, convertibility, closure, witness, or complexity structure does not by itself determine a nonzero typed physical augmentation. A physical bound requires an explicit realization model; once that model is fixed, the claim must be separated from existing reachability, resource, computation, information, control and thermodynamic lower-bound theories.

This is a useful negative theorem family, but not yet the requested breakthrough.

## Surviving target
**OPEN — Representation-independent closure deficiency relative to a declared physical realization class.**

Rather than asking for a universal cost of an abstract witness, define a *class* `P` of physically admissible realizations with explicit boundary conditions and quotient by semantics-preserving recompilation. The next candidate is a minimax deficiency

\[
\Omega_{\mathcal P}(S\to q;B,\epsilon)
=\inf_{\rho\in\mathcal P}\;\inf_{h\in H_\rho(S\to q,\epsilon)} C_\rho(h),
\]

followed by a theorem only if a lower bound survives the entire declared realization class. The scientific burden is to prove that such a lower bound is neither merely Landauer/process work, ordinary communication/query complexity, reachability, nor a definition-induced infimum.

### Required next attack
Construct a finite family with at least two semantics-equivalent realizations and compute the full minimax frontier exactly; then search for a lower bound invariant under realization changes. If every candidate reduces to an established monotone or can be driven to zero by a reversible realization, record the corresponding no-go theorem rather than claiming novelty.

## Status table
| Claim | Status |
|---|---|
| Abstract witness alone determines typed physical cost | FALSIFIED |
| Realization-dependence theorem | PROVED |
| Dimensional compatibility requirement | PROVED |
| Landauer/process-work implementation bounds | IMPORTED/KNOWN |
| Architecture-independent strictly positive witness cost | FALSIFIED |
| Realization-class minimax closure deficiency | OPEN |
| GC-II breakthrough | OPEN / NOT ESTABLISHED |
