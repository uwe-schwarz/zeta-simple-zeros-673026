# Draft announcement

Do not publish this text before the release checklist, attribution wording,
repository URL, and release-day novelty check are complete.

## Short post

We have prepared an AI-assisted, unreviewed derivative artifact that strengthens
the finite certificate in Ainta's Montgomery--Taylor refinement for zeros that
are both simple and on the critical line:

`liminf N_0^s(T,2T) / N(T,2T) >= 0.6730266625438475`.

The new finite input is an exact Arb-certified inequality
`F6 >= 382623/100000000`, checked over a complete branch-and-bound cover with
980,069 nodes. The verifier, certificate, proof draft, exact constant
arithmetic, and an explicit verification-status matrix are available here:

`REPOSITORY_URL`

Important boundary: substantial Lean components are kernel-checked, but the
dependency-closed production replay is not complete. This is a research draft
and a request for independent mathematical and computational review, not a
claim of peer review or a completed formal proof.

## Longer release note

This artifact preserves the stability-enhanced rank--trace, overlap-kernel,
block-aggregation, and shifted-pinching arguments from Ainta's public draft,
derived from Anthropic's Montgomery--Taylor work. It adds an exact
finite-dimensional spectral envelope and strengthens the finite input to

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

The full Code-9 catalog is complete and Code-10 is being allowed to finish.
The complete Code-2 catalog and final dependency-closed public theorem build
are intentionally deferred unless there is external interest in funding or
running that final verification stage. Nothing in the release should be read
as claiming those deferred gates have passed.

The mathematical stability, overlap-kernel, aggregation, and pinching
arguments derive from Ainta's public verifier and draft. Anthropic's analytic
paper and Lean artifact are the cited foundation, and Learademacher's
clean-room reproduction is a comparison point. The new work here is the exact
spectral-envelope extension, the stronger q2 certificate and its reproduction
package, and the partial Lean consumer.
Independent review, reruns, and specific criticism are welcome.
