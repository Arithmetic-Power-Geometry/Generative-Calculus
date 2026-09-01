import math
from generative_calculus.core import (
    blackwell_binary_deficiency,
    canonical_reachability_system,
    convex_reconstruction_identity,
    cyclic_reversal_cost,
    equality_costs,
    exact_program_qubits,
    feasible,
    generative_order_parity,
    marginal_incompleteness_example,
    pareto_frontier,
    parity_envelopes,
    proper_projection_agreement,
    reachable_transport_audit,
)


def test_pareto_removes_dominated():
    assert pareto_frontier([(1,3),(3,1),(4,4),(2,3)]) == [(1.0,3.0),(3.0,1.0)]


def test_feasible():
    F=[(1,3),(3,1)]
    assert feasible(F,(1,3))
    assert not feasible(F,(1,1))


def test_marginal_incompleteness():
    ex=marginal_incompleteness_example()
    assert ex['marginal_A']==ex['marginal_B']==(1.0,1.0)
    assert not ex['A_feasible'] and ex['B_feasible']


def test_blackwell_better_to_worse_exact():
    assert blackwell_binary_deficiency(.9,.75) == 0


def test_blackwell_worse_to_better_gap():
    assert abs(blackwell_binary_deficiency(.75,.9)-.15) < 1e-12


def test_equality_scaling():
    a=equality_costs(64,1/3); b=equality_costs(128,1/3)
    assert b['deterministic_bits'] > a['deterministic_bits']
    assert b['public_randomized_proxy_bits']==a['public_randomized_proxy_bits']


def test_parity_envelopes_disjoint_and_equal_size():
    even, odd = parity_envelopes(5)
    assert even.isdisjoint(odd)
    assert len(even) == len(odd) == 16


def test_every_proper_projection_agrees():
    for m in range(2,8):
        assert proper_projection_agreement(m)


def test_unbounded_generative_order_family():
    for m in range(2,8):
        assert generative_order_parity(m) == m


def test_convex_reconstruction_machine_precision():
    r=convex_reconstruction_identity([(0,0),(2,0),(0,1)],[(0,0),(1,0),(0,3)],t=.73,steps=37)
    assert r['max_abs_error'] < 1e-12


def test_cyclic_reversal_exponential():
    a=cyclic_reversal_cost(5); b=cyclic_reversal_cost(6)
    assert a['reverse_via_forward_cost'] == 31
    assert b['reverse_via_forward_cost'] == 63
    assert b['reverse_via_forward_cost'] > a['reverse_via_forward_cost']


def test_program_qubits():
    assert exact_program_qubits(1)==0
    assert exact_program_qubits(2)==1
    assert exact_program_qubits(3)==2
    assert exact_program_qubits(1024)==10


def test_reachable_transport_theorem_finite_system():
    graph, task_at=canonical_reachability_system()
    rows=reachable_transport_audit(graph,task_at,max_budget=12)
    assert rows and all(r['transport_holds'] for r in rows)


def test_generated_benchmark_shapes(tmp_path):
    from generative_calculus.benchmarks import run_all
    s=run_all(tmp_path)
    assert s['binary_sensor_rows']==5
    assert s['equality_rows']==8
    assert s['hierarchy_rows']==20
    assert s['projection_rows'] > 0
    assert s['reachable_transport_all_hold']
