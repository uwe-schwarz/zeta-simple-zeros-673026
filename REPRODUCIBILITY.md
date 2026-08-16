# Fresh reproducibility evidence

Replay date: 2026-08-16

This is a fresh execution of the standalone q2 verifier from the candidate
release tree. It is independent of the long generated Lean production build.

## Environment

| Component | Version |
| --- | --- |
| operating system | macOS 26.6.1, arm64 |
| Python | 3.11.15 |
| python-flint | 0.9.0 |
| Arb precision used by verifier | 128 bits |
| PDF builder | Tectonic 0.17.0 |

## Command

```bash
.venv/bin/zeta-zero-verify seven --progress-every 100000
```

## Result

The command exited with status zero after 111.909243 seconds and reported:

```text
certificate=seven-point
verified=true
target=F6 >= 382623/100000000
grid=4000
precision_bits=128
kernel_table_sha256=5a1f95f754a83ba05f37692d4bda69bf3fa5d3752af902826bfc4cffd31428b9
initial_boxes=729
nodes=980069
pruned=490399
splits=489670
maximum_depth=65
interval_pruned=285258
pressure_pruned=3166
second_derivative_table_sha256=02589f9acbab9808a303f85cf14f5e98bcb6f30265a5542f9ccca5f9fe8c3b97
subcell_tangent_pruned=1773
surviving_gap_components_cells=[3807,4780];[7218,9373];[10560,44945]
surviving_gap_components_count=3
tangent_pruned=201975
terminal_subcell_max_depth=20
```

The structural counts, exact target, kernel-table hash, second-derivative
table hash, and surviving components match
[`certificates/seven-point-382623.txt`](certificates/seven-point-382623.txt).
The elapsed time is not expected to match and is not part of the mathematical
certificate identity.

The same run printed the downstream decimal:

```text
seven_point_bound=0.6730266625438475
```

## Exact downstream constant

The finite spectral conversion and block-size optimization are checked
separately with exact rational inputs and directed 256-bit Arb arithmetic:

```bash
.venv/bin/python verify_constants.py
```

The script verifies the exact closed-form identities used in the paper,
separates `m=279` from every other integer `7 <= m <= 1000`, identifies
`m=278` as the runner-up, checks the stated directed decimal enclosure, and
checks the two exact positive rational inequalities used by the monotonic
tail argument. It uses no binary floating-point value for a decision.

## Unit tests

Immediately before the replay, the release environment passed all seven unit
tests:

```text
Ran 7 tests in 0.179s
OK
```

After adding the exact constant verifier, the source distribution was rebuilt,
extracted into a fresh temporary directory, checked against
`RELEASE_MANIFEST.sha256`, and reran all seven tests plus
`verify_constants.py` successfully.
