from gc2.omega_gap import Context, Edge, omega_path_formula


def test_current_nonlinear_omega_fails_triangle_inequality():
    """Exact counterexample: R/I complementarity makes Omega_G nonmetric."""
    edges = [
        Edge(0, 1, (1,)),
        Edge(1, 2, (0,), info=frozenset({"i"})),
    ]
    baseline = Context((0,))

    d_xy = omega_path_formula(edges, [0], baseline, 1, max_steps=2)
    d_yz = omega_path_formula(edges, [1], baseline, 2, max_steps=2)
    d_xz = omega_path_formula(edges, [0], baseline, 2, max_steps=2)

    assert d_xy == 1
    assert d_yz == 1
    assert d_xz == 3
    assert d_xz > d_xy + d_yz
