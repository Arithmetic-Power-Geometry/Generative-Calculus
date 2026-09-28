# GC-II Audit 387 — leave-one-out certificate for positive Möbius tails

## Scope
Branch-only GC-II capability-accounting audit. GC-I foundations on main are unchanged.

## Setup
Let N be a finite ground set, |N|=n. Let v:2^N -> [0,1] satisfy v(empty)=0, v(N)=1 and admit a nonnegative Möbius transform m(T)>=0 for all nonempty T. Hence sum_{T subseteq N} m(T)=1 and m is a probability mass function on nonempty subsets.

For q<n define the order-q truncation residual

E_q := sum_{|T|>q} m(T).

Under nonnegative Möbius mass this equals 1 minus the cumulative Möbius mass through order q.

Define a random focal set X with P(X=T)=m(T), and its interaction order K:=|X|. Then exactly

E_q = P(K>q).

This probabilistic representation is IMPORTED/KNOWN belief-function/Möbius machinery, not a GC novelty claim.

## Theorem 387.1 — linear-query tail certificate
Define the leave-one-out deficit

d_i := v(N)-v(N\{i}) = 1-v(N\{i}).

Then

mu := sum_{i in N} d_i = sum_T |T| m(T) = E[K].

Consequently, for every integer q>=0,

E_q <= min(1, mu/(q+1)).

### Proof
Because v(S)=sum_{T subseteq S}m(T),

1-v(N\{i}) = sum_{T: i in T} m(T).

Summing over i and exchanging finite sums gives

sum_i d_i = sum_T (sum_i 1[i in T])m(T)
          = sum_T |T|m(T)
          = E[K].

Since K is a nonnegative integer, on {K>q} we have K>=q+1. Therefore

E[K] >= (q+1)P(K>q) = (q+1)E_q,

which proves the claim.

Status: PROVED.

## Tightness
The coefficient 1/(q+1) cannot be improved using mu alone. Whenever n>=q+1 and alpha in [0,1], place Möbius mass alpha on one set T of size q+1 and the remaining mass 1-alpha on singleton focal sets. Then

E_q=alpha,

while mu = alpha(q+1)+(1-alpha).

Thus the raw Markov form is not equality unless zero-order mass is permitted. Under v(empty)=0, K>=1, yielding the sharper shifted certificate below.

## Theorem 387.2 — shifted certificate exploiting v(empty)=0
Because K>=1 almost surely,

mu-1 = E[K-1] >= q P(K>q)

for q>=1. Hence

E_q <= min(1,(mu-1)/q).

This bound is sharp: put mass alpha on a (q+1)-set and mass 1-alpha on singleton sets. Then mu-1=alpha q and E_q=alpha.

Status: PROVED, SHARP.

## Operational reading
For normalized positive-Möbius capability, the entire unseen interaction tail above order q can be certified using only n leave-one-out evaluations:

C_LOO(q) := min(1, [sum_i (1-v(N\{i})) - 1]/q).

Then E_q <= C_LOO(q).

This is computationally O(n) value-oracle calls after v(N), rather than enumeration of all 2^n coalitions.

This does NOT solve general GC-II capability accounting:
- it requires nonnegative Möbius mass;
- it is a tail-mass certificate, not a signed-tail certificate;
- it does not yet derive positivity or small mu from frozen GC-I structure;
- it is an application of classical probability tail reasoning after the belief-function representation.

Status of GC-specific novelty: OPEN / NOT CLAIMED.

## Edge and degenerate cases
- n=1: no proper q>=1<n exists; theorem is vacuous for proper truncation.
- q=0: E_0=1 under v(empty)=0 and normalized positive mass. Use Theorem 387.1, not the shifted division by q.
- mu lies in [1,n].
- unanimity witness m(N)=1 gives mu=n and shifted bound E_q <= min(1,(n-1)/q)=1 for q<n, correctly reproducing Audit 386.
- singleton-only mass gives mu=1 and E_q=0 for every q>=1, with equality.
- relabeling invariance: mu and C_LOO are invariant under permutations of N.
- monotonicity in q: C_LOO is nonincreasing in q.
- composition: no closure claim is made. Positive Möbius mass and the certificate must be rechecked after composition.

## Prior-art collision
The representation of nonnegative normalized Möbius coefficients as probability mass on focal sets is standard belief-function/capacity theory. The inequality is Markov's tail inequality applied to K-1. Therefore neither ingredient should be presented as a new standalone theorem.

The potentially useful GC-II contribution, if it can be proved later, would be a frozen-GC-I structural condition that forces small leave-one-out mean interaction order mu, or an analogue surviving signed Möbius mass and operational composition.

## Status ledger
- Positive Möbius mass -> focal-set probability representation: IMPORTED/KNOWN.
- E_q=P(K>q): PROVED (direct representation).
- mu=sum_i[1-v(N\{i})]=E[K]: PROVED.
- E_q<=min(1,(mu-1)/q), q>=1: PROVED, SHARP.
- O(n)-query certificate under positive Möbius mass: PROVED.
- General signed-Möbius analogue: OPEN.
- Composition-stable GC-I derivation of small mu: OPEN.
- Standalone novelty claim for the inequality: FALSIFIED by collision with standard probability/belief-function machinery.

## Next attack
Seek a signed analogue based on total-variation Möbius mass or paired positive/negative focal measures, and test whether any such certificate can be obtained from polynomially many complement/leave-r-out queries. Attempt adversarial collisions with identical leave-r-out data but arbitrarily different signed high-order residuals.
