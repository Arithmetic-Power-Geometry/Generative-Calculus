# Q-ary whole-envelope projection ambiguity

Status: **PROVED** as a finite GC structural strengthening.  Novelty status: **not a breakthrough claim**; the combinatorial skeleton is classical single-parity-check / orthogonal-array territory.

## Statement

For integers `q >= 2` and `m >= 2`, define, for each residue `a in Z_q`,

`E_a = {x in Z_q^m : sum_i x_i = a (mod q)}`.

Then:

1. the `q` sets `E_a` are pairwise disjoint and partition `Z_q^m`;
2. each has cardinality `q^(m-1)`;
3. for every nonempty strict coordinate set `S subsetneq {1,...,m}`, every projection `pi_S(E_a)` equals the full cube `Z_q^|S|`, independently of `a`;
4. therefore all strict coordinate projections fail to distinguish `q` mutually disjoint whole envelopes, while the full `m`-coordinate relation distinguishes them;
5. the minimum distinguishing projection order is `m`, and a uniformly distributed hidden whole-envelope label contains `log2(q)` bits not determined by the entire collection of strict coordinate projections.

## Proof

Disjointness and partition follow because every vector has exactly one checksum residue.  Fix a strict coordinate set `S` and an arbitrary assignment on `S`.  At least one coordinate `j` is omitted.  Assign all other omitted coordinates arbitrarily (zero is sufficient), then choose coordinate `j` uniquely modulo `q` so that the total checksum equals `a`.  Thus every assignment on `S` extends to a member of every `E_a`, so `pi_S(E_a)=Z_q^|S|`.  The cardinality is consequently `q^(m-1)`, since the first `m-1` coordinates may be chosen freely and the last coordinate is uniquely fixed by the checksum.  Since every strict projection agrees and the full relations are disjoint, the first distinguishing order is exactly `m`.  Under a uniform prior on `a`, the unresolved label entropy is `log2(q)` bits.

## Kill test / prior-art boundary

This strengthens the repository's binary parity pair from two hidden whole envelopes to an arbitrarily large finite ambiguity multiplicity `q`.  It does **not** establish a new combinatorial phenomenon: parity-check codes and orthogonal arrays already encode closely related projection properties.  Therefore this result may be used as a sharper GC stress test and falsification benchmark, but not as stand-alone evidence of foundational novelty.

The current breakthrough target remains stronger: a whole-envelope invariant, impossibility theorem, or same-input quantitative prediction whose content cannot be reduced to coding/orthogonal-array structure, Pareto geometry, Blackwell/Le Cam comparison, resource conversion, GPT simulation, reachability, or standard complexity/physical-computation results.

## Machine audit

Implementation: `src/generative_calculus/projection_lab.py`

Tests: `tests/test_projection_lab.py`

Finite audit table: `results/tables/qary_projection_ambiguity.csv` for `q=2,...,5` and `m=2,...,5`.
