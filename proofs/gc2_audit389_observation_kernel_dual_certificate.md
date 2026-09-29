# GC-II Audit 389 — Exact observation-kernel criterion and robust dual certificate

## Purpose

Audits 386–388 show that sign, normalization, monotonicity, submodularity, and bounded-radius complement observations do not by themselves identify a signed higher-order capability tail. This audit isolates the exact finite-dimensional obstruction before adding any GC-specific operational structure.

## Setup

Let \(V\) be a finite-dimensional real vector space of capability descriptions. Let
\[
O:V\to\mathbb R^m
\]
be the operational observation map and let
\[
L:V\to\mathbb R
\]
be the scalar capability quantity to be certified (for example a chosen Möbius-tail functional). Let \(C\subseteq V\) be the admissible capability class and define its difference set
\[
D=C-C=\{x-y:x,y\in C\}.
\]

Two admissible capabilities are observationally indistinguishable exactly when their difference lies in \(D\cap\ker O\).

## Theorem 389.1 — admissible exact-identifiability criterion

The following are equivalent:

1. \(L(x)\) is exactly determined by \(O(x)\) on \(C\).
2. For all \(x,y\in C\), \(O(x)=O(y)\Rightarrow L(x)=L(y)\).
3. \[
   D\cap\ker O\subseteq\ker L.
   \]

### Proof

(1) and (2) are the definition of exact determination. For (2) iff (3), put \(d=x-y\). Linearity gives \(O(x)=O(y)\) iff \(Od=0\), and \(L(x)=L(y)\) iff \(Ld=0\). QED.

**Status:** PROVED, but mathematically a direct linear-identifiability fact; do not claim novelty.

## Corollary 389.2 — unrestricted linear row-space criterion

If \(C=V\), then exact identification is equivalent to
\[
\ker O\subseteq\ker L,
\]
which in finite dimensions is equivalent to
\[
L\in\operatorname{row}(O).
\]
Equivalently, there exists \(\lambda\in\mathbb R^m\) such that
\[
L=\lambda^\top O.
\]

Hence every exactly identifiable unrestricted linear target has a linear observation certificate
\[
L(x)=\lambda^\top O(x).
\]

**Status:** PROVED / IMPORTED-KNOWN linear algebra.

## Theorem 389.3 — robust dual certificate

Equip the observation space with a norm \(\|\cdot\|\), with dual norm \(\|\cdot\|_*\). If
\[
L=\lambda^\top O,
\]
then for any two descriptions \(x,y\),
\[
|L(x)-L(y)|
\le \|\lambda\|_*\,\|O(x)-O(y)\|.
\]

Among all linear certificates, the best guaranteed constant is
\[
\kappa_L(O)
=
\inf_{\lambda:\,O^\top\lambda=L}\|\lambda\|_*.
\]

Thus noisy observations with error at most \(\eta\) certify target error at most \(\kappa_L(O)\eta\).

### Proof

Apply dual Hölder:
\[
|L(x-y)|=|\lambda^\top O(x-y)|
\le\|\lambda\|_*\|O(x-y)\|.
\]
Infimize over feasible certificates. QED.

**Status:** PROVED / IMPORTED-KNOWN convex duality and inverse-problem conditioning.

## Consequence for Audit 388

Audit 388 constructs \(d=v_\varepsilon-g_n\) satisfying \(Od=0\) but \(L_qd\ne0\) for the bounded-radius complement observation map \(O\) and signed tail functional \(L_q\). Therefore
\[
d\in (C_{\rm norm,mono,submod}-C_{\rm norm,mono,submod})\cap\ker O
\quad\text{but}\quad
d\notin\ker L_q.
\]
Theorem 389.1 therefore certifies the impossibility without reference to any estimator.

## What a genuine GC-II theorem must now prove

The linear criterion itself is not a breakthrough. A nontrivial GC-II result must derive, from GC-I operational admissibility rather than assume, at least one of:

- **kernel elimination:** \(D_{\rm GC}\cap\ker O\subseteq\ker L\);
- **kernel contraction:** \(|L(d)|\le K\|O(d)\|\) for every admissible operational difference \(d\);
- **finite certificate construction:** a computable family of GC-derived observations whose rows span the target functional on the admissible difference geometry;
- **translator lower bound:** prove that any observation family failing a GC-derived structural requirement necessarily leaves an admissible \(d\in\ker O\) with \(L(d)\ne0\).

This is the correct location for a possible Closure-Escape statement: an observationally silent admissible direction that changes target capability is an escape from the observation closure. Merely renaming Theorem 389.1 as Closure-Escape would be tautological and is explicitly rejected.

## Stress checks

- **Degenerate \(L=0\):** criterion holds trivially; scientifically uninformative.
- **No observations \(O=0\):** exact identification requires \(L\) constant on \(C\); for linear unrestricted \(C\), this forces \(L=0\).
- **Injective \(O\):** \(\ker O=\{0\}\), so every linear target is identifiable.
- **Restricted \(C\):** row-space membership is sufficient but not necessary; the exact object is \((C-C)\cap\ker O\).
- **Composition:** no closure under composition follows from linear algebra alone. This remains OPEN and is where GC structure must enter.
- **Dimensions:** \(O\) maps capability units to observation coordinates; \(\lambda\) carries the corresponding conversion weights so \(\lambda^\top O\) has the units of \(L\).
- **Invariance:** replacing observations by any invertible coordinate transform \(AO\) leaves \(\ker O\) and exact identifiability unchanged.
- **Monotonicity:** not required for the theorem; Audit 388 matters because its witness remains inside a strongly regular admissible class.

## Prior-art collision boundary

The unrestricted row-space/nullspace equivalence is elementary finite-dimensional linear algebra. The robust constant is standard dual-norm/conditioning machinery. Related language appears broadly in inverse problems, observability, experimental design, compressed sensing, and statistical identifiability. Therefore none of these statements should be presented as GC novelty.

The candidate novelty is only a future theorem that derives a useful restriction on \(D_{\rm GC}\) from the explicit GC operational rules and proves composition-stable kernel elimination/contraction or a translator lower bound.

## Ledger

| Claim | Status |
|---|---|
| admissible difference-kernel criterion | PROVED |
| unrestricted row-space certificate | IMPORTED/KNOWN |
| robust dual certificate | IMPORTED/KNOWN |
| Audit-388 collision implies estimator-independent impossibility | PROVED |
| generic linear criterion itself is GC novelty | FALSIFIED |
| GC-I rules imply kernel elimination | OPEN |
| GC-I rules imply quantitative kernel contraction | OPEN |
| composition-stable certificate | OPEN |
| operational local-to-global translator lower bound | OPEN |
