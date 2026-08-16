# Candidate release checklist

This checklist is for a GitHub research-draft release. It deliberately keeps
the reproducible mathematical artifact separate from the optional completion
of the full generated Lean build.

## Required before the first public release

- [x] Omit an author line rather than assigning human authorship that cannot be
  substantiated. Preserve explicit provenance for Ainta, Anthropic, the
  clean-room reproduction, and the AI-assisted revision.
- [x] Create the private staging repository
  `uwe-schwarz/zeta-simple-zeros-673026`. Keep it private until the release-day
  novelty review and a separate, explicit decision to publish.
- [x] Review the proof against the exact q2 theorem arithmetic and the cited
  Anthropic source.
- [x] Run `python3 -m unittest discover -s tests -v` from an extracted source
  distribution using the locked release environment.
- [x] Replay `zeta-zero-verify seven` or publish the existing frozen report
  together with its exact source and dependency hashes.
- [x] Run the exact downstream constant verifier and confirm the unique finite
  optimum, directed decimal enclosure, and positive tail checkpoints.
- [x] Build `paper/riemann.pdf` from `paper/riemann.tex` and visually inspect
  every displayed constant, table, URL, and page break.
- [x] Refresh the primary-source novelty comparison for this snapshot. Repeat
  it on the release day.
- [x] Confirm that README, paper, provenance notes, and the social post all use
  the same claim boundary: candidate, AI-assisted, unreviewed, reproducible Arb
  certificate, incomplete dependency-closed Lean replay.
- [x] Create a clean release manifest containing hashes of the verifier source,
  certificate report, paper source/PDF, and verification-status snapshot.
- [x] Build the source distribution and wheel without packaging warnings, then
  extract the source distribution and verify every release-manifest entry.
- [ ] Finish all 5,793 scaled Code-10 modules, validate the lane, transfer, and
  cross-host artifact attestations, and preserve those attestations in the
  release snapshot.

## Optional evidence before release

- [x] Include the already completed partitioned Code-9 terminal attestation.
- [ ] Include representative scaled Code-2 kernel logs without implying that
  all 3,979 modules were built.

## Deferred unless there is external interest

- [ ] Finish the full scaled Code-2 catalog.
- [ ] Execute the frozen 8,379-target final Lean plan.
- [ ] Run the public rehash build, negative fixtures, transitive axiom audit,
  `leanchecker --fresh`, and final analytic integration.

## Suggested release wording

> We present an AI-assisted, unreviewed candidate refinement of the
> Montgomery--Taylor simple-critical-line zero bound. A reproducible Arb
> certificate proves the exact finite inequality
> $F_6\ge382623/100000000$, yielding the candidate asymptotic constant
> $0.6730266625438475$. Substantial Lean components have been kernel-checked,
> but the dependency-closed production replay is not complete. Independent
> mathematical and computational review is welcome.
