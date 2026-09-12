from collections import defaultdict
import csv
from pathlib import Path


def delta(state: int, bit: int, n: int) -> int:
    mask = (1 << n) - 1
    return ((state << 1) | bit) & mask


def minimize_state_count(n: int) -> int:
    states = set(range(1 << n))
    accepting = {s for s in states if (s >> (n - 1)) & 1}
    partition = [accepting, states - accepting]
    partition = [block for block in partition if block]

    changed = True
    while changed:
        changed = False
        block_id = {}
        for i, block in enumerate(partition):
            for state in block:
                block_id[state] = i

        refined = []
        for block in partition:
            groups = defaultdict(set)
            for state in block:
                signature = tuple(block_id[delta(state, bit, n)] for bit in (0, 1))
                groups[signature].add(state)
            refined.extend(groups.values())
            if len(groups) > 1:
                changed = True
        partition = refined

    return len(partition)


def main() -> None:
    output = Path("results/gc2_realization_complexity_collision.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for n in range(1, 9):
        observed = minimize_state_count(n)
        expected = 1 << n
        rows.append(
            {
                "n": n,
                "constructed_states": expected,
                "minimized_states": observed,
                "expected_2_pow_n": expected,
                "match": int(observed == expected),
            }
        )
        assert observed == expected

    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"verified {len(rows)} cases; all minimal counts equal 2^n")


if __name__ == "__main__":
    main()
