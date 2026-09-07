I unpacked, ran, and audited the package. It builds cleanly, `--tests` passes, all 69 SHA256 sums verify, and the workbook has no formula errors. The lineage recovery itself worked: 22 modules are back and the double-count guards (RECONCILE\_ONLY electricity, working-stock vs durable CDR, BiCRS substitution) are correctly implemented.

But there is a submission-blocking problem, and it is not a dropped variable.

## 1. The external validation was run, it failed, and nothing in the package says so

`external_validation_results/` contains real results dated 2026-09-03:

- **FaIR 2.2.4**, fair-calibrate 1.4.1, 841 calibrated-constrained configs: `returning_configs: 0`, `nonreturn_fraction: 1.0`, all crossing percentiles `null`. **Zero of 841 members return to 280 ppm.** p50 CO₂ is 312.5 ppm in 2155, 302.0 in 2300, 294.2 in 2400. Even p05 is 290.3 ppm in 2400.
- **Hector 3.5.0**: minimum 295.96 ppm in **2156**, then rebounds to 304.9 by 2190 and sits at 297.3 in 2300. `first_le_280_year: null`, right-censored.

Both models were fed your own `external_validation_net_co2_trajectory.csv`. Meanwhile:

- `data/planetary_restoration_v55_results.json` → `external_validation_status`: "inherits the archived V53.1 external benchmark comparison."
- `README_V55.md` → same wording.
- Workbook `External_Validation` sheet → still `NOT_EXECUTED_DEPENDENCY_UNAVAILABLE_IN_BUILD_ENVIRONMENT`.
- Workbook `Nature_Readiness` → "Official calibrated/constrained FaIR benchmark: **OPEN — BLOCKING**".
- V53.1's own publication rule → "No precise restoration year may be presented as validated until official calibrated/constrained FaIR and an archived OSCAR configuration have been run."

So the package carries its own refutation inside a zip that no code path, no sheet and no document reads. The word "inherits" converts a blocking gate into a pass. A Nature reviewer who opens that zip — and they will, it is in the manifest — ends the review there.

The divergence is not noise. At 2155 the internal Joos core says 280.0 ppm; FaIR p50 says 312.5 and Hector says 296.0. The residual gap at 2155 is \~32.5 ppm ≈ **253 GtCO₂ of atmospheric removal still outstanding**, on top of the 1,835 GtCO₂ already spent. Two independent structurally different models agree with each other and disagree with yours, which points at your carbon core rather than at their configs.

Your Dashboard already diagnoses the mechanism: **"Joos fast box first negative — 2043"** and **"Joos natural flux first outgassing — 2067"**. The linear impulse-response is running 112 years past the year one of its reservoirs goes negative. Under sustained large negative emissions the ocean and land re-equilibrate and give carbon back; a symmetric IRF does not capture that state dependence. Hector's 9 ppm rebound between 2156 and 2190 is exactly this.

**What to do.** Do not submit until this is resolved. Three options, in order of defensibility:

1. Replace the Joos IRF as the headline carbon core with FaIR-calibrated output and report 280 ppm as **not reached within the analysis horizon**. This is a publishable result — "restoration to preindustrial CO₂ is unreachable on any financeable removal schedule; the binding constraint is sink reversal, not capital" is a stronger and more novel Nature paper than a 2155 date.
2. Keep Joos as a diagnostic only, report the FaIR 841-member spread as the result, and add a formal attribution decomposing the gap into (a) IRF state-dependence, (b) the 6 ppm initial-condition offset (FaIR 425.0 vs your 431.2 in 2026), (c) background non-CO₂ scenario, (d) post-2183 extension.
3. If you believe the external runs are misconfigured, that case must be made explicitly with the config archived — but you would be arguing against both FaIR and Hector simultaneously.

Two reproducibility gaps to close either way: your trajectory file ends in **2183** while FaIR ran to 2400 and Hector to 2300, and the extension assumption is undocumented; and V53.1 required **OSCAR**, not Hector. Hector is a reasonable independent SCM but it is a substitution that needs stating.

## 2. Variables still dropped

The recovery caught the v8–v23 lineage modules. It did not catch what fell out of **V53.1 itself**. The V53.1 results JSON has nine top-level blocks; V55's `v53_1_core` carries only `headline` and `ensemble_summary`. Seven blocks vanish from the V55 pipeline entirely:

| Dropped block What it contains    |                                                                                                                              |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `energy_and_grid`                 | **4/4 synthetic adequacy cases fail** at 0.01% unserved energy; VRE overbuild frontier 1.221–1.542×; grid-adjusted materials |
| `monetary_liquidity_stress`       | `all_cases_pass: False` — **3/6 fail** (Liquidity shock, Severe combined, Thirty-day run)                                    |
| `degraded_collection_physics`     | Degraded settlement collection propagated through the physical state                                                         |
| `central_joos_diagnostic_summary` | Initialization state, reversal 59.2 GtCO₂, permafrost 22.2 GtCO₂, per-pathway stock                                          |
| `scenario_matrix`                 | GDP, permafrost-τ, DACCS-cost and non-CO₂ case matrices                                                                      |
| `external_validation`             | The BLOCKING gate itself                                                                                                     |
| `primary_screen_headline`         | Duplicate of headline                                                                                                        |

