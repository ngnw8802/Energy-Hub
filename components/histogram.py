import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#file_path = '2020_carbon_accounting_hourly_us_units/CISO.csv'
#df = pd.read_csv(file_path)
#CISOdata = df['consumed_co2_rate_lb_per_mwh_for_electricity'].to_list()

SingBANCData = pd.read_csv('data/BANC.csv')
BANCdata = SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'].to_list()

fig_histogram, ax = plt.subplots(figsize=(10,10)) 
ax.hist(BANCdata, bins = 20)