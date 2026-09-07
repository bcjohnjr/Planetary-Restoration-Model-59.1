#!/usr/bin/env python3
import planetary_restoration_model_v56 as m
r = m.run_v56()
m.run_tests(r)
print("V56 AUDIT-CORRECTED TESTS PASSED")
print("FaIR returning configs:", r["external_validation_v56"]["fair"]["returning_configurations"], "/", r["external_validation_v56"]["fair"]["configurations"])
print("Hector minimum ppm:", r["external_validation_v56"]["hector"]["minimum_co2_ppm"])
print("Primary seaweed dry Gt/yr:", r["headline"]["v56_primary_seaweed_biomass_gt_dry_yr"])
