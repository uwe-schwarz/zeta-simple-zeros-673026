"""Closed-form constants occurring in the two certificates."""

from __future__ import annotations

import math


H0 = 1.5 - (1.0 / math.sqrt(2.0)) / math.tan(1.0 / math.sqrt(2.0))
"""Anthropic's Montgomery-Taylor constant (Theorem D)."""


def three_point_bound(epsilon: float) -> float:
    """Return (H0 - epsilon/4) / (1 - epsilon/2)."""

    if not 0.0 < epsilon <= 1.0:
        raise ValueError("epsilon must lie in (0, 1]")
    return (H0 - epsilon / 4.0) / (1.0 - epsilon / 2.0)


def seven_point_bound() -> float:
    """Return the bound produced by the certified F6 >= 382623/100000000 inequality."""

    q = 382_623.0 / 100_000_000.0
    block_size = 279.0
    energy = q * (block_size - 6.0)
    defect = (
        energy / block_size
        + 2.0 * math.sqrt((block_size - 1.0) * energy / block_size)
        - 1.0
    )
    span_loss = (block_size - 1.0) / (500.0 * block_size)
    return (H0 - span_loss) / (1.0 - defect / block_size)
