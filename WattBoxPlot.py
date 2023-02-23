import pandas as pd 
import os.path
import streamlit as st
import glob 
import matplotlib.pyplot as plt
import seaborn
import numpy as np


st.title('WattTime data for BANC in 2020')

#JOIN ALL DATA 
path = "BANC_historical"
all_files = glob.glob(os.path.join(path, "*2020*.csv"))

#PUT INTO DATAFRAME
WattTimeDf = pd.concat((pd.read_csv(f, parse_dates = ['timestamp'], index_col = ['timestamp']) for f in all_files))

#CREATE FIGURE FOR BOXPLOT
fig, ax = plt.subplots(figsize=(20,5))

#CREATE BOXPLOT
myboxplot = seaborn.boxplot(x = WattTimeDf.index.month, y = WattTimeDf["MOER"], ax = ax)

#DISPLAY WITH STREAMLIT
st.subheader("watt time box plot for banc 2020 data grouped by month")
st.pyplot(fig)
