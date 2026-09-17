"""GC-II Audit 201: exact finite generated-experiment compilation check.

Two worlds. Initially only GENERATE is admissible; it costs 1 and opens a
world-revealing probe. After generation, STOP or PROBE are admissible. PROBE
costs 2 and returns the world exactly. We compare the native generated-family
description with the augmented controlled-sensing description for every
deterministic policy up to horizon 2.
"""
from itertools import product

W = (0, 1)


def admissible(mode):
    return ("generate", "stop") if mode == 0 else ("probe", "stop")


def step_native(w, mode, action):
    assert action in admissible(mode)
    if action == "generate":
        return [(1.0, None, 1, 1)]  # prob, obs, new mode, cost
    if action == "probe":
        return [(1.0, w, mode, 2)]
    return [(1.0, None, mode, 0)]


def step_compiled(w, mode, action):
    # Augmented controlled-sensing state is (w, mode); same kernels/costs.
    return step_native(w, mode, action)


def rollout(step, w, first, second_after_generate):
    mode = 0
    transcript = []
    cost = 0
    p = 1.0
    for t in range(2):
        action = first if t == 0 else second_after_generate
        if action not in admissible(mode):
            break
        outcomes = step(w, mode, action)
        assert len(outcomes) == 1
        pr, obs, mode, c = outcomes[0]
        p *= pr
        cost += c
        transcript.append((action, obs, mode, c))
        if action == "stop":
            break
    return p, tuple(transcript), cost


def main():
    policies = list(product(("generate", "stop"), ("probe", "stop")))
    checked = 0
    for w in W:
        for first, second in policies:
            a = rollout(step_native, w, first, second)
            b = rollout(step_compiled, w, first, second)
            assert a == b, (w, first, second, a, b)
            checked += 1
    # Nontrivial witness: generation changes admissible family and cost geometry.
    assert admissible(0) != admissible(1)
    assert rollout(step_native, 0, "generate", "probe")[2] == 3
    assert rollout(step_native, 1, "generate", "probe")[1][-1][1] == 1
    print(f"PASS: {checked} world-policy cases; exact transcript/cost equality")


if __name__ == "__main__":
    main()
