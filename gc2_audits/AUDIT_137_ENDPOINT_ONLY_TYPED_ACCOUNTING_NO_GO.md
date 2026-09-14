# GC-II Audit 137 — Endpoint-Only Typed Accounting No-Go

## Question

Can an exact continuation-sensitive capability quantity be universally upper-bounded by a finite function

\[
\Omega_G \le F(\Delta R,\Delta I,\Delta A,\Delta L)
\]

when the four deltas are endpoint/acquisition quantities and do **not** explicitly charge continuation-sufficient persistent memory/history state?

## Result

**No.** Under that interpretation, endpoint-only accounting is insufficient.

Use the operational language

\[
L=\{0^n1^n:n\ge 0\}.
\]

For a finite horizon parameter \(K\), consider prefixes

\[
p_i=0^i,\qquad i=0,\ldots,K.
\]

For every \(i<j\), the continuation \(z_i=1^i\) distinguishes the two prefixes:

\[
p_i z_i=0^i1^i\in L,
\qquad
p_j z_i=0^j1^i\notin L.
\]

Therefore the \(K+1\) prefixes are pairwise continuation-distinguishable. Any exact continuation-sufficient state representation needs at least

\[
N_K\ge K+1
\]

states and hence at least

\[
M_K\ge \lceil\log_2(K+1)\rceil
\]

bits of persistent state.

Now hold the endpoint accounting vector fixed at

\[
(\Delta R,\Delta I_{\rm external},\Delta A,\Delta L)=(0,0,0,0)
\]

for every \(K\), where \(I_{\rm external}\) explicitly excludes persistent continuation memory. Then any proposed finite value

\[
F(0,0,0,0)=C<\infty
\]

cannot upper-bound a continuation-sensitive quantity that grows at least as \(\log_2(K+1)\): choose \(K>2^C-1\).

Thus a universal exact bound of that form is impossible unless the accounting variables include a continuation-sufficient memory/history term or another quantity that lower-bounds it.

## Important scope condition

This audit **does not** show that information accounting is useless. If \(\Delta I\) is defined to include persistent internal memory capacity, then the counterexample disappears as a no-go and instead yields the ordinary lower bound

\[
\Delta I_{\rm memory}\ge \lceil\log_2(K+1)\rceil.
\]

Accordingly, the falsified target is specifically an endpoint/acquisition-only accounting law that omits continuation memory.

## Exact regression

Executable: `experiments/audit137_endpoint_only_typed_accounting_no_go.py`

Frozen output: `results/audit137_endpoint_only_typed_accounting_no_go.json`

Horizons tested:

\[
K\in\{1,2,4,8,16,32,64,128,256\}.
\]

The checker performed **43,946** pairwise continuation-distinguishability checks with **0 failures**. At \(K=256\), the verified lower bound is **257 exact continuation classes**, requiring at least **9 bits**.

The finite checks are regression evidence only. The unbounded statement follows analytically from the distinguishing continuation above.

## Prior-art collision

The core lower-bound mechanism is not new GC mathematics. It is a direct continuation-equivalence/state-complexity argument of Myhill–Nerode type: distinct right contexts force distinct exact states. Streaming and communication-complexity lower bounds similarly use retained information/state as a computational resource.

Therefore GC-II must not claim novelty for the memory lower bound itself.

## Ledger

- Pairwise continuation distinguishability of \(0^0,\ldots,0^K\): **PROVED**.
- \(N_K\ge K+1\): **PROVED**.
- Persistent exact-memory lower bound \(\lceil\log_2(K+1)\rceil\): **PROVED**.
- Universal finite endpoint-only bound omitting persistent memory: **FALSIFIED**.
- Exact finite regression through \(K=256\): **PASS / NUMERICALLY SUPPORTED**.
- Myhill–Nerode/state-complexity mechanism: **IMPORTED/KNOWN**.
- A genuinely GC-specific coupled law after adding independently measurable continuation memory: **OPEN**.

## Consequence for the Paper-II program

The quantitative accounting target should be refined from

\[
\Omega_G\le F(\Delta R,\Delta I,\Delta A,\Delta L)
\]

to a form in which the information coordinate is operationally decomposed, for example

\[
\Omega_G\le F(\Delta R,\Delta I_{\rm acquired},\Delta I_{\rm persistent},\Delta A,\Delta L),
\]

or where an independently measurable continuation-state complexity enters explicitly. The next scientific gate is to determine whether a nontrivial coupling among these quantities survives reduction to ordinary streaming/state/communication complexity.
