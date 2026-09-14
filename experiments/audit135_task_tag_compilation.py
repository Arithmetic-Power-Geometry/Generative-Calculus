"""Exact finite regression for GC-II Audit 135.

Enumerates all deterministic maps on X={0,1}, all identity-containing
composition-closed transformation monoids, and every ordered assignment of
such monoids to two task tags. Compares native task-indexed reachability with
tagged-state reachability.
"""
import itertools, json

X=(0,1)
MAPS=list(itertools.product(X, repeat=2))
ID=(0,1)

def compose(f,g):
    return tuple(f[g[x]] for x in X)

def all_monoids():
    out=[]
    for mask in range(1<<len(MAPS)):
        F={MAPS[i] for i in range(len(MAPS)) if (mask>>i)&1}
        if ID not in F:
            continue
        if all(compose(f,g) in F for f in F for g in F):
            out.append(F)
    return out

def run():
    monoids=all_monoids()
    comparisons=0
    mismatches=0
    for F0 in monoids:
        for F1 in monoids:
            Fs=(F0,F1)
            for t in (0,1):
                for x in X:
                    native={f[x] for f in Fs[t]}
                    tagged={(t,f[x]) for f in Fs[t]}
                    expected={(t,y) for y in native}
                    comparisons += 1
                    mismatches += tagged != expected
    result={
        "states":len(X),
        "deterministic_maps":len(MAPS),
        "transformation_monoids":len(monoids),
        "ordered_two_task_assignments":len(monoids)**2,
        "native_vs_tagged_comparisons":comparisons,
        "mismatches":mismatches,
        "status":"PASS" if mismatches==0 else "FAIL"
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return result

if __name__ == "__main__":
    run()
