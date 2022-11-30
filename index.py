import streamlit as st
import datetime
from components.singularity_banc_2020 import *
from components.watttime_banc_2020 import *
from components.variance import *

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

#st.write("WattTime Data Line Graph")
#st.line_chart(data= WattTimeDf,x="timestamp",y="MOER")

st.write("Singularity Variance")
st.pyplot(fig_variance)

toplot = list([jan,feb,mar])

violin, ax = plt.subplots()

xticklabels = ['Jan 2020', 'Feb 2020','Mar 2020']
ax.set_xticks([1, 2,3])
ax.set_xticklabels(xticklabels)
#axes.violinplot(df1['MOER'])
ax.violinplot(toplot)
st.pyplot(violin)

# print("Mean of CO2 rate lb per mwh for electricity in BANC is(from singulairty) for 2020: ")
# print(SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'].mean())

# print("Variance of CO2 rate lb per mwh for electricity in BANC is(from singulairty) for 2020: ")
# print(SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'].var()) 

# token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6ImJhc2ljLGRhdGE9QVpQUzpTUlA6UEpNX0RDOkVSQ09UX0FVU1RJTjpTUFBfS0M6Q2FsaWZvcm5pYV9hbGwsbWFwcyIsImlhdCI6MTY2NzQwMzgyNywiZXhwIjoxNjY3NDA1NjI3LCJpc3MiOiJXYXR0VGltZSIsInN1YiI6Imp1c3Rpbl9lbmVyZ3lodWIifQ.f-XXRaa0Vw8jLMJRFP7g4fJH59St3uxkCNwAKcgNXIjuOMC9pWwYbuA7YeCpUciKDBCfcVkiwep9yDk4ryidnpL_JoadVFaiOXbdoBSzk5Cx9k2wykKbfNet4cv7DbNk-PnFtJ9sTY5BA43h2DSLQP0fd5MeofPnGRvPDwOD2fK5HQIQtYbyPqS-sIRrztCRpb2JzQIqiGbVsl_TcnfzszaszsNHBMq-sBl52CzYgXQrUjhI7cJ2KtjTB6NWowec9poBEd4o7Y6rVbeD5VfigturGTjJCI2Y2puz2YP2EH1cGW3xjHF5oSxZwTx8m94MoV-Ep9B9wAf4u8AASbOPkg"

# print('Mean of MOER in BANC from Wattime for 2020 is: ')
# print(WattTimeDf['MOER'].mean())

# print('Var of MOER in BANC from Wattime for 2020 is: ')
# print(WattTimeDf['MOER'].var())
