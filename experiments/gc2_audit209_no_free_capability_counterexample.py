"""GC-II Audit 209: exact zero-work strict closure-escape witness."""
from fractions import Fraction
from heapq import heappush, heappop

X = ("x", "y")

def ident(s): return s
def generate(s): return "y" if s == "x" else "y"

G0 = (("id", ident, Fraction(0)),)
G1 = (("id", ident, Fraction(0)), ("g", generate, Fraction(0)))

def closure(start, gens, budget):
    best = {start: Fraction(0)}
    pq = [(Fraction(0), start)]
    while pq:
        cost, s = heappop(pq)
        if cost != best[s]: continue
        for _, f, w in gens:
            nc, t = cost + w, f(s)
            if nc <= budget and (t not in best or nc < best[t]):
                best[t] = nc
                heappush(pq, (nc, t))
    return best

for B in map(Fraction, (0, 1, 17)):
    c0 = closure("x", G0, B)
    c1 = closure("x", G1, B)
    assert set(c0) == {"x"}
    assert set(c1) == {"x", "y"}
    assert c1["y"] == 0
    # Enriched transcript explicitly exposes measured generator work.
    transcript = ("generator", "g", "work", c1["y"], "result", "y")
    assert transcript[3] == 0

print("Audit 209 PASS: strict budgeted closure escape with exact measured work 0")
