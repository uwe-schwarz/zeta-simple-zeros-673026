# A candidate 67.302666% lower bound for simple critical-line zeros of the Riemann zeta function

This derivative research draft updates the finite certificate in Ainta's
AI-assisted [`zeta-simple-zeros`](https://github.com/ainta/zeta-simple-zeros/tree/040c5e899e658aed7b56a2a87f501798fe10761d)
draft. It retains Ainta's stability refinement, seven-point use of the
Montgomery--Taylor overlap kernel, block aggregation, shifted pinching, and
verifier lineage. The analytic foundation and limiting kernel come from
Anthropic's paper
[*More Than Two Thirds of the Zeros of the Riemann Zeta Function Lie on the Critical Line*](https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf).
This project adds an exact finite-dimensional spectral conversion, a stronger
reproducible interval certificate, and a substantial Lean
certificate-consumer effort.

> AI-assisted derivative research artifact. Curated and released by Uwe
> Schwarz. Mathematical provenance and contribution boundaries are documented
> below; this stewardship note is not a claim of sole mathematical authorship.

**[Paper source](paper/riemann.tex)** · [Proof outline](docs/proof.md) ·
[Verifier](docs/verifier.md) · [Verification status](VERIFICATION_STATUS.md) ·
[Novelty status](NOVELTY_STATUS.md) · [Fresh replay](REPRODUCIBILITY.md) ·
[Lean build evidence](evidence/lean/README.md)

Let $N(T,2T)$ count nontrivial zeros with multiplicity and let
$N_0^s(T,2T)$ count zeros that are simultaneously simple and on the critical
line. The candidate theorem is

$$
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
\ge 0.6730266625438475.
$$

The exact constant proved by the downstream arithmetic is

$$
0.6730266625438475496579090211642630978\ldots,
$$

so the displayed decimal is a downward truncation.

## New finite input

For six nonnegative consecutive gaps, the verifier proves

$$
\mathcal F_6(g_1,\ldots,g_6)
\ge \frac{382623}{100000000}=0.00382623.
$$

The functional contains the 21 pairwise Montgomery--Taylor overlap terms and
the same pressure coefficient $1/3000$ as the earlier seven-point argument.
The committed report [`certificates/seven-point-382623.txt`](certificates/seven-point-382623.txt)
records a successful 128-bit Arb run over 980,069 search nodes.

The optimal block size for the exact spectral conversion is $m=279$. If

$$
A=\frac{382623}{100000000}(m-6),\qquad
C=\frac{A}{m}+2\sqrt{\frac{m-1}{m}A}-1,
$$

then the final constant is

$$
B_{279}=
\frac{H_{\mathrm{MT}}-139/69750}{1-C/279},\qquad
H_{\mathrm{MT}}=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}.
$$

## Evidence

| Component | Current evidence |
| --- | --- |
| Anthropic analytic input | Imported from the public paper and Lean artifact |
| Stability and spectral conversion | Mathematical proof plus Lean formalization of the analytic assembly |
| Finite inequality | Reproducible Arb certificate at the exact rational target |
| Lean certificate semantics | Kernel-built generic MVT, segment, replay, and scaled-checker layers |
| Code-9 terminal catalog | Complete dependency-ordered kernel build; terminal attestation preserved in [`evidence/lean`](evidence/lean/README.md) |
| Code-10 terminal catalog | Complete 5,793-module production build; lane, transfer, canonical gap replay, and cross-host content attestations preserved in [`evidence/lean`](evidence/lean/README.md) |
| Code-2 terminal catalog | Representative production modules kernel-built; full catalog deliberately deferred |
| Final public Lean theorem | Source-complete candidate, but its dependency-closed production replay is not complete |

The theorem stated in the paper relies on the standalone Arb certificate for
the finite inequality. The last row is important: this draft does **not**
currently claim a fully dependency-closed Lean verification of the new bound.
See
[`VERIFICATION_STATUS.md`](VERIFICATION_STATUS.md) for the precise boundary.

## Reproduce the interval certificate

Python 3.9 or later and `python-flint` are required.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -e .

python3 -m unittest discover -s tests -v
python3 verify_constants.py
zeta-zero-verify seven --progress-every 100000
```

A successful constant check must report `verified=true`, the unique finite
maximum at `m=279`, and positive exact tail checkpoints. A successful interval
run must report
`target=F6 >= 382623/100000000` and `verified=true`. An unresolved terminal
box is a hard failure.

## Status and claims

This is an AI-assisted, unreviewed research draft. The finite interval
certificate is reproducible, and substantial parts of the new proof have
been independently source-audited and kernel-checked. Independent
mathematical review remains necessary.

Until the final build gates in `VERIFICATION_STATUS.md` have passed, describe
this work as a **candidate improvement within the cited certificate lineage,
with an incomplete full Lean replay**, not as a completed formal proof or an
established record.
It is also not the largest numerical value among current public research-draft
claims; the intended contribution is the exact certificate and formalization
path. See [`NOVELTY_STATUS.md`](NOVELTY_STATUS.md).

## Provenance

The stability refinement, seven-point kernel use, block aggregation, shifted
pinching, and original verifier lineage derive from
[`ainta/zeta-simple-zeros` at commit `040c5e899e...`](https://github.com/ainta/zeta-simple-zeros/tree/040c5e899e658aed7b56a2a87f501798fe10761d),
which is distributed under the MIT license. This citation does not imply
coauthorship or endorsement by Ainta.

The clean-room reproduction
[`learademacher/ai-refines-ai-zeta-bound` at commit `bd4a7d3698...`](https://github.com/learademacher/ai-refines-ai-zeta-bound/tree/bd4a7d36988b23220034527881f4457f2f689e86)
is an independent comparison point; this repository imports no proof text or
implementation from it. The analytic foundation and limiting
Montgomery--Taylor overlap kernel come from Anthropic's paper and its
[`zeta-23-lean` v1.0 artifact at commit `3635e74826...`](https://github.com/anthropics/zeta-23-lean/tree/3635e74826a4c1fcece7d1cd2b6fa75e43a00510).

This project contributes the exact finite-dimensional spectral envelope, the
stronger rational certificate, the `m=279` optimization, the reproducibility
package, and the partial Lean certificate consumer.

## License

MIT for the inherited verifier and paper materials. The separately developed
Lean formalization carries the licenses recorded in its source tree.
