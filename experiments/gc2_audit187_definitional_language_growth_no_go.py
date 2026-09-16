"""GC-II Audit 187: definitional action-language growth is closure-conservative.

Question
--------
Audit 186 left open growth of the admissible transformation language itself.
Does adding newly generated actions create extensional capability?

Theorem (Macro Conservativity)
------------------------------
Let G have primitive actions A with compositional semantics [[.]] and additive
cost vector c in R_+^d. Extend the language by a new symbol m whose semantics is
exactly an existing admissible word w=a1;...;ak, and assign
c(m)=sum_i c(ai). Then replacing every occurrence of m by w preserves endpoint
and total cost vector. Conversely every old execution remains available.
Therefore for every start state x and budget b,

    Closure_G(x,b) = Closure_{G+m}(x,b).

The result iterates to any finite set of definitional macros. Hence purely
syntactic/library growth cannot create new extensional budgeted closure when
macro costs faithfully equal their expansions.

Boundary cases
--------------
* If m receives a discounted cost, budgeted closure can expand, but the cause is
  a changed cost/accounting rule rather than new extensional transformation.
* If m has semantics not realizable by any old admissible word, it is not a
  definitional macro: genuine primitive/physical/oracle expansion has occurred.
* If w was semantically realizable but forbidden by an interface/rule, adding m
  changes admissibility, again not mere definitional compression.
* Under bounded description length, planning horizon, wall-clock search, or
  computational limits, macros can change practical/intensional capability.
  That is a complexity/representation effect, not extensional closure escape.
* Zero-cost actions and vector costs are allowed; nonnegative additivity is
  enough for the budget statement.

Prior-art boundary
------------------
Macro-operators and library learning explicitly add reusable abstractions to
planning/program-synthesis languages to shorten search/descriptions. DreamCoder,
Stitch/Top-Down Synthesis, AbstractBeam, and recent TAMP macro-operator learning
occupy this territory. Thus 'growing the action language' is not by itself a
GC-II breakthrough.

Status
------
* cost-faithful definitional macro conservativity: PROVED.
* definitional language growth as extensional Closure-Escape mechanism: FALSIFIED.
* macros improving bounded-search/intensional capability: IMPORTED/KNOWN mechanism.
* capability growth from genuinely non-definitional transformations: OPEN; this
  must explicitly charge acquisition of new semantics/physics/oracles/rules.

The exhaustive check below enumerates small deterministic finite systems and
verifies endpoint/cost identity for old words versus macro-expanded words.
"""
from itertools import product


def run(trans, costs, s, word):
    cost = 0
    for a in word:
        s = trans[a][s]
        cost += costs[a]
    return s, cost


def expand(word, macro_name, macro_word):
    out = []
    for a in word:
        out.extend(macro_word if a == macro_name else (a,))
    return tuple(out)


def verify(n_states=2, max_old_word=3, max_new_word=3):
    actions = ("a", "b")
    checked = 0
    # all deterministic transition maps for two primitive actions
    maps = list(product(range(n_states), repeat=n_states))
    for ta in maps:
        for tb in maps:
            trans = {"a": ta, "b": tb}
            for ca in range(3):
                for cb in range(3):
                    costs = {"a": ca, "b": cb}
                    for k in range(1, max_old_word + 1):
                        for macro_word in product(actions, repeat=k):
                            # compile macro semantics as its expansion
                            m_next = []
                            for s in range(n_states):
                                m_next.append(run(trans, costs, s, macro_word)[0])
                            ext_trans = dict(trans, m=tuple(m_next))
                            ext_costs = dict(costs, m=sum(costs[a] for a in macro_word))
                            alphabet = actions + ("m",)
                            for ell in range(max_new_word + 1):
                                for word in product(alphabet, repeat=ell):
                                    old = expand(word, "m", macro_word)
                                    for s in range(n_states):
                                        assert run(ext_trans, ext_costs, s, word) == run(trans, costs, s, old)
                                        checked += 1
    return {"n_states": n_states, "checks": checked}


if __name__ == "__main__":
    print(verify())
