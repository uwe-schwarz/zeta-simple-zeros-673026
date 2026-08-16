# Draft announcement

Do not publish this text before the release checklist, attribution wording,
repository URL, and release-day novelty check are complete.

## Short post

This repository contains an AI-assisted, unreviewed derivative artifact that
strengthens the finite certificate in Ainta's Montgomery--Taylor refinement
for zeros that are both simple and on the critical line:

`liminf N_0^s(T,2T) / N(T,2T) >= 0.6730266625438475`.

The new finite input is an exact Arb-certified inequality
`F6 >= 382623/100000000`, checked over a complete branch-and-bound cover with
980,069 nodes. The verifier, certificate, proof draft, exact constant
arithmetic, and an explicit verification-status matrix are available here:

`https://github.com/uwe-schwarz/zeta-simple-zeros-673026`

Important boundary: substantial Lean components are kernel-checked, but the
dependency-closed production replay is not complete. This is a research draft
and a request for independent mathematical and computational review, not a
claim of peer review or a completed formal proof.

## Longer release note

This artifact preserves Ainta's stability-enhanced rank--trace refinement,
seven-point use of the inherited Montgomery--Taylor overlap kernel,
block aggregation, shifted pinching, and verifier lineage. The analytic
foundation and limiting kernel come from Anthropic's work. This project adds
an exact finite-dimensional spectral envelope and strengthens the finite input
to

`F6(g1,...,g6) >= 382623/100000000`

for all nonnegative gaps. A 128-bit Arb verifier proves this over a complete
six-dimensional branch-and-bound cover. The frozen run reports 980,069 visited
nodes, 490,399 terminal boxes, and maximum depth 65. The exact
finite-dimensional spectral conversion is optimized at block size 279 and
gives

`0.6730266625438475496579090211642630978...`.

The repository separates four kinds of evidence:

1. the mathematical deduction and exact constants;
2. the independently reproducible Arb certificate;
3. source and replay audits for the generated Lean certificate data;
4. the subset of the Lean production graph that has actually completed kernel
   checking.

The full bounded-subcell adaptive tangent and mean-value interval catalogs are
complete, including preserved Code-10 lane, transfer, canonical gap-replay,
and cross-host artifact attestations. The complete tangent-and-convexity
catalog and final dependency-closed public theorem build are intentionally
deferred unless there is external interest in funding or running that final
verification stage. Nothing in the release should be read as claiming those
deferred gates have passed.

The stability refinement, seven-point kernel use, aggregation, and pinching
arguments derive from Ainta's pinned public verifier and draft. Anthropic's
analytic paper and pinned Lean artifact are the cited foundation, and
Learademacher's clean-room reproduction is an independent comparison only.
The new work here is the exact
spectral-envelope extension, the stronger q2 certificate and its reproduction
package, and the partial Lean consumer.
Independent review, reruns, and specific criticism are welcome.
