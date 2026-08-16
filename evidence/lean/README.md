# Lean build evidence

This directory preserves small completion attestations from the generated Lean
certificate-consumer builds. It does not contain the multi-gigabyte generated
source tree or platform-specific `.olean` files, and it is not a substitute for
the deferred dependency-closed build of the public theorem.

## Partitioned Code-9 catalog

[`code9-partitioned-all-pass.json`](code9-partitioned-all-pass.json) is the
terminal marker emitted by the serial Linux production build. It records:

- source metadata SHA-256
  `917f72bd33a3a97e0bbbf1b0c1d96fb53a22967e06ac946af8b4033c1ea516cf`;
- 6,350 dependency-ordered targets;
- terminal status `PASS` at `2026-08-16T02:55:28Z`.

The marker file itself has SHA-256
`19e57216c7aebd86e2fa1870476eadfb89b3ffde010faa320090c75845434bb9`.
Its scope is the complete 1,773-terminal partitioned Code-9 catalog, not the
final finite theorem.

## Scaled Code-10 catalog

The lane, transfer, and cross-host artifact attestations will be added here
only after all 5,793 modules have completed and the existing fail-closed
finalizer has accepted them.

## Deferred evidence

The full 3,979-module scaled Code-2 catalog, frozen final build plan, public
rehash, negative fixtures, transitive axiom audit, `leanchecker --fresh`, and
analytic integration remain deferred. See
[`../../VERIFICATION_STATUS.md`](../../VERIFICATION_STATUS.md) for the exact
claim boundary.
