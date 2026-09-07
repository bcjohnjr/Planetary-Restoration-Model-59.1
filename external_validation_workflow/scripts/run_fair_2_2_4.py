#!/usr/bin/env python3
"""Official FaIR 2.2.4 benchmark runner for the frozen V53.1 net-CO2 pathway.

Networked prerequisites:
  pip install fair==2.2.4 pandas numpy
  git clone --depth 1 --branch v2.2.4 https://github.com/OMS-NetZero/FAIR.git FAIR-v2.2.4

The script uses FaIR's official calibration-1.4.1 files and the "medium-extension"
background scenario for non-CO2 emissions/solar/volcanic forcing, while replacing
CO2 FFI + AFOLU after 2026 with the exact V53.1 annual net-CO2 flux:
  CO2 FFI = V53.1 net CO2
  CO2 AFOLU = 0
This is an intentionally transparent net-CO2 carbon-cycle benchmark. It does not
pretend that V53.1 permafrost/reversal/CDR terms are fossil emissions physically.
"""
from pathlib import Path
import argparse, json, os
import numpy as np
import pandas as pd
from fair import FAIR
from fair.interface import fill, initialise
from fair.io import read_properties

def first_crossing(years, values, threshold=280.0, start=2026):
    hit = [int(round(y)) for y, v in zip(years, values) if y >= start and v <= threshold]
    return hit[0] if hit else None

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--fair-repo", default=os.environ.get("FAIR_REPO","FAIR-v2.2.4"))
    ap.add_argument("--trajectory", default="validation_input/external_validation_net_co2_trajectory_extended_to_2400.csv")
    ap.add_argument("--outdir", default="external_results/fair")
    args=ap.parse_args()
    repo=Path(args.fair_repo)
    data=repo/"examples/data/calibrated_constrained_ensemble"
    params=data/"calibrated_constrained_parameters_calibration1.4.1.csv"
    species_cfg=data/"species_configs_properties_calibration1.4.1.csv"
    emissions=data/"extensions_1750-2500.csv"
    forcing=data/"volcanic_solar.csv"
    for p in (params,species_cfg,emissions,forcing):
        if not p.exists(): raise FileNotFoundError(p)

    traj=pd.read_csv(args.trajectory)
    f=FAIR(ch4_method="Thornhill2021")
    f.define_time(1750, 2400, 1)
    f.define_scenarios(["medium-extension"])
    cfg=pd.read_csv(params,index_col=0)
    f.define_configs(cfg.index)
    species, properties=read_properties(filename=species_cfg)
    f.define_species(species,properties)
    f.allocate()
    f.fill_from_csv(emissions_file=emissions, forcing_file=forcing)
    fill(f.forcing, f.forcing.sel(specie="Volcanic") * cfg["forcing_scale[Volcanic]"].values.squeeze(), specie="Volcanic")
    fill(f.forcing, f.forcing.sel(specie="Solar") * cfg["forcing_scale[Solar]"].values.squeeze(), specie="Solar")
    f.fill_species_configs(species_cfg)
    f.override_defaults(params)
    initialise(f.concentration, f.species_configs["baseline_concentration"])
    initialise(f.forcing, 0)
    initialise(f.temperature, 0)
    initialise(f.cumulative_emissions, 0)
    initialise(f.airborne_emissions, 0)
    initialise(f.ocean_heat_content_change, 0)

    # FaIR emissions live at timepoints (mid-year). Map annual V53.1 values by floor(timepoint).
    year_to_net={int(r.year):float(r.net_co2_gtco2) for r in traj.itertuples()}
    ffi=f.emissions.loc[dict(scenario="medium-extension",specie="CO2 FFI")]
    afolu=f.emissions.loc[dict(scenario="medium-extension",specie="CO2 AFOLU")]
    for i,tp in enumerate(f.timepoints):
        yr=int(np.floor(float(tp)))
        if yr in year_to_net:
            ffi[i,:]=year_to_net[yr]
            afolu[i,:]=0.0
    f.emissions.loc[dict(scenario="medium-extension",specie="CO2 FFI")]=ffi
    f.emissions.loc[dict(scenario="medium-extension",specie="CO2 AFOLU")]=afolu
    f.run(progress=False)

    years=np.asarray(f.timebounds,float)
    co2=np.asarray(f.concentration.loc[dict(scenario="medium-extension",specie="CO2")])
    temp=np.asarray(f.temperature.loc[dict(scenario="medium-extension",layer=0)])
    # xarray arrays are time x config here
    outdir=Path(args.outdir); outdir.mkdir(parents=True,exist_ok=True)
    q=[0.05,0.5,0.95]
    co2q=np.quantile(co2,q,axis=1); tq=np.quantile(temp,q,axis=1)
    pd.DataFrame({
        "year":years,
        "co2_p05_ppm":co2q[0],"co2_p50_ppm":co2q[1],"co2_p95_ppm":co2q[2],
        "temperature_p05_c":tq[0],"temperature_p50_c":tq[1],"temperature_p95_c":tq[2],
    }).to_csv(outdir/"fair_v2_2_4_timeseries.csv",index=False)
    crossings=[]
    for j,c in enumerate(cfg.index):
        crossings.append({"config":str(c),"first_le_280_year":first_crossing(years,co2[:,j])})
    pd.DataFrame(crossings).to_csv(outdir/"fair_v2_2_4_crossings.csv",index=False)
    vals=[x["first_le_280_year"] for x in crossings if x["first_le_280_year"] is not None]
    summary={
        "model":"FaIR","version":"2.2.4","calibration":"fair-calibrate 1.4.1",
        "configs":len(crossings),"returning_configs":len(vals),
        "nonreturn_fraction":1-len(vals)/len(crossings),
        "crossing_p05":float(np.quantile(vals,.05)) if vals else None,
        "crossing_p50":float(np.quantile(vals,.5)) if vals else None,
        "crossing_p95":float(np.quantile(vals,.95)) if vals else None,
        "background_nonco2_scenario":"FaIR calibrated-constrained example: medium-extension",
        "co2_override":"V53.1 net CO2 mapped to CO2 FFI; CO2 AFOLU zero from 2026",
    }
    (outdir/"fair_v2_2_4_summary.json").write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary,indent=2))
if __name__=="__main__": main()