Every one of the surviving results is favourable and every one of the dropped ones is unfavourable. That pattern is what a reviewer will name, regardless of intent. It is also self-inflicted: the three failed liquidity cases and the 4/4 grid failures are honest, interesting results that make the paper more credible, not less.

Also dropped and worth deciding on deliberately: **`Vegetarian_Fish`** **/ fisheries**. Six separate guard clauses in the seaweed branch protect against double-counting into "the core fish-stock headline" and "the core fish-recovery result" — but no fisheries module exists in V53.1, V54 or V55. Only a static literature line survives (`Wild-fish median recovery, 10 years`). Your manuscript scope lists fisheries. Either rebuild it or remove the phantom guards and the scope claim. Similarly absent from the register: `Human_Welfare_Floor`, `Demographics`, `Global_Economics`, `Industry_Materials`, `Population_Literature`, `Monetary_System_Risks`, `Diet_Carbon_v19`.

## 3. The seaweed central case is \~5× above what your own two internal checks support

`SeaweedBioeconomyInputs` uses 25 t dry/ha/yr over 586,000 km² = 1.465 Gt dry/yr. Two independent constraints inside the same module contradict it:

- **Nutrient balance**: `nutrient_supported_biomass_without_other_sources_gt_yr = 0.2526` — 17% of central. It needs 25.6 Mt N/yr and credits only 4.42 Mt.
- **Your own 2026 meta-analysis medians**: `ecosystem_median_biomass_accumulation_kgc_ha_yr = 1546` → 5.15 t dry/ha/yr at 30% C, i.e. 0.302 Gt/yr scaled to full area.

Two unrelated lines converge on 0.25–0.30 Gt/yr against a central case of 1.465. Both are currently reported as caution strings and neither propagates into food, hunger, population or fuel. Make the nutrient-limited case a headline scenario. It divides every seaweed-derived number by roughly five.

Related, smaller: there is **no ash term** anywhere, though macroalgae run 20–35% ash — the 17% HTL finished-fuel mass yield should be on an ash-free dry basis. And `edible_dry_kcal_kg = 2000` is gross energy; seaweed structural polysaccharides (alginate, fucoidan, laminarin) are largely indigestible to humans, so metabolizable energy is a fraction of that. Every capacity number downstream — 170.8 M full-diet equivalents, 682 M at a 500 kcal gap, the 10.371 B population screen — is proportional to that constant. A nutrition reviewer will go straight at it. Cite a metabolizable-energy source or reframe the whole module as protein and micronutrient supply rather than calories.

## 4. Headline framing

Your Dashboard is internally honest and your README is not. Dashboard: 2188 is the "primary V53.1 uncertainty headline"; 2155 is "high-ambition design; not central forecast" at **percentile rank 0.0275** — the 2.8th percentile of returning draws. README and `VALIDATION_V55.txt` lead with 2155/2153/2151. If the abstract inherits the README, you are leading with a 2.8th-percentile case, and the difference between 2151 and 2155 is four years inside a conditional 2158–2319 spread — a distinction with no meaning at that uncertainty. Report the ensemble as the result and the deterministic design as a corner case, or drop the additionality deltas from the headline.

Two more the reviewers will hit: `V55_ENERGY_ONLY_CAPACITY_B = 14.707241956010044` and `13.6159 B` population figures carry 17 and 6 significant figures on screening quantities with order-of-magnitude uncertainty — round to two. And `residual warming at ≤280 ppm = 0.762 °C` with residual non-CO₂ forcing of 0.788 W/m² is one of the best results in the package ("CO₂ restoration is not temperature restoration") and it is currently only in a Dashboard cell, not in the V55 pipeline.

## Priority order

1. Read the FaIR/Hector zips into the pipeline; resolve or reframe the 32.5 ppm divergence. Nothing else matters until this is done.
2. Restore the seven V53.1 blocks — especially the 4/4 grid failures and 3/6 liquidity failures — to the V55 output and to the manuscript.
3. Promote the nutrient-limited seaweed case (0.25 Gt/yr) to a headline scenario.
4. Fix the metabolizable-energy basis for seaweed calories, or reframe as protein/micronutrient.
5. Lead with 2188 and the ensemble spread, not 2155.
6. Decide on fisheries: rebuild or remove.
7. Run OSCAR, or state plainly that Hector substitutes for it.

The engineering discipline in this package is genuinely good — the RECONCILE\_ONLY discipline, the working-stock/durable-CDR separation and the BiCRS substitution rule are exactly the accounting hygiene reviewers look for. The problem is that the machinery built to prevent overclaiming was not applied to the one result that carries the paper.