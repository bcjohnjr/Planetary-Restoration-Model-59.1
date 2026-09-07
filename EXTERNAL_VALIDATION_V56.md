# V56 External Validation Status

## FaIR

Archived package: `external_validation_results/fair-v2.2.4-results.zip`

- FaIR 2.2.4
- fair-calibrate 1.4.1
- 841 calibrated-constrained configurations
- 0 configurations reach <=280 ppm through 2400
- p50 CO2: ~312.55 ppm in 2155, ~302.03 ppm in 2300, ~294.23 ppm in 2400
- 2400 p05/p50/p95: ~290.29 / 294.23 / 297.90 ppm

**V56 interpretation:** external return year = **not reached within horizon**.

## Hector

Archived package: `external_validation_results/hector-v3.5.0-results.zip`

- Hector 3.5.0
- no <=280 ppm crossing through 2300
- minimum CO2 ~295.96 ppm in 2156
- ~304.89 ppm in 2190 after rebound
- ~297.34 ppm in 2300

**Role:** independent SCM comparison. Hector is not OSCAR.

## Joos diagnostic divergence

The V53.1 internal Joos diagnostic reaches ~280 ppm in 2155. At the same year FaIR p50 is ~312.55 ppm and Hector is ~295.99 ppm. The internal Joos fast reservoir becomes negative in 2043 and natural reservoir flux first becomes net outgassing in 2067. V56 therefore demotes Joos to diagnostic status under this large sustained drawdown.

## Trajectory extension

The canonical input trajectory ends in 2183. For external comparison beyond 2183, the benchmark holds the 2183 annual net-CO2 flux constant. See `external_validation_workflow/BENCHMARK_EXTENSION_NOTE.md`.

## OSCAR

Status: **OPEN**.

The original V53.1 publication gate required official IIASA OSCAR in addition to calibrated/constrained FaIR. V56 does not relabel Hector as OSCAR.
