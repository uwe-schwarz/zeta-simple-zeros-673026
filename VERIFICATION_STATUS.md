# Verification status

Snapshot date: 2026-08-16

This document separates mathematical claims, reproducible computation,
source audits, and kernel-checked Lean evidence. A green item in one column
must not be used as evidence for a stronger column.

## Claim matrix

| Claim or artifact | Mathematical/source audit | Reproducible computation | Lean kernel status | Release status |
| --- | --- | --- | --- | --- |
| Exact local target $F_6\ge382623/10^8$ | Independently replayed from the frozen topology and terminal data | Fresh Arb replay on 2026-08-16 reports `verified=true` with matching counts and hashes | Generic checker and representative production terminals pass | Candidate evidence complete |
| Stability-enhanced rank--trace argument | Proof audited against the pinned Anthropic setup | Not applicable | Analytic assembly is formalized | Candidate evidence complete |
| Exact spectral conversion and $m=279$ optimum | Exact rational and directed-Arb audit | Included constant verifier separates the complete finite scan and checks the exact tail checkpoints | Formalized, including the displayed decimal comparison | Candidate evidence complete |
| MVT cells, segment forest, transformed topology | Exhaustive independent source/replay audits | Deterministic generators and pinned manifests | Generic layers and production MVT data are kernel-built | Complete for the generated layers |
| Partitioned Code-9 catalog | Exact tree/box/path/source audit | 1,773 terminal providers, 6,350 dependency targets | Full catalog build passed | Complete |
| Scaled Code-10 catalog | Exact 289,646-terminal source audit | 5,793 generated modules and 28,965 cross-host-hashed artifacts | Full catalog build, seven-module canonical gap replay, transfer, and macOS/Linux artifact digest passed | Complete |
| Scaled Code-2 catalog | Exact 198,935-terminal source audit and direct semantic bridge audit | 3,979 generated modules | 22 production modules and representative bridge modules passed | Full catalog deferred |
| Final finite theorem `q2_finite_certificate_mvt` | Full source graph and fail-closed plan audited | 8,379-target final plan frozen | Dependency-closed final build not run | Pending |
| Final zeta-zero asymptotic theorem | Analytic bridge and exact theorem statements audited | Not applicable | Final fresh integration and axiom audit not run | Pending |

The internal catalog labels used by the build scripts mean:

- **Code-9:** bounded-subcell adaptive tangent terminals;
- **Code-10:** mean-value interval terminals;
- **Code-2:** tangent-and-convexity terminals.

These labels describe certificate-consumer implementation paths, not separate
mathematical claims.

## What may be claimed now

- The project has a reproducible interval certificate for the exact finite
  inequality $F_6\ge382623/100000000$.
- The downstream exact arithmetic gives the candidate constant
  $0.6730266625438475496579\ldots$ and the displayed lower bound
  $0.6730266625438475$.
- The new theorem is intended for the joint count of zeros that are both
  simple and on the critical line.
- Large parts of the certificate consumer and analytic bridge have been
  formalized and kernel-built.

## What must not be claimed yet

- “The new bound is fully Lean-verified.”
- “The dependency-closed public theorem has passed a clean build.”
- “The project has completed its final transitive axiom audit.”
- “This is an established or peer-reviewed numerical record.”
- “No stronger public research draft exists.”

## Gates required for a full formal-verification claim

1. [Complete] Finish and attest all 5,793 scaled Code-10 catalog modules.
2. Finish and attest all 3,979 scaled Code-2 catalog modules.
3. Build all 8,379 targets in the frozen final dependency plan.
4. Rehash-build the public finite theorem from the exact source closure.
5. Run the 25-fixture fail-closed negative audit and validate its result.
6. Parse the full transitive `#print axioms` output against the stated
   standard-axiom whitelist.
7. Run `leanchecker --fresh` on the public theorem.
8. Run the separately pinned analytic integration and its axiom audit.
9. Refresh the primary-source novelty review immediately before release.

## Trust boundary of the current interval certificate

The standalone verifier trusts Python, IEEE-754 binary64 behavior,
`python-flint`, FLINT/Arb, the operating system, the hardware, and the
committed verifier source. The release replay used Python 3.11.15 and
`python-flint` 0.9.0 on macOS 26.6.1 arm64; the exact file set is pinned by
`RELEASE_MANIFEST.sha256`. The incomplete full Lean replay is designed to
replace most of this certificate-consumption boundary, but it must not be
treated as complete until every gate above has passed.
