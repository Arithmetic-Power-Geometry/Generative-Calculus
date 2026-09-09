# Audit 035 — Whole-envelope simultaneity collision

Audit 034 proposed a quantitative whole-envelope simultaneity penalty. This audit tests whether such a penalty is itself GC-II-specific.

## Exact witness
Let S=(S1,...,Sm) be independent uniform bits. Singleton task Ti asks for Si with zero error. One bit solves each singleton, so C(Ti)=1.

A common whole-envelope translator message M must permit recovery of every Si simultaneously. Zero error gives H(S|M)=0, hence

H(M) >= I(S;M) = H(S)-H(S|M) = m.

Sending M=S achieves m bits, so C(all)=m exactly. Thus a parametric simultaneity penalty exists even with a fixed graph, fixed preconditions, no structural rewrite, and no cross-axis gating.

For any subset J of q independent bits the same argument gives C(J)=q. Shared randomness independent of S cannot remove this zero-error requirement. Correlation can reduce the joint entropy; identical tasks collapse the penalty; nonzero-error variants require the corresponding approximate information bounds.

## Collision
The mechanism is classical rather than GC-specific. Direct-sum and direct-product theory studies the cost of solving multiple instances together. Simultaneous-message communication studies simultaneous transmission requirements. Index coding studies one broadcast satisfying multiple demands with side information, including exact linear regimes characterized by minrank. Multiterminal rate-distortion likewise treats joint demands under distortion constraints.

Therefore a parametric whole-envelope simultaneity penalty does not imply GC-II novelty.

Classification: **PROVED witness / IMPORTED-KNOWN mechanism / FALSIFIED as a standalone breakthrough criterion**.

## Consequence
A raw gap such as C(all)-max_i C(Ti) can be arbitrarily large for ordinary information-theoretic reasons. A defensible Omega_G cannot call this residual GC novelty without controlling the strongest neighboring joint-demand explanation.

A provisional research quantity is

Omega_G_res = C_G(all) - C_N_star(all | matched ordinary structure),

where N is a comparison class fixed independently of the candidate. This is OPEN and positivity alone would not prove novelty.

## Stronger next target
Match the entire ordinary joint-demand problem, not merely singleton tasks: same state/transition graph, action preconditions, joint source or deterministic demand relation, costs for every declared subset of tasks, and physical budget model. Then vary only a GC whole-envelope ingredient such as scale-indexed error-budget compatibility under composition. Seek a provable convertibility or Pareto-cost separation and collision-test it against direct-sum/direct-product results, simultaneous-message communication, index coding, multiterminal rate-distortion, resource theories, and robust/viability control.

## Status delta
- Parametric simultaneity penalty: **PROVED**.
- Entropic/direct-sum mechanism: **IMPORTED/KNOWN**.
- Simultaneity penalty alone as GC-II breakthrough: **FALSIFIED**.
- Residual novelty gap against a fixed strongest comparison class: **OPEN**.
- GC-specific scale-error-budget compatibility separation after matching full ordinary joint-demand structure: **OPEN**.