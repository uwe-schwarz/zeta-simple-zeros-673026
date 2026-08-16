# Verifier design

The finite verifier combines Arb interval arithmetic with a fail-closed
branch-and-bound search. It proves the exact rational target

$$
\mathcal F_6\ge\frac{382623}{100000000}.
$$

## Kernel cells

For grid size $G=4000$, cell $i$ is the closed interval

$$
[i/G,(i+1)/G].
$$

`python-flint`/Arb evaluates the entire function

$$
K(x)=\frac12\left[
\operatorname{sinc}(\pi x-1/\sqrt2)+
\operatorname{sinc}(\pi x+1/\sqrt2)
\right]
$$

at 128-bit precision. The verifier derives directed lower bounds for
$w(x)=(K(x)/K(0))^2$ and for the tangent and Hessian data used by the
terminal predicates. Binary64 conversions are widened in the conservative
direction with `math.nextafter`.

## Seven-point search

For six nonnegative gaps,

$$
\mathcal F_6(g_1,\ldots,g_6)
=\frac1{3000}\sum_i g_i
+\sum_{s=1}^6\frac{2}{7-s}
 \sum_{i=1}^{7-s}w(g_i+\cdots+g_{i+s-1}).
$$

The search uses four terminal mechanisms:

- pressure pruning when the linear term alone reaches the target;
- interval lower bounds for all 21 overlap terms;
- certified tangent and convexity bounds from cached point and second-order
  interval data;
- a bounded subcell tangent tree for the remaining hard boxes.

If none of these predicates proves a box, the widest coordinate interval is
bisected. If a terminal box remains unresolved, verification fails loudly.
The committed certificate is therefore a complete cover, not a sampling
argument.

## Frozen result

[`certificates/seven-point-382623.txt`](../certificates/seven-point-382623.txt)
records:

| Field | Value |
| --- | ---: |
| exact target | `382623/100000000` |
| precision | 128 bits |
| visited nodes | 980,069 |
| pruned nodes | 490,399 |
| split nodes | 489,670 |
| maximum depth | 65 |
| interval terminals | 285,258 |
| pressure terminals | 3,166 |
| tangent terminals | 201,975 |
| of which use subcell fallback | 1,773 |
| result | `verified=true` |

The report also binds the generated tables and certificate data by hashes.

## Reproduction

Run the unit tests and the seven-point verifier from a clean environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
zeta-zero-verify seven --progress-every 100000
```

A successful run must print the exact target and `verified=true`.

## Trust base and Lean boundary

The standalone certificate trusts Python, IEEE-754 binary64 behavior,
`python-flint`, FLINT/Arb, the operating system, the hardware, and the
committed verifier source. It does not trust sampled optimization or an
unchecked terminal box.

A separately developed Lean consumer is intended to reduce this trust
boundary. Its generic semantics and substantial generated layers are
kernel-built, but the dependency-closed production replay is not yet
complete. See [`VERIFICATION_STATUS.md`](../VERIFICATION_STATUS.md).
