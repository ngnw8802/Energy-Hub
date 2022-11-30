import streamlit as st
import datetime
from scipy.stats import norm
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

# Display WattTime line chart
st.write("WattTime Data Line Graph")
st.line_chart(data= WattTimeDf,x="timestamp",y="MOER")

#violin plot for singularity data
st.write("Violin plot for first 3 months of 2020 (singularity data)")
t1 = "2020-02-01 00:00:00-08:00"
t2 = "2020-03-01 00:00:00-08:00"
jan = SingBANCData.loc[SingBANCData['datetime_local']<t1]['consumed_co2_rate_lb_per_mwh_for_electricity']
feb = SingBANCData.loc[SingBANCData['datetime_local']<t2]['consumed_co2_rate_lb_per_mwh_for_electricity']
mar = SingBANCData.loc[SingBANCData['datetime_local']>=t2]['consumed_co2_rate_lb_per_mwh_for_electricity']

toplot = list([jan,feb,mar])

violin, ax = plt.subplots()

xticklabels = ['Jan 2020', 'Feb 2020','Mar 2020']
ax.set_xticks([1, 2,3])
ax.set_xticklabels(xticklabels)
#axes.violinplot(df1['MOER'])
ax.violinplot(toplot)
st.pyplot(violin)

#Singularity Variance/Distribution
singmu, singvar = norm.fit(SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'])

variances, s1 = plt.subplots()
xmin, xmax = SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'].min(), SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'].max()
xs = np.linspace(xmin, xmax, 100)
ps = norm.pdf(xs, singmu, singvar)
s1.hist(SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'], bins=25, density=True, alpha=0.6, color='b')
s1.plot(xs, ps, 'k', linewidth=2)

s1.set_title("Variance in Singularity Data")
s1.set_xlabel("Consumed CO2 Rate for Electricity (lb/mwh)")
s1.set_ylabel("Distribution")

st.pyplot(variances)

#wattmu, wattvar = norm.fit(WattTimeDf['MOER'])
#variancew, s2 = plt.subplots()
#xmin, xmax = WattTimeDf['MOER'].min(), WattTimeDf['MOER'].max()
#xw = np.linspace(xmin, xmax, 100)
#pw = norm.pdf(xw, wattmu, wattvar)
#s2.hist(WattTimeDf['MOER'], bins=25, density=True, alpha=0.6, color='r')
#s2.plot(xw, pw, 'k', linewidth=2)

#st.pyplot(variancew)