# Planetary Restoration Model Version 56.0
## Audit-Corrected External Validation

Version 56 is a corrective release built from V55 after a line-by-line external audit. Its central change is scientific hierarchy: **the archived external carbon-cycle runs are now the primary validation result**. The internal Joos four-reservoir calculation remains useful for diagnostics and controller testing, but it is no longer presented as a validated restoration-date engine under sustained large negative emissions.

## Primary result

The archived V53.1/V55 net-CO2 pathway **does not return atmospheric CO2 to 280 ppm within the archived external-model horizons**:

- **FaIR 2.2.4 / fair-calibrate 1.4.1:** 0 of 841 calibrated-constrained configurations reach <=280 ppm through 2400. Median CO2 is about **312.55 ppm in 2155**, **302.03 ppm in 2300**, and **294.23 ppm in 2400**; the 2400 p05/p50/p95 range is about **290.29 / 294.23 / 297.90 ppm**.
- **Hector 3.5.0:** no <=280 ppm crossing through 2300. CO2 reaches a minimum of about **295.96 ppm in 2156**, then rebounds, including about **304.89 ppm in 2190**, and is about **297.34 ppm in 2300**.

Accordingly, V56 reports **no externally validated return year**.

The V53.1 internal 700-draw ensemble conditional median of **2188** and the accelerated Joos crossing of **2155** remain in the package only as internal model context. The 2155 design is near the optimistic tail of the internal returning draws (~2.8th percentile), and neither date overrides the archived external results.

## Why the carbon-cycle result changed

The internal Joos diagnostic reaches a regime that is explicitly flagged as problematic for a headline calculation: its fast reservoir becomes negative in **2043**, and the model's natural reservoir flux first reverses to outgassing in **2067**. At 2155, the internal diagnostic is near 280 ppm while the FaIR median remains near 312.55 ppm. V56 therefore treats state-dependent sink reversal as an unresolved binding Earth-system issue rather than hiding the divergence.

The archived external benchmark extends the canonical annual net-CO2 pathway beyond its 2183 endpoint by holding the 2183 annual net flux constant. This extension is documented in `external_validation_workflow/BENCHMARK_EXTENSION_NOTE.md` and is a validation-extension assumption, not a V56 emissions forecast.

## V53.1 adverse results restored

V56 propagates the complete V53.1 top-level result object, including results that are unfavorable:

- **4/4** default synthetic grid-adequacy cases fail the strict 0.01% unserved-energy criterion.
- **3/6** monetary-liquidity stress cases fail: Liquidity shock, Severe combined, and Thirty-day run.
- Severe settlement-migration stress materially constrains funded CDR and is right-censored without return by 2400 in the internal physical screen.
- The full Joos diagnostic, scenario matrix, external-validation gate, energy/grid block and monetary-liquidity block are all preserved.

These are not treated as defects to conceal; they are model findings and constraints.

## Seaweed correction

V55 treated 0.586 million km2 at 25 dry t/ha/yr as the central production scale: 1.465 Gt dry biomass/yr. V56 distinguishes three cases:

1. **Nutrient-closed central:** about **0.253 Gt dry/yr**, the biomass supported by the explicitly credited eutrophic N/P supply in the current mass balance.
2. **External ecosystem-accumulation benchmark:** about **0.302 Gt dry/yr** when the 2026 ecosystem-services meta-analysis median biomass accumulation is translated into a dry-biomass equivalent. This is context only; it is not treated as a cultivated farm-yield ceiling.
3. **Managed-nutrient geometric potential:** **1.465 Gt dry/yr**, retained as a high engineering scenario that requires roughly **21.2 Mt N/yr** and **0.86 Mt P/yr** of additional natural or managed nutrient flux to be demonstrated regionally.

### Ash and fuel

V56 adds a central **25% dry-mass ash fraction** with 20–35% sensitivity. The 17% HTL/upgrading finished-fuel mass yield is now applied to **ash-free dry organic matter**, not total dry biomass.

Under the nutrient-closed central case and the existing 5/80/10/5 food/fuel/storage/material allocation, this gives approximately:

- **0.253 Gt dry biomass/yr**
- **12.63 Mt dry food-grade seaweed/yr**
- **0.884 Mt/yr digestible protein** in the 70% protein-digestibility screen
- **308 TWh/yr** finished liquid-fuel energy
- **2.70 TWh/yr** Grid Harvesting electricity

The managed-nutrient 1.465 Gt/yr case remains available, but it is no longer the primary nutrient-closed result.

## Seaweed food and calories

V56 no longer treats the older **2,000 kcal/kg dry seaweed** composition value as metabolizable human energy. Mixed seaweeds have highly species- and processing-dependent digestibility, while much seaweed carbohydrate is dietary fiber or otherwise poorly digested by humans.

V56 therefore reports:

- gross protein;
- a 70% human protein-digestibility screen;
- an intentionally conservative **protein-only metabolizable-energy floor of 280 kcal/kg dry** (10% protein x 70% digestibility x 4 kcal/g);
- the old **2,000 kcal/kg figure only as a gross upper/composition screen**.

This is deliberately conservative and does not assume carbohydrate contributes zero energy in reality. Species-specific human metabolizable-energy studies are required before a single calorie number can become a primary food-capacity claim.

## Fisheries restored

V56 restores an explicit fisheries layer, but it is literature-bounded rather than a fictitious stock-by-stock global simulation. It reports:

- 62.4% of assessed marine stocks biologically sustainable in the retained 2023/FAO reference;
- 72.6% of assessed-stock landings from biologically sustainable stocks;
- an illustrative ~10-year median managed-stock recovery sensitivity under effective reform;
- a 2050 literature planning horizon in which about 98% of modeled fisheries in the cited global reform study are biologically healthy.

Seaweed co-culture and habitat are **not** counted as wild-fish stock recovery.

## Restored human/economic modules

V56 also restores explicit screens for:

- Human Welfare Floor (updated to a 2,350 kcal/person/day central consumption screen);
- Demographics;
- Global Economics;
- Industry Materials;
- Population Literature/context;
- Monetary System Risks;
- historical Diet Carbon scenarios.

Population figures are rounded and reported as scenario context. **V56 does not claim that Earth has one immutable maximum human carrying capacity.**

## OSCAR status

V53.1's release rule required calibrated/constrained FaIR and an archived OSCAR configuration. V56 contains the completed FaIR run and an independent Hector run, but **Hector is not OSCAR**. OSCAR therefore remains an open publication gate unless the validation protocol is explicitly revised and justified.

## Submission status

**V56 is not marked submission-ready.** The principal scientific issue is no longer hidden: the proposed finance/engineering architecture can be evaluated independently, but the archived external carbon-cycle models do not validate a precise return to 280 ppm under the tested net-CO2 trajectory.

This reframing is intentional. A defensible paper can report that **carbon-cycle sink response, rather than finance alone, becomes a binding constraint on atmospheric restoration**.
