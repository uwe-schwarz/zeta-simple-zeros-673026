#!/usr/bin/env python3
"""Verify the exact downstream constant with directed Arb arithmetic.

The local certificate ``F6 >= 382623/100000000`` is an exact input here.
This script independently checks the finite block-size optimization, the
closed form used in the paper, and the rational checkpoints used to control
the infinite tail.  No binary floating-point value is used in a decision.
"""

from __future__ import annotations

import importlib.metadata
import platform
import sys

from flint import arb, ctx, fmpq


PRECISION_BITS = 256
LOCAL_TARGET = fmpq(382_623, 100_000_000)
OPTIMAL_BLOCK_SIZE = 279
SCAN_LIMIT = 1_000

DECIMAL_LOWER_TEXT = (
    "0.673026662543847549657909021164263097878597771825043451997732504815857553753"
)
DECIMAL_UPPER_TEXT = (
    "0.673026662543847549657909021164263097878597771825043451997732504815857553754"
)


def exact_decimal(value: str) -> fmpq:
    """Convert a nonnegative finite decimal string to an exact rational."""

    whole, fractional = value.split(".")
    return fmpq(int(whole + fractional), 10 ** len(fractional))


def h0() -> arb:
    """Return the Montgomery--Taylor constant at the active Arb precision."""

    theta = 1 / arb(2).sqrt()
    return arb(fmpq(3, 2)) - theta * (theta.cos() / theta.sin())


def spectral_envelope(block_size: int) -> tuple[fmpq, fmpq, arb]:
    """Return A, the radical argument, and g_m(A), respectively."""

    energy = LOCAL_TARGET * (block_size - 6)
    if not (0 <= energy <= block_size * (block_size - 1)):
        raise AssertionError("energy lies outside the spectral-envelope domain")

    threshold = fmpq(block_size, block_size - 1)
    if energy <= threshold:
        return energy, fmpq(0), arb(energy)

    radical = fmpq(block_size - 1, block_size) * energy
    converted = arb(energy) / block_size + 2 * arb(radical).sqrt() - 1
    return energy, radical, converted


def final_bound(block_size: int) -> arb:
    """Return the directed-Arb enclosure of B_m."""

    _, _, converted = spectral_envelope(block_size)
    span_loss = fmpq(block_size - 1, 500 * block_size)
    denominator = 1 - converted / block_size
    if not (denominator > 0):
        raise AssertionError("nonpositive rearrangement denominator")
    return (h0() - arb(span_loss)) / denominator


def exact_dyadic_interval(value: arb) -> str:
    """Render Arb's outward enclosure without decimal conversion."""

    lower_mantissa, lower_exponent = value.lower().man_exp()
    upper_mantissa, upper_exponent = value.upper().man_exp()
    return (
        f"[{lower_mantissa} * 2^({lower_exponent}), "
        f"{upper_mantissa} * 2^({upper_exponent})]"
    )


def verify_closed_form() -> None:
    """Verify the exact algebra behind the paper's radical closed form."""

    energy, radical, _ = spectral_envelope(OPTIMAL_BLOCK_SIZE)
    linear = fmpq(11_606_231, 3_100_000_000)
    expected_radical = fmpq(1_613_266_109, 1_550_000_000)
    span_loss = fmpq(139, 69_750)
    scale = fmpq(3_100_000_000)

    assert energy == fmpq(104_456_079, 100_000_000)
    assert energy / OPTIMAL_BLOCK_SIZE == linear
    assert radical == expected_radical
    assert fmpq(OPTIMAL_BLOCK_SIZE - 1, 500 * OPTIMAL_BLOCK_SIZE) == span_loss

    # Multiplying numerator and denominator by this scale gives exactly
    # (864900000000 H0 - 1723600000) /
    # (867988393769 - 20000 sqrt(100022498758)).
    assert scale * OPTIMAL_BLOCK_SIZE == 864_900_000_000
    assert span_loss * 864_900_000_000 == 1_723_600_000
    assert scale * (280 - linear) == 867_988_393_769
    assert (2 * scale) ** 2 * radical == 20_000**2 * 100_022_498_758


def verify_finite_scan() -> tuple[arb, arb]:
    """Prove by disjoint intervals that m=279 uniquely wins the finite scan."""

    bounds = {block_size: final_bound(block_size) for block_size in range(7, SCAN_LIMIT + 1)}
    chosen = bounds[OPTIMAL_BLOCK_SIZE]
    runner_up = bounds[278]

    for block_size, candidate in bounds.items():
        if block_size != OPTIMAL_BLOCK_SIZE:
            assert chosen > candidate, (
                f"m={block_size} was not separated from m={OPTIMAL_BLOCK_SIZE}"
            )
        if block_size not in (OPTIMAL_BLOCK_SIZE, 278):
            assert runner_up > candidate, f"m={block_size} was not below runner-up m=278"

    assert chosen - runner_up > arb(fmpq(1_894_760_587_641_366, 10**24))
    return chosen, runner_up


def verify_tail_checkpoints() -> tuple[fmpq, fmpq]:
    """Verify the exact positivity checkpoints used for m >= 1000."""

    square_checkpoint = LOCAL_TARGET * 986 * 986 - 1_000
    derivative_checkpoint = 2 * LOCAL_TARGET * 986 - 1
    assert square_checkpoint == fmpq(67_996_137_527, 25_000_000)
    assert derivative_checkpoint == fmpq(163_633_139, 25_000_000)
    assert square_checkpoint > 0
    assert derivative_checkpoint > 0
    return square_checkpoint, derivative_checkpoint


def main() -> None:
    ctx.prec = PRECISION_BITS

    verify_closed_form()
    bound, runner_up = verify_finite_scan()
    square_checkpoint, derivative_checkpoint = verify_tail_checkpoints()

    decimal_lower = exact_decimal(DECIMAL_LOWER_TEXT)
    decimal_upper = exact_decimal(DECIMAL_UPPER_TEXT)
    assert bound > arb(decimal_lower)
    assert bound < arb(decimal_upper)

    energy, radical, converted = spectral_envelope(OPTIMAL_BLOCK_SIZE)
    print(f"python={sys.version.replace(chr(10), ' ')}")
    print(f"platform={platform.platform()}")
    print(f"python-flint={importlib.metadata.version('python-flint')}")
    print(f"precision_bits={PRECISION_BITS}")
    print(f"local_target={LOCAL_TARGET}")
    print(f"block_size={OPTIMAL_BLOCK_SIZE}")
    print(f"A={energy}")
    print(f"radicand={radical}")
    print(f"span_loss={fmpq(139, 69_750)}")
    print(f"H0={h0().str(80)}")
    print(f"C={converted.str(80)}")
    print(f"B={bound.str(80)}")
    print(f"B_exact_dyadic_enclosure={exact_dyadic_interval(bound)}")
    print(f"B_decimal_enclosure=[{DECIMAL_LOWER_TEXT}, {DECIMAL_UPPER_TEXT}]")
    print(f"B_m278={runner_up.str(80)}")
    print(f"B_m279_minus_B_m278={(bound - runner_up).str(50)}")
    print(f"finite_scan=unique maximum at m=279 for 7 <= m <= {SCAN_LIMIT}")
    print(f"tail_square_checkpoint={square_checkpoint}>0")
    print(f"tail_derivative_checkpoint={derivative_checkpoint}>0")
    print("verified=true")


if __name__ == "__main__":
    main()
