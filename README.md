# A candidate 67.302666% lower bound for simple critical-line zeros of the Riemann zeta function

This derivative research draft updates the finite certificate in Ainta's
AI-assisted [`zeta-simple-zeros`](https://github.com/ainta/zeta-simple-zeros)
draft. It preserves that draft's stability refinement, overlap kernel, block
aggregation, and shifted pinching, which extend Anthropic's paper
[*More Than Two Thirds of the Zeros of the Riemann Zeta Function Lie on the Critical Line*](https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf),
and adds an exact finite-dimensional spectral conversion, a stronger
reproducible interval certificate, and a substantial Lean
certificate-consumer effort.

**[Paper source](paper/riemann.tex)** · [Proof outline](docs/proof.md) ·
[Verifier](docs/verifier.md) · [Verification status](VERIFICATION_STATUS.md) ·
[Novelty status](NOVELTY_STATUS.md) · [Fresh replay](REPRODUCIBILITY.md)

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
| Code-9 terminal catalog | Complete dependency-ordered kernel build |
| Code-10 terminal catalog | Production kernel build in progress |
| Code-2 terminal catalog | Representative production modules kernel-built; full catalog deliberately deferred |
| Final public Lean theorem | Source-complete candidate, but its dependency-closed production replay is not complete |

The last row is important: this draft does **not** currently claim a fully
dependency-closed Lean verification of the new bound. See
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

The stability argument and original verifier derive from
[`ainta/zeta-simple-zeros`](https://github.com/ainta/zeta-simple-zeros), which
is distributed under the MIT license. The clean-room reproduction
[`learademacher/ai-refines-ai-zeta-bound`](https://github.com/learademacher/ai-refines-ai-zeta-bound)
provides a useful independent comparison point. The analytic foundation is
Anthropic's paper and its
[Lean artifact](https://github.com/anthropics/zeta-23-lean).

## License

MIT for the inherited verifier and paper materials. The separately developed
Lean formalization carries the licenses recorded in its source tree.
