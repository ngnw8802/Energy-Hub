import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = '2020_carbon_accounting_hourly_us_units/CISO.csv'

df = pd.read_csv(file_path)

CISOdata = df['consumed_co2_rate_lb_per_mwh_for_electricity'].to_list()

# Histogram of CO2 emissions for CISO 2020
CISO_histogram_tile = "CISO: Consumed_co2_rate_lb_per_mwh_for_electricity"
fig_histogram, ax = plt.subplots(figsize=(10,10)) 
ax.hist(CISOdata, bins = 20)
#ax.set_title('CISO: consumed_co2_rate_lb_per_mwh_for_electricity', fontsize=18)