# GC-II Audit 176 — Finite Product-Compilation No-Go

## Question
Can coupling communication/information, resources, mutable interfaces/actions, and rules produce a capability distinction that survives ordinary finite-state compilation?

## Model
Let a finite GC operational system have state

\[
s=(x,r,i,\ell),
\]

where `x` is physical/task state, `r` is a finite resource state, `i` is a finite information/communication state, and `ell` is a finite interface/rule state. For each action `a`, admissibility and update are functions/relations of the current tuple. Assume Markov sufficiency: the tuple contains all information required to determine future admissibility and transition behavior.

## Theorem candidate: finite product-compilation no-go
**Status: PROVED under the stated finite Markov assumptions; IMPORTED/KNOWN mechanism.**

Every such coupled system is behaviorally identical to an ordinary finite transition system/game on the product state space

\[
S=X\times R\times I\times L.
\]

### Proof
For every product state `s` and action `a`, place an edge `s --a--> s'` exactly when the original coupled semantics declares `a` admissible at `s` and permits successor `s'`. This preserves, by induction on trace length, exactly the finite traces and their state labels. Infinite traces are preserved because the one-step transition relation is identical. Therefore every reachability, safety, omega-regular, finite-horizon budget-feasibility, and strategy property defined on this semantics is preserved. Conversely the product transition system is merely an extensional listing of the original transition relation. QED.

## Consequence
Under these assumptions, merely coupling R/I/A/L cannot yield a new invariant. Any claimed residual must rely on structure excluded by the theorem assumptions or on a restriction on allowed compilers/observers/strategies. State-space blow-up alone is representation complexity.

## Exact finite check
`experiments/gc2_audit176_product_compilation_no_go.py` constructs a 12-state example `(q,r,i)` where interface mutation and resource consumption are coupled. Independent explicit enumeration gives exactly the same 12 transitions as the endogenous semantics. The script asserts equality.

## Stress checks
- **Degenerate resources:** singleton `R` reduces to ordinary finite transition semantics.
- **Static interfaces:** singleton `L` removes rule mutation without changing the proof.
- **Zero communication:** singleton `I` removes information coupling.
- **Nondeterminism:** replace update functions by finite successor relations; the construction is unchanged.
- **Composition:** synchronous/asynchronous finite products remain finite product transition systems once scheduler/channel state is included.
- **Cycles/replenishment:** allowed; they are represented as ordinary edges.
- **Unreachable product tuples:** may be removed after reachability analysis without changing behavior from the initial state.
- **Partial observation:** observation maps must be retained; this produces a finite imperfect-information game rather than escaping compilation.

## Prior-art collision boundary
The mechanism is standard finite-state game/model-checking compilation. Concurrent games already use finite state with joint choices; consumption/energy games attach multidimensional resource updates and reloads to finite-state transitions; communicating automata and distributed synthesis already treat communication-state restrictions. Therefore the theorem is useful as a GC-II **no-go boundary**, not as a novelty claim.

## What can still escape
A genuine GC-II residual must violate at least one compilation premise in a scientifically defensible way, e.g.:
1. unbounded/non-finitely representable endogenous rule or interface state;
2. a uniform family where compilation size/communication/resource cost has a new lower bound not reducible to automata/communication/energy-game complexity;
3. semantic generation of genuinely new task/action descriptions with an explicitly restricted interpreter class;
4. non-Markov operational semantics for which no bounded sufficient state exists;
5. a coupled quantitative law whose observable prediction is not determined by the compiled transition/game semantics.

## Ledger
- finite Markov R/I/A/L product compilation — **PROVED / IMPORTED-KNOWN mechanism**;
- coupling alone as independent GC-II novelty — **FALSIFIED**;
- finite interface mutation escaping compilation — **FALSIFIED**;
- state-space explosion alone as capability novelty — **FALSIFIED**;
- non-finitely compilable endogenous closure — **OPEN**;
- coupled quantitative law beyond compiled behavior — **OPEN**.

## Next attack
Search for the weakest operational assumption under which a non-finitely-compilable closure can still be measured and falsified experimentally. In parallel, test whether reversibility gap survives this no-go: if reversibility is computed solely from the compiled transition graph plus costs, it too is imported path/game structure; a surviving invariant must depend on an operationally observable asymmetry not recoverable from those data.
