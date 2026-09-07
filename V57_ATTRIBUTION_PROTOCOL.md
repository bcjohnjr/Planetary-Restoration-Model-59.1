# Version 57 FaIR attribution protocol

## Purpose
V57 treats the archived FaIR/Hector non-return as the scientific result to explain, not as a software failure. Two attribution questions are already closed from the archived outputs and two require a fresh official FaIR 2.2.4 execution.

## Time-index convention correction
The internal annual row labelled year **Y** is the state *after* applying that year's annual flux. In the archived FaIR runner, annual flux for Y is applied at timepoint Y+0.5 and changes concentration from timebound Y to timebound Y+1. Therefore internal 2155 must be compared with FaIR timebound 2156. The earlier V56 diagnostic comparing internal row 2026 with FaIR timebound 2026 was not a like-for-like initial-state comparison.

The internal model actually initializes at **428.73 ppm**, the NOAA global monthly mean for May 2026, before applying the 2026 flux. The archived FaIR p50 timebound at 2026 is 424.95 ppm. Removing this constant historical offset does **not** resolve the later discrepancy: the matched-start drawdown-response gap at the internal 2155 milestone is about **35.9 ppm**.

## Experiment A — common-state / time alignment
**Status: closed as an archived-output diagnostic; an official FaIR restart is still optional.**

1. Use 428.73 ppm as the common observational anchor for May 2026.
2. Compare internal state after year Y with FaIR timebound Y+1.
3. Report both the raw matched-step gap and the response-only gap after removing the constant 2026 historical p50 offset.

V57 result: the response-only gap is larger than the raw gap, so starting-state bias cannot explain the deep-drawdown divergence.

## Experiment B — no post-2183 extension
**Status: closed causally from the archived run.**

The canonical trajectory ends with annual input year 2183. Because FaIR is causal, the artificial constant-flux extension beginning after that year cannot alter any timebound through the end of the 2183 step. The archived FaIR p50 is about **311.40 ppm at timebound 2184**, after the final canonical 2183 flux has been applied. A separate run ending there would reproduce that value to numerical precision.

Thus the post-2183 extension matters for the 2300/2400 tail, but is not the reason the canonical programme itself fails to approach 280 ppm.

## Experiment C — zero background non-CO2 attribution
**Status: OPEN — official FaIR execution required.**

Run FaIR 2.2.4 / fair-calibrate 1.4.1 with the same CO2 pathway but a controlled future in which non-CO2 forcing after the common 2026 state is removed/held neutral using a documented restart procedure. Preserve the 2026 carbon and temperature state rather than silently erasing historical warming. This experiment must archive the exact state-restart implementation because simply zeroing non-CO2 emissions is not equivalent to zeroing non-CO2 forcing.

Primary output: difference in CO2 concentration and carbon uptake relative to the standard medium-extension run. This quantifies the component of sink weakening mediated by background non-CO2 warming.

## Experiment D — inverse removal schedule
**Status: OPEN — official FaIR execution required.**

Do not extrapolate a fixed ppm/Gt conversion. Iteratively solve an additional removal-control vector using the calibrated 841-member ensemble. At minimum report:

- target year(s): 2200, 2300, 2400;
- target statistic: p50 <= 280 ppm, plus p05/p95 concentrations;
- annual additional-removal ceiling and ramp-rate constraints;
- cumulative extra removal;
- fraction of configurations reaching <=280;
- the resulting temperature and sink-response trajectories.

A bisection/search over a simple post-2183 additional-removal multiplier is an acceptable first diagnostic, followed by a constrained piecewise schedule if the scalar multiplier is insufficient.

### Local-linear seed only
The archived 2301-2399 segment converts about 21% of cumulative net negative emissions into atmospheric mass decrease. Holding that response fraction fixed would imply roughly **527 GtCO2** of additional net removal to close the 2400 median gap. This is only a numerical seed for the inversion, **not** a removal requirement or forecast, because the response itself is state dependent.

## Runtime note
This ChatGPT build environment cannot install `fair==2.2.4` or clone the official calibration repository because outbound package/repository access is blocked. The archived official results are therefore retained, and unexecuted C/D experiments remain explicitly OPEN. Use `scripts/run_fair_2_2_4.py` with the official v2.2.4 repository/calibration files in a networked environment.
