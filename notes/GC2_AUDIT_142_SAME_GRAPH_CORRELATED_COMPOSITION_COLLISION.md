# GC-II Audit 142 — Same One-Shot Graph Can Hide Composition Structure, but the Separation Collides with Channels with Memory

## Gate tested
Audit 141 asked for two finite operational worlds with the same induced one-shot confusability graph but different compositional capability because operational constraints change which product witnesses are realizable.

## Exact finite construction
Let the one-shot task class be c in {0,1}, nuisance n in {0,1}, and observed output y = c XOR n. In either world, when n is unrestricted in a single use, each class can produce both outputs {0,1}. Thus the one-shot confusability graph in both worlds is K2 and alpha(K2)=1.

Now compare two-use operational laws.

WORLD S (shared nuisance): the same hidden nuisance bit n is used in both positions,

    (y1,y2) = (c1 XOR n, c2 XOR n).

For input word 00 the possible outputs are {00,11}; for 01 they are {01,10}. These supports are disjoint. Hence 00 and 01 are exactly distinguishable and the two-use zero-error code size is at least 2. In fact each word is confusable only with its bitwise complement, so the four input words split into two complement pairs and alpha=2 exactly.

WORLD I (independent nuisance): independent nuisance bits n1,n2 are available,

    (y1,y2) = (c1 XOR n1, c2 XOR n2).

Every input word can produce every output word. The two-use confusability graph is K4 and alpha=1.

Therefore the worlds have identical one-shot confusability graph K2 but different two-use exact capability:

    alpha_S^(2)=2 != 1=alpha_I^(2).

This proves that the one-shot confusability graph is not a sufficient statistic for composition when the operational law contains cross-use correlation/memory.

## Why this is not yet GC-II novelty
The separation does not survive the required prior-art collision. It is exactly the kind of phenomenon studied by channels with memory / correlated-noise channels: once cross-use state or noise correlation is admitted, the memoryless strong-product construction is no longer the complete channel description. Zero-error capacity of binary channels with memory is an established subject, including finite-memory and 1-/2-memory models. Thus the extra carrier retained by the operational world is real, but here it is ordinary channel memory/correlation, not a new Generative Calculus invariant.

Equivalently, augmenting the channel state with the nuisance/memory variable restores a standard finite-state channel representation. The one-shot graph loses that state only because it was projected away.

## Ledger
- Same one-shot confusability graph with different two-use capability: PROVED by explicit finite construction.
- WORLD S two-use code size 2: PROVED.
- WORLD I two-use code size 1: PROVED.
- One-shot confusability graph as sufficient statistic under correlated composition: FALSIFIED.
- Correlated-noise / channel-memory explanation: IMPORTED/KNOWN.
- This separation as GC-II breakthrough novelty: FALSIFIED.
- GC-specific composition obstruction surviving finite-state channel augmentation: OPEN.

## Next gate
The next candidate must not merely hide a finite nuisance/memory state. Search for an operational separation where (i) one-shot observable/confusability structure agrees, (ii) finite continuation-state augmentation up to the relevant budget also agrees or is explicitly controlled, yet (iii) admissible capability differs because resource/action/interface/rule constraints restrict the realizability of transformations rather than only correlating channel outputs. Any candidate must then be collision-tested against finite-state channels, arbitrarily varying channels, causal channels, process/resource theories, communication complexity, and simulation preorders before receiving a novelty claim.