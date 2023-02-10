import streamlit as st
import datetime
from scipy.stats import norm
from components.singularity_banc_2020 import *
from components.watttime_banc_2020 import *
import numpy as np

st.subheader(singsub)
st.write(SingBANCData)

st.subheader(wattsub)
st.write(WattTimeDf)

# Choose balancing authority to be displayed
option = st.selectbox(
    'Which balancing authority would you like to display?',
    ('BANC', 'AEC', 'AECI', 'AVA', 'AZPS'))
BAselection = option + ".csv"
fileToRead = "data/" + BAselection
selectBoxChoice = pd.read_csv(fileToRead)

# Choose timeframe to be displayed
startDate = datetime.date(2020, 1, 1)
d = st.date_input(
    "Select the start date of timeframe to be displayed (must be in year 2020):",
    startDate)

startDate = d
startDate = str(startDate)
if (startDate == "2020-01-01"):
    start = startDate + " 08:00:00+00:00"
else:
    start = startDate + " 00:00:00+00:00"

endDate = datetime.date(2020, 12, 31)
d = st.date_input(
    "Select the end date of timeframe to be displayed (must be in year 2020):",
    endDate)
endDate = d
endDate = str(endDate)
end = endDate + " 23:00:00+00:00"

# Create new dataframe with user selected dates for Singularity data
mask = (selectBoxChoice['datetime_utc'] >= start) & (selectBoxChoice['datetime_utc'] <= end)
selectBoxChoice = selectBoxChoice.loc[mask]

# Change start and end dates to be searchable in WattTime csv
WT_start = start.replace(" ", "T")
WT_end = end.replace(" ", "T")

# Create new dataframe with user selected dates using WattTime dataframe
# NOTE: unlike for the singularity charts, here we have hard coded in the balancing authority we are using
# This balancing authority data is grabbed in watttime_banc_2020.py
mask = (WattTimeDf['timestamp'] >= WT_start) & (WattTimeDf['timestamp'] <= WT_end)
WattTimeDf = WattTimeDf.loc[mask]

# Display Singularity area chart
st.write("Singularity Data Area Chart")
st.area_chart(data=selectBoxChoice, x="datetime_utc", y="consumed_co2_rate_lb_per_mwh_for_electricity")

# Display WattTime area chart
st.write("WattTime Data Area Chart")
st.area_chart(data=WattTimeDf, x="timestamp", y="MOER")

# Display Singularity line chart
st.write("Singularity Data Line Graph")
st.line_chart(data= selectBoxChoice,x="datetime_utc",y="consumed_co2_rate_lb_per_mwh_for_electricity")

# Display WattTime line chart
st.write("WattTime Data Line Graph")
st.line_chart(data= WattTimeDf,x="timestamp",y="MOER")

#caclulations for singularity data
charge = 30 #kWh
chargeType = 6 #Level 2 kW
timeCharge = charge/chargeType

st.write("Calculations for Electric Vehicle")
start = "2020-02-01 00:00:00-08:00"
end = "2020-02-01 23:00:00-08:00"

chunks = []

breakupDay = np.arange(0, 24, timeCharge)

for step in breakupDay:
    if step < 10:
        step = "0"+str(int(step))
    else:
        step = str(int(step))
    chunks.append("2020-02-01 "+ step + ":00:00-08:00")

mask = (SingBANCData['datetime_local']>start) & (SingBANCData['datetime_local']<=end)

day = SingBANCData.loc[mask]

st.write(day)

meanList = []

for data in range(len(chunks)-1):
    meanList.append(SingBANCData.loc[(SingBANCData['datetime_local']>chunks[data]) & (SingBANCData['datetime_local']<=chunks[data+1])]['consumed_co2_rate_lb_per_mwh_for_electricity'].mean())

bestMean = min(meanList)
bestIdx = meanList.index(bestMean)

for i in range(len(meanList)):
    if bestIdx==i:
        st.write("Best Time to Charge is:", chunks[i], "to", chunks[i+1])
    else:
        continue

st.line_chart(data= day,x="datetime_local",y="consumed_co2_rate_lb_per_mwh_for_electricity")