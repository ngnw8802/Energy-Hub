import pandas as pd 
import os.path
import streamlit as st
import glob 
import matplotlib.pyplot as plt
import seaborn
import numpy as np



#PUT DATA INTO DATAFRAME AND PARSE DATES
SingBANCData = pd.read_csv('2020_carbon_accounting_hourly_us_units/BANC.csv', parse_dates=['datetime_utc'], index_col=['datetime_utc'])

#CREATE FIGURE TO DISPLAY BOXPLOT
fig, ax = plt.subplots(figsize=(20,5))

#CREATE BOXPLOT
myboxplot = seaborn.boxplot(x = SingBANCData.index.month, y = SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'], ax = ax)


#SINGULARITY DATA DISPLAYED WITH STREAMLIT
st.title('Singularity data for BANC in 2020')
st.subheader("boxplot grouped by month for Singularity BANC 2020 data")
st.pyplot(fig)



