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

The complete 289,646-terminal mean-value interval catalog has passed its
5,793-module production build. The release preserves four exact markers:

- [`code10-low-lane-all-pass.json`](code10-low-lane-all-pass.json), covering
  modules 0--4,499, SHA-256
  `14dbf1ea754ce8bcefa8f11b1a84d8db215588ddeda18f4815c26a8f039f5489`;
- [`code10-high-lane-all-pass.json`](code10-high-lane-all-pass.json), covering
  modules 4,507--5,792, SHA-256
  `2260fecc058e235543789ec5c2bedd50db714d1171a11755d57429259c5ba2cc`;
- [`code10-transfer-all-pass.json`](code10-transfer-all-pass.json), whose
  canonical Lake-mode kernel replay closes modules 4,500--4,506 and attests
  all 5,793 modules and 28,965 build artifacts, SHA-256
  `8a60225477fec2d69c687a7d20e8b2d8ecd9a8ef12a8c245b6ce5f1a08656122`;
- [`code10-artifact-digest-all-pass.json`](code10-artifact-digest-all-pass.json),
  which independently obtains the same content digest on macOS and Linux,
  SHA-256
  `aa81e456fbbb6788d2fdd0e34f3bd43cf9431a70f9a6bbb6f2879f621b0365ef`.

The common cross-host artifact digest is
`f1c6957723a027456bacc348667c0adba61a0de547b4d3c9b18371b7c33e5cb1`.
This completes the scaled Code-10 catalog only; it is not a clean Linux
rehash of the final finite theorem.

## Deferred evidence

The full 3,979-module scaled Code-2 catalog, frozen final build plan, public
rehash, negative fixtures, transitive axiom audit, `leanchecker --fresh`, and
analytic integration remain deferred. See
[`../../VERIFICATION_STATUS.md`](../../VERIFICATION_STATUS.md) for the exact
claim boundary.
