import pandas as pd 
import numpy as np
import os.path
import glob
import matplotlib.pylab as plt


path = "data"

#only want 2020 for now

all_files = glob.glob(os.path.join(path, "*2020*.csv"))
#print(all_files)

watt = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
sing = pd.read_csv('data/BANC.csv')

watt_variance_tile = "BANC: WattTime and Singularity Variance"
fig_variance, ax = plt.subplots(figsize=(10,10)) 

singvar = sing['consumed_co2_rate_lb_per_mwh_for_electricity'].var()
wattvar = watt['MOER'].var()

singmean = sing['consumed_co2_rate_lb_per_mwh_for_electricity'].mean()
wattmean = watt['MOER'].mean()

#print(singvar, wattvar, singmean, wattmean)

# Variance of CO2 emissions for BANC 2020
ax.boxplot(sing['consumed_co2_rate_lb_per_mwh_for_electricity'])

#ax.boxplot(watt['MOER'])