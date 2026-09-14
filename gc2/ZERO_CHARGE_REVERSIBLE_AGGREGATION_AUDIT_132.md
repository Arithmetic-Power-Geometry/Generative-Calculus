# GC-II Audit 132 — Zero-Charge Reversible Aggregation

## Question
Does bare GC-II operational closure force a strictly positive charge `c_min > 0` for every genuinely capability-expanding aggregation?

## Result
**No. The claim is FALSIFIED without an additional resource/physical axiom.**

Consider the reversible three-bit Toffoli transformation

`T(x,y,z) = (x,y,z XOR (x AND y))`.

It is a bijection and an involution. With a clean ancilla `z=0`,

`T(x,y,0) = (x,y,x AND y)`.

Thus the transformation retains both primitive inputs while making their joint conjunction explicitly available at the interface. In the operational sense relevant to Audit 131, this is a nontrivial two-source aggregation. Yet nothing in bare reachability/closure semantics assigns it a strictly positive typed charge. An admissible accounting model may assign charge zero unless positivity is independently imposed or derived from a resource monotone or physical implementation constraint.

Therefore the implication

`capability-expanding aggregation => charge >= c_min > 0`

cannot follow from closure, admissibility, reversibility, finite state, or information preservation alone.

## Exact finite check
`experiments/gc2_zero_charge_reversible_aggregation_audit.py` checks all 8 input states for bijectivity and involutivity, and all 4 clean-ancilla input pairs for exact AND realization. Expected result: 0 AND mismatches.

## Consequence for Audit 131
The charged-support theorem from Audit 131 remains mathematically correct **conditional on** a positive minimum aggregation charge. Audit 132 shows that the positivity premise is not derivable from the current abstract operational axioms. Hence it cannot yet be promoted to an unconditional No-Free-Capability law.

## Prior-art collision
This boundary is consistent with reversible computation: logically reversible transformations need not possess a positive Landauer erasure cost merely because they compute a nontrivial function when inputs/ancillas are retained. It is also consistent with resource theories, where 'free' operations are defined by the chosen resource structure and typically cannot generate the designated resource from free states; positivity requires specifying what resource is being conserved or consumed.

## Status ledger
- Toffoli bijection/involution: **PROVED / exact finite verification**.
- Clean-ancilla conjunction realization: **PROVED / exact finite verification**.
- Strict positive charge from bare operational closure: **FALSIFIED**.
- Audit-131 support bound given `c_min>0`: **PROVED, CONDITIONAL premise retained**.
- Universal No-Free-Capability theorem without a resource monotone/physical axiom: **FALSIFIED in this form**.
- Search for a typed, operationally justified monotone whose increase lower-bounds capability expansion: **OPEN**.

## Next surviving route
Replace assumed positive event charge by a typed monotone balance. Seek a theorem of the form

`Omega_G <= F(Delta R, Delta I, Delta A, Delta L)`

where every claimed positive lower bound is tied to a declared monotone or inaccessible free-state boundary, and explicitly allow reversible zero-erasure computation as a zero-cost edge case. The theorem must distinguish *rearranging already available joint information* from *acquiring a genuinely unavailable operational resource*.
