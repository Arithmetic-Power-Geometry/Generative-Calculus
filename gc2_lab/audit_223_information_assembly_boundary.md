# GC-II Audit 223 — Information-assembly boundary

Status: decisive falsification / prior-art boundary.

## Candidate under test

Audit 222 left open a projection-forced endogenous information-assembly excess: under the same causal architecture and future information, perhaps proper projections being insufficient to assemble a global generative witness forces extra observations/messages beyond those needed for matched external behavior.

## Operational model

Fix an architecture A with parties i=1,...,k. Party i receives local view v_i=P_i(w) of an underlying world w. A global generative witness is any output z satisfying a relation G(v_1,...,v_k,z). Let

T_A(G)=inf{cost(P): P is an A-admissible protocol that outputs some z with G(v_1,...,v_k,z) on every admissible input}.

Let external behavior be relation B on the same local views, with cost T_A(B).

## Theorem 223.1 — witness-as-relation collapse

If all operational requirements on the purported global generative witness are captured by G as a relation of the parties' local views and protocol transcript/output, then the minimum information/message cost of assembling that witness is exactly the ordinary communication/distributed-computation complexity T_A(G) of that relation.

Proof. The feasible GC witness-assembly procedures and the feasible A-protocols solving G are the same objects: each receives the same local views, has the same allowed communication/actions, and succeeds exactly when its output satisfies G. The cost functional is also the same. Therefore the feasible sets and their costs coincide, so their infima coincide. QED.

## Corollary 223.2 — subtraction does not manufacture GC novelty

Define the tempting residual

Xi_assm = T_A(G)-T_A(B).

Even when Xi_assm>0, this proves only that relation G is harder than relation B under architecture A. It is not intrinsically a GC novelty gap. In particular, choosing B to be a constant-output task makes T_A(B)=0 and Xi_assm=T_A(G), i.e. the residual is exactly ordinary communication complexity.

Thus proper-projection insufficiency can force information transfer, but if the required global object is extentionally specified as a relation on local inputs, that transfer cost is already a distributed relation/function-computation cost.

## Exact separating family

For two n-bit local views x,y, let B be the constant behavior B(x,y)=0 and let G require the equality bit 1[x=y]. Then T_A(B)=0 while deterministic exact T_A(G)>0 (indeed standard equality communication complexity applies). Hence a strictly positive assembly-minus-behavior residual exists without any generative calculus structure at all. Positivity alone therefore cannot certify Omega_G.

## Prior-art collision

Communication complexity studies the information/communication required for parties with distributed inputs to compute functions or relations. Information complexity lower-bounds communication by the information revealed by protocols, and distributed/local computation studies when local views suffice for global decisions. Local verification of global proofs further studies the cost of certificates enabling nodes with local views to verify global properties. Therefore projection-insufficient local views plus a globally required witness are not, by themselves, outside established theory.

## Edge and invariance checks

- If G=B, Xi_assm=0 exactly.
- If B is constant, Xi_assm reduces to T_A(G).
- If G has a zero-communication selector valid for every local-view tuple, T_A(G)=0 despite possible hidden global structure.
- Relabeling local alphabets or witness symbols by bijections leaves protocol complexity unchanged.
- Adding irrelevant latent variables invisible to every P_i cannot change T_A(G) unless G is changed to depend operationally on them.
- Randomized/error-tolerant variants collapse in the same way when both formulations use the same error and adversary convention.
- Infeasible witness relations should be recorded as infeasible/infinite cost; infinity-minus-infinity is not a scalar invariant.
- The theorem does not assume additivity, finite state, or a particular number of communication rounds.

## Status ledger

- projection insufficiency can force communication for a specified global relation: PROVED / IMPORTED-KNOWN mechanism
- witness-assembly cost for an extensional relation G: PROVED identical to ordinary distributed/communication complexity of G
- positive T_A(G)-T_A(B) as GC-specific Omega_G: FALSIFIED
- information complexity / distributed function or relation computation / local global verification: IMPORTED/KNOWN boundary
- a GC-specific residual based only on extra observations/messages for a global witness: FALSIFIED when the witness requirement is extensionally relational
- non-extensional generative requirement not reducible to a fixed input-output relation under the same operational semantics: OPEN, but must be defined without smuggling in an analyst-chosen representation or hidden task

## Consequence for Paper II

Do not pursue raw information-assembly excess as the breakthrough. Audits 218-223 jointly show that architecture, communication, nonanticipativity, local-view insufficiency, and witness production all collapse to established protocol complexity once the complete operational requirement is fixed extensionally.

The next admissible target must therefore change the mathematical object, not merely the protocol cost. A serious possibility is a capability-accounting invariant over transformations of the operational specification itself: whether acquiring resources/information/actions/rules changes which task relations can be instantiated, with a quotient that identifies behaviorally equivalent presentations. Any such object must immediately be tested against resource-theory convertibility, simulation preorders, program synthesis, and algorithmic information before being called novel.
