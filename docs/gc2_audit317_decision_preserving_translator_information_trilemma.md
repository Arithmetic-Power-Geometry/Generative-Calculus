# GC-II Audit 317 — Decision-preserving translator information trilemma

## Status

- Finite decision-preserving translator lower bound: **PROVED**.
- Confusability-graph / chromatic-number characterization: **PROVED**.
- Extra-information/resource/interface escape clause: **PROVED as an operational disjunction under the stated model**.
- Zero-error source-coding / communication-complexity mechanism: **IMPORTED/KNOWN**.
- Claim that the generic graph-coloring lower bound is novel: **NOT MADE**.
- Stronger GC-II theorem beyond standard zero-error communication/sufficient-statistic theory: **OPEN**.

## Purpose

Audit 316 ended with a precise target: connect robust irreducibility to budgeted operational closure. This audit supplies the clean finite operational bridge and, equally importantly, identifies its prior-art boundary.

The result says that a local translator which must preserve a specified family of downstream conversion decisions cannot arbitrarily compress the operational state. It must either carry enough distinguishing information, obtain additional admissible side information/resources/interfaces, or fail on at least one required decision.

## Model

Let `X` be a finite set of operational states. Let `D={d_1,...,d_m}` be a fixed family of required downstream decisions, with

`d_j : X -> Y_j`.

A translator has an internal message alphabet `M` and encoder

`T : X -> M`.

With no side information, downstream decision `d_j` is preserved exactly when there exists a decoder

`g_j : M -> Y_j`

such that

`g_j(T(x)) = d_j(x)` for every `x in X`.

The translator information budget is

`B_T = ceil(log_2 |M|)` bits.

This is a representation budget, not a physical-energy budget. Mixing these dimensions is explicitly forbidden.

## Decision-confusability graph

Define the graph `G_D=(X,E_D)` by

`{x,x'} in E_D` iff there exists `j` such that `d_j(x) != d_j(x')`.

Thus adjacent states must remain distinguishable if all decisions in `D` are to be exactly preserved.

## Theorem 317.1 — exact translator criterion

The following are equivalent:

1. `T` preserves every decision in `D`.
2. For every edge `{x,x'} in E_D`, `T(x) != T(x')`.
3. `T` is a proper coloring of `G_D` by message symbols.

Consequently the minimum possible message-alphabet size is exactly

`min |M| = chi(G_D)`,

and every exact translator obeys

`B_T >= ceil(log_2 chi(G_D))`.

### Proof

`1 => 2`: if `d_j(x) != d_j(x')` for some `j` but `T(x)=T(x')`, then the deterministic decoder `g_j` receives the same message for both states and cannot output both distinct required decisions, contradiction.

`2 => 3` is exactly the definition of proper coloring.

`3 => 1`: for each message/color `m`, all states in the color class have identical value under every `d_j`; otherwise two members would be adjacent. Define `g_j(m)` to be this common value. Then `g_j(T(x))=d_j(x)` for all `x`.

Minimizing the number of colors gives `chi(G_D)`.

## Corollary 317.2 — operational translator trilemma

Fix a translator budget `b` bits, so at most `2^b` messages are available. If

`2^b < chi(G_D)`,

then no translator using only the current local operational state and the fixed downstream decoders can preserve all decisions in `D`.

Therefore any successful architecture must do at least one of the following:

1. increase the translator information budget to at least `ceil(log_2 chi(G_D))` bits;
2. introduce additional admissible side information, resources, interfaces/actions, or rules that alter the effective decision-confusability relation;
3. relax/fail at least one required decision-preservation constraint.

This is the precise finite version of the GC-II translator trilemma.

The theorem does **not** say that extra physical resource automatically substitutes for bits. It says only that an expanded admissible operational model can change which states remain confusable at the translator boundary.

## Side-information version

Let admissible side information be `S:X->Z`, available to the downstream decoder in addition to `T(x)`. Exact preservation requires

`g_j(T(x),S(x))=d_j(x)`.

Define the residual graph `G_{D|S}` by connecting `x,x'` exactly when

`S(x)=S(x')`

and

`d_j(x) != d_j(x')` for some `j`.

Then the same proof gives

`|M| >= chi(G_{D|S})`.

Hence admissible side information can lower the required translator budget only by removing decision-confusable pairs inside equal-side-information fibers.

Two edge cases are exact:

- constant `S`: `G_{D|S}=G_D`, so side information gives no benefit;
- `S` itself determines every `d_j`: `G_{D|S}` has no edges, so one translator symbol suffices.

## Connection to budgeted operational closure

Represent an operational specification as

`O=(X, Tau, R, I, A, L)`

where `Tau` is the admissible transformation family, `R` resource budget, `I` admissible information, `A` interfaces/actions, and `L` rules/constraints.

