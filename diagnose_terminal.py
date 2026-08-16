#!/usr/bin/env python3
"""Bounded Arb diagnosis of the q=0.00382623 terminal basin cell."""

from __future__ import annotations

from collections import Counter
from typing import Sequence

from flint import arb, ctx, fmpq

from zeta_simple_zeros.kernel import kernel_constants, squared_kernel_derivatives
from zeta_simple_zeros.verify_seven import (
    COEFFICIENT_RATIONALS,
    GRID,
    PRESSURE_DENOMINATOR,
    TARGET_DENOMINATOR,
    TARGET_NUMERATOR,
)


CELL = (4184, 7956, 7945, 4166, 7907, 4179)
MAX_DEPTH = 24
MAX_VISITED = 1_000_000


def tangent_data_at(
    midpoints: Sequence[fmpq], radii: Sequence[fmpq]
) -> tuple[arb, arb, list[arb], list[arb]]:
    constants = kernel_constants()
    value = sum((arb(point) for point in midpoints), arb(0)) / PRESSURE_DENOMINATOR
    gradient = [arb(fmpq(1, PRESSURE_DENOMINATOR)) for _ in range(6)]
    for span in range(1, 7):
        coefficient = arb(COEFFICIENT_RATIONALS[span])
        for start in range(7 - span):
            point = sum(midpoints[start : start + span], fmpq(0))
            potential, derivative, _ = squared_kernel_derivatives(
                arb(point), constants
            )
            value += coefficient * potential
            for coordinate in range(start, start + span):
                gradient[coordinate] += coefficient * derivative
    errors = [
        derivative.abs_upper() * arb(radius)
        for derivative, radius in zip(gradient, radii)
    ]
    return value - sum(errors, arb(0)), value, gradient, errors


def main() -> None:
    ctx.prec = 256
    target = arb(fmpq(TARGET_NUMERATOR, TARGET_DENOMINATOR))
    initial = [(fmpq(index, GRID), fmpq(index + 1, GRID)) for index in CELL]
    stack = [(initial, 0)]
    visited = accepted = 0
    splits_by_depth: Counter[int] = Counter()
    unresolved: list[tuple[list[tuple[fmpq, fmpq]], arb, arb, list[arb], list[arb]]] = []

    while stack:
        if visited >= MAX_VISITED:
            raise RuntimeError(f"visited-node cap exceeded: {MAX_VISITED}")
        bounds, depth = stack.pop()
        visited += 1
        midpoints = [(left + right) / 2 for left, right in bounds]
        radii = [(right - left) / 2 for left, right in bounds]
        lower, value, gradient, errors = tangent_data_at(midpoints, radii)
        if lower >= target:
            accepted += 1
            continue
        if depth >= MAX_DEPTH:
            unresolved.append((bounds, lower, value, gradient, errors))
            continue
        coordinate = max(range(6), key=lambda index: float(errors[index].upper()))
        left, right = bounds[coordinate]
        midpoint = (left + right) / 2
        lower_half = list(bounds)
        upper_half = list(bounds)
        lower_half[coordinate] = (left, midpoint)
        upper_half[coordinate] = (midpoint, right)
        stack.append((lower_half, depth + 1))
        stack.append((upper_half, depth + 1))
        splits_by_depth[depth] += 1

    print(f"target={TARGET_NUMERATOR}/{TARGET_DENOMINATOR}")
    print("cell=" + ",".join(str(index) for index in CELL))
    print(f"max_depth={MAX_DEPTH}")
    print(f"visited={visited}")
    print(f"accepted={accepted}")
    print(f"unresolved={len(unresolved)}")
    print(
        "splits_by_depth="
        + ",".join(f"{depth}:{count}" for depth, count in sorted(splits_by_depth.items()))
    )
    if unresolved:
        worst = min(unresolved, key=lambda row: row[1].lower())
        bounds, lower, value, gradient, errors = worst
        print("worst_bounds=" + ";".join(f"[{left},{right}]" for left, right in bounds))
        print(f"worst_lower={lower}")
        print(f"worst_value={value}")
        print("worst_gradient=" + ";".join(str(item) for item in gradient))
        print("worst_errors=" + ";".join(str(item) for item in errors))
        print(f"worst_target_minus_lower={target - lower}")
        print(f"worst_value_minus_target={value - target}")


if __name__ == "__main__":
    main()
