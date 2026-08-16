# Novelty and comparison status

Snapshot date: 2026-08-16

This file is intentionally separate from the proof. Public research-draft
claims are changing quickly, and numerical ordering is not evidence of
correctness, peer review, or independent acceptance.

## Direct lineage

| Work | Publicly stated joint simple-and-critical-line lower bound | Status relevant here |
| --- | ---: | --- |
| [Anthropic, *More Than Two Thirds of the Zeros...*](https://www.anthropic.com/research/riemann-zeta) | $0.672500703679\ldots$ | Published company research paper and Lean artifact; analytic foundation used here |
| [Ainta, `zeta-simple-zeros`](https://github.com/ainta/zeta-simple-zeros/tree/040c5e899e658aed7b56a2a87f501798fe10761d) | $0.673008527927\ldots$ | AI-assisted, unreviewed research draft; source of the verifier lineage |
| [Learademacher, `ai-refines-ai-zeta-bound`](https://github.com/learademacher/ai-refines-ai-zeta-bound) | $0.673021361950\ldots$ | Clean-room research draft and reproduction point |
| This artifact | $0.6730266625438475$ | Reproducible q2 Arb certificate; incomplete full Lean production replay |

Thus this artifact improves the exact number in the direct Ainta and
Learademacher lineage.

## Higher public research-draft claims already exist

The number above is **not** the largest public claim in the same broad
research-draft category. Examples visible at the snapshot date include:

- [`sxuff/zeta-positioned-pressure`](https://github.com/sxuff/zeta-positioned-pressure),
  whose repository description states $67.3205978423\%$;
- [`AMTOPA/zeta-exact-pressure-673262`](https://github.com/AMTOPA/zeta-exact-pressure-673262),
  whose repository description states $67.3262375585\%$;
- [`AMTOPA/zeta-exact-pressure`](https://github.com/AMTOPA/zeta-exact-pressure),
  whose current repository description states $67.3416490971\%$.

These entries are cited as public claims, not endorsed as correct. Their
proofs, trust boundaries, and review status are not interchangeable with this
artifact's evidence.

## Honest novelty claim

The release should not advertise a numerical record. Its defensible novelty
is narrower:

- a stronger exact target within the original seven-point q2 certificate
  lineage;
- an exact finite-dimensional spectral conversion at the uniquely optimal
  block size $m=279$;
- a complete reproducible Arb certificate for that target;
- a substantial, explicitly incomplete Lean certificate-consumer effort with
  unusually detailed source, negative-test, and axiom-audit gates.

If the remaining Lean production build is completed, the formal-evidence
story may become the main differentiator. Without it, the project is still a
useful reproducibility artifact, but not the numerical frontier.

Refresh this comparison immediately before any public release.