For a fixed downstream decision family `D`, the current specification induces an effective residual confusability graph `G_D(O)`. A proposed closure-preserving local translator with `b` information bits is impossible whenever

`2^b < chi(G_D(O))`.

An operational extension

`O -> O'`

can escape this obstruction only if it changes at least one charged component sufficiently to reduce the residual confusability requirement or increases the translator budget. This is a finite computational certificate of failure of the proposed translator inside the old budgeted closure.

Importantly, this is not yet a universal Closure-Escape theorem: deciding which changes in `R,I,A,L` are admissible and how they alter `G_D` remains model-dependent.

## Relation to the Audit 313–316 reversibility family

Take a finite packing `P={x_1,...,x_N}` of operationally realizable cycle-coordinate states from Audit 316. If the downstream decision family is chosen so that every pair of packing states requires a different conversion decision somewhere, then `G_D` is complete and

`chi(G_D)=N`.

Thus an exact translator requires at least

`ceil(log_2 N)` bits.

Using Audit 316's packing with

`N = (floor(rho/(2 epsilon))+1)^beta`,

one recovers the robust scaling

`B_T >= beta log_2(floor(rho/(2 epsilon))+1)`

for any translator required to retain enough information to reconstruct/implement the corresponding epsilon-separated decision distinctions.

This shows that the earlier metric lower bound can be interpreted as a boundary-translation information requirement rather than merely a static representation statement.

## Dimensions and domain checks

- `chi(G_D)` and `|M|` are counts; their base-2 logarithms are measured in bits.
- Physical resources `R` are not added to information bits unless a separate operational conversion law is explicitly supplied.
- If all decisions are constant, `G_D` has no edges, `chi=1`, and the lower bound is zero bits.
- If every pair of states differs on some required decision, `G_D` is complete and the exact requirement is `ceil(log_2 |X|)` bits.
- Adding a required decision can only add graph edges, so `chi(G_D)` cannot decrease.
- Removing a required decision can only remove edges, so the required budget cannot increase.
- Adding side information can only delete residual edges relative to the no-side-information graph, so the minimum translator alphabet cannot increase.
- Relabeling states or decision outputs preserves the graph up to isomorphism and leaves the bound invariant.
- For independent products, chromatic numbers do not obey a universal additive identity without specifying the product/confusability semantics; no additive composition claim is made.

## Counterexample checks

### Cardinality alone is not the correct lower bound

A large state space can require zero translator bits when all required decisions are constant. Therefore `log_2 |X|` is not a universal requirement.

### Number of decisions alone is not the correct lower bound

One binary decision can split arbitrarily many states into only two decision classes and need one bit, while a family of decisions can jointly make `G_D` complete. The graph structure, not merely `m`, controls the exact zero-error requirement.

### Extra side information can defeat the original bound

If `S(x)` reveals the complete required decision vector, one message suffices. Hence any theorem omitting the admissible-information boundary would be false.

### Approximate preservation is different

Allowing decision error probability or distortion changes the problem to graph entropy, rate-distortion, information bottleneck, or communication-complexity variants. The exact chromatic-number statement is not extrapolated to that regime.

## Prior-art collision audit

The mathematical core collides directly with established zero-error information theory, graph coloring of confusability graphs, sufficient statistics, and one-way communication complexity. A deterministic exact message must separate inputs that require different outputs; graph coloring is a standard formulation of zero-error coding. Therefore:

- graph-coloring criterion: **IMPORTED/KNOWN mechanism**;
- logarithmic message lower bound: **IMPORTED/KNOWN mechanism**;
- generic claim that a decision-preserving translator must transmit enough information: **NOT NOVEL**.

Blackwell/Le Cam comparison similarly formalizes when one experiment/statistic is sufficient for decision problems. The present audit should therefore be used as a rigorous GC-II bridge and diagnostic, not advertised as a standalone foundational novelty theorem.

The possible GC-II novelty target remains narrower: a theorem in which the budgeted closure itself induces a nontrivial, computable obstruction tying transformation/resource/interface constraints to a decision-confusability or deficiency quantity in a way not reducible to standard coding or experiment comparison.

## Scientific consequence

Audit 317 validates a necessary architecture for any future Closure-Escape claim:

`closure restriction -> residual decision confusability -> translator lower bound -> charged escape channel`.

But the generic finite theorem is already contained in known zero-error/communication ideas. Therefore this audit records a **validated bridge, not a breakthrough claim**.

## Next target

Search for the missing nontrivial step: derive `G_D(O)` or an analogue directly from admissible transformations and resource/interface rules, rather than supplying the decision family externally. Candidate directions are (i) resource-constrained distinguishability under adaptive actions, (ii) Blackwell-deficiency lower bounds under restricted experiment families, and (iii) local-to-global translator obstructions where the witness family is forced by GC-I projection irreducibility rather than chosen by hand.