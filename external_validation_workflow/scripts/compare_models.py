#!/usr/bin/env python3
from pathlib import Path
import json, pandas as pd, numpy as np
root=Path(".")
internal=pd.read_csv("validation_input/annual_state.csv")
fairp=root/"external_results/fair/fair_v2_2_4_timeseries.csv"
hectorp=root/"external_results/hector/hector_v3_5_0_timeseries_long.csv"
rows=[]
if fairp.exists():
    f=pd.read_csv(fairp)
    m=internal.merge(f,on="year",how="inner")
    rows.append({
        "model":"FaIR 2.2.4 median",
        "overlap_years":len(m),
        "co2_rmse_ppm":float(np.sqrt(np.mean((m.co2_ppm-m.co2_p50_ppm)**2))),
        "temperature_rmse_c":float(np.sqrt(np.mean((m.surface_warming_c-m.temperature_p50_c)**2))),
        "first_le_280_year":int(f.loc[f.co2_p50_ppm<=280,"year"].iloc[0]) if (f.co2_p50_ppm<=280).any() else None
    })
if hectorp.exists():
    h=pd.read_csv(hectorp)
    co2=h[h.variable.astype(str).str.contains("CO2",case=False,regex=False)][["year","value"]].rename(columns={"value":"hector_co2"})
    m=internal.merge(co2,on="year",how="inner")
    rows.append({
        "model":"Hector 3.5.0",
        "overlap_years":len(m),
        "co2_rmse_ppm":float(np.sqrt(np.mean((m.co2_ppm-m.hector_co2)**2))),
        "temperature_rmse_c":None,
        "first_le_280_year":int(co2.loc[co2.hector_co2<=280,"year"].iloc[0]) if (co2.hector_co2<=280).any() else None
    })
Path("external_results").mkdir(exist_ok=True)
pd.DataFrame(rows).to_csv("external_results/model_comparison_summary.csv",index=False)
Path("external_results/model_comparison_summary.json").write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
