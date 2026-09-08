import math

from generative_calculus.projection_lab import (
    all_strict_projections_identical,
    checksum_family,
    checksum_projection_audit,
)


def test_qary_checksum_family_partitions_and_projects_identically():
    for q in range(2, 6):
        for m in range(2, 6):
            fam = checksum_family(q, m)
            assert len(fam) == q
            assert all(len(E) == q ** (m - 1) for E in fam)
            assert set().union(*fam) == set(
                tuple(x)
                for x in __import__('itertools').product(range(q), repeat=m)
            )
            assert all_strict_projections_identical(q, m)


def test_qary_projection_audit_quantities():
    for q, m in [(2, 4), (3, 4), (5, 3)]:
        row = checksum_projection_audit(q, m)
        assert row['number_of_whole_envelopes'] == q
        assert row['class_size'] == q ** (m - 1)
        assert row['partition_complete']
        assert row['pairwise_disjoint']
        assert row['all_strict_projections_identical']
        assert row['minimum_distinguishing_projection_order'] == m
        assert math.isclose(row['whole_label_information_bits'], math.log2(q))
