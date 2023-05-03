import streamlit as st
import datetime
import pandas as pd
from PIL import Image

def calculate(chargeAmt, chargeRate, Data):
    # chargeAmt is amount (kWh) needed to be charged and chargeRate is charge rate (kW)
    # timeCharge is the amount of time (hours currently) that charging needs to occur to fill battery
    timeCharge = chargeAmt / chargeRate

    # total number of rows in dataframe (each row is an hour)
    totalHoursStored = Data.shape[0]

    meanCO2List = []
    timeStamps = []

    # create a list of mean CO2 emmissions using the "slider algorithm"
    # this means we are finding the mean emmissions between rows [0,9], then [1,10], then [2,11], and so on
    # we are also appending the corresponding timeStamps to a list for each mean emmissions appended to meanCO2List
    for i in range(int(totalHoursStored - timeCharge)):
        initialRow = Data.iloc[int(i)]
        startDate = initialRow["datetime_utc"]
        endRow = Data.iloc[int(i+timeCharge)]
        endDate = endRow["datetime_utc"]
        timeStamps.append((startDate, endDate))
        meanCO2List.append(Data.loc[(Data['datetime_utc']>startDate) & (Data['datetime_utc']<=endDate)]['consumed_co2_rate_lb_per_mwh_for_electricity'].mean())


    # find window with least emissions
    minMean = min(meanCO2List)
    bestIdx = meanCO2List.index(minMean)

    result = tuple()

    # dates to return are the tuple of dates with the same index as that of our min emmissions in meanCO2List
    # return time window tuple and min emissions and the min mean emissions rate itself in result
    for i in range(len(meanCO2List)):
        if bestIdx==i:
            result = (timeStamps[i], minMean)
        else:
            continue
    
    return result

image = Image.open('./header.png')
st.image(image)

col1, col2, col3 = st.columns([1,1,1])

# Choose balancing authority to be displayed
with col1: option = st.selectbox(
    'Balancing Authority:',
    ('AEC', 'AECI', 'AVA', 'AZPS', 'BANC', 'BPAT', 'CHPD', 'CISO', 'CPLE', 'CPLW', 'DOPD', 'DUK', 'EPE', 'ERCO', 'FMPP', 'FPC', 'FPL', 'GCPD', 'GVL', 'HST', 'IID', 'IPCO', 'ISNE', 'JEA', 'LDWP', 'LGEE', 'MISO', 'NEVP', 'NSB', 'NWMT', 'NYIS', 'PACE', 'PACW', 'PGE', 'PJM', 'PNM', 'PSCO', 'PSEI', 'SC', 'SCEG', 'SCL', 'SEC', 'SOCO', 'SPA', 'SRP', 'SWPP', 'TAL', 'TEC', 'TEPC', 'TIDC', 'TPWR', 'TVA', 'WACM', 'WALC', 'WAUW'))
BAselection = option + ".csv"
fileToRead2 = "data_2021/" + BAselection
Data2021 = pd.read_csv(fileToRead2)

with col2: chargeAmt = st.selectbox(
    'Amount to charge (kWh): ',
    ('10', '20', '30', '40', '50', '60'))
with col3: chargeRate = st.selectbox(
    'Charge rate (kW): ',
    ('3', '4', '5', '6'))

options = st.multiselect(
    'Emissions types to monitor',
    ['co2', 'ch4', 'n2o', 'co2e', 'nox', 'so2', 'co2_adjusted', 'ch4_adjusted', 'n2o_adjusted', 'co2e_adjusted', 'nox_adjusted', 'so2_adjusted'],
    'co2')

indicators = []
for x in options:
    if x == 'co2':
        indicators.append('consumed_co2_rate_lb_per_mwh_for_electricity')
    if x == 'co2_adjusted':
        indicators.append('consumed_co2_rate_lb_per_mwh_for_electricity_adjusted')
    if x == 'ch4':
        indicators.append('consumed_ch4_rate_lb_per_mwh_for_electricity')
    if x == 'ch4_adjusted':
        indicators.append('consumed_ch4_rate_lb_per_mwh_for_electricity_adjusted')
    if x == 'n2o':
        indicators.append('consumed_n2o_rate_lb_per_mwh_for_electricity')
    if x == 'n2o_adjusted':
        indicators.append('consumed_n2o_rate_lb_per_mwh_for_electricity_adjusted')
    if x == 'co2e':
        indicators.append('consumed_co2e_rate_lb_per_mwh_for_electricity')
    if x == 'co2e_adjusted':
        indicators.append('consumed_co2e_rate_lb_per_mwh_for_electricity_adjusted')
    if x == 'nox':
        indicators.append('consumed_nox_rate_lb_per_mwh_for_electricity')
    if x == 'nox_adjusted':
        indicators.append('consumed_nox_rate_lb_per_mwh_for_electricity_adjusted')
    if x == 'so2':
        indicators.append('consumed_so2_rate_lb_per_mwh_for_electricity')
    if x == 'so2_adjusted':
        indicators.append('consumed_so2_rate_lb_per_mwh_for_electricity_adjusted')

# data starts at hour 8 for 1/1/21. Code is hardcoded to be hour 8 for this day no matter what hour is selected
# Choose timeframe
startDate = datetime.date(2021, 1, 1)
endDate = datetime.date(2021, 12, 31)

col1, col2, col3 = st.columns([1,1,1])

with col1: d = st.date_input(
    "Day to start charging (2021):",
    startDate)

startDate = d
startDate = str(startDate)

with col2: hour = st.selectbox(
    'Hour to start charging: ',
    ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))

with col3: midDay = st.selectbox(
    ' ',
    ('am', 'pm'))
if midDay == 'am':
    if (startDate == "2021-01-01"):
        start = startDate + " 08:00:00+00:00"
    elif str(hour) == "12":
        start = startDate + " " + "00:00:00+00:00"
    elif len(str(hour)) == 2:
        start = startDate + " " + str(hour) + ":00:00+00:00"
    else:
        start = startDate + " " + "0" + str(hour) + ":00:00+00:00"
if midDay == 'pm':
    hour = int(hour)
    if hour == 12:
        start = startDate + " " + "12:00:00+00:00"
    else:
        hour += 12
        if (startDate == "2021-01-01"):
            start = startDate + " 08:00:00+00:00"
        else:
            start = startDate + " " + str(hour) + ":00:00+00:00"

col11, col22, col33 = st.columns([1,1,1])

with col11: d1 = st.date_input(
    "Day to end charging by (2021):",
    endDate)
endDate = d1
endDate = str(endDate)

with col22: hour2 = st.selectbox(
    'Hour to end charging by: ',
    ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))

with col33: midDay2 = st.selectbox(
    ' ',
    ('am', 'pm'), key = "1")
if midDay2 == 'am':
    if str(hour2) == "12":
        end = endDate + " " + "00:00:00+00:00"
    elif len(str(hour2)) == 2:
        end = endDate + " " + str(hour2) + ":00:00+00:00"
    else:
        end = endDate + " " + "0" + str(hour2) + ":00:00+00:00"
if midDay2 == 'pm':
    hour2 = int(hour2)
    if hour2 == 12:
        end = endDate + " " + "12:00:00+00:00"
    else:
        hour2 += 12
        end = endDate + " " + str(hour2) + ":00:00+00:00"

st.write(" ")
st.write(" ")
st.write(" ")

# create new dataframe with user selected dates for Singularity data
mask = (Data2021['datetime_utc'] >= start) & (Data2021['datetime_utc'] <= end)
Data2021 = Data2021.loc[mask]

chargeAmt = int(chargeAmt)
chargeRate = int(chargeRate)

# check if charge window is long enough based on inputs for "amount to charge" and "charge rate"
if int(chargeAmt/chargeRate) < int(Data2021.shape[0]):
    (timeStampTuple, emissions) = calculate(chargeAmt, chargeRate, Data2021)

else:
    st.write("You have selected to short of a timeframe to charge completely. Please expand your selected timeframe and try again.")
    st.stop()

st.write("Best to charge from", timeStampTuple[0][:-9], "to", timeStampTuple[1][:-9], "as average CO2 emissions on the power grid were", str(round(emissions, 2)), "rate_lb_per_mwh_for_electricity for this period.")

# code below here except for the last two lines serves to plot the light blue line on top of the dark blue line in our graph to show the optimal charging period
# create dataframe of optimal charge period and add suffix to column names of optimalChargeData so optimalChargeData and Data2021 can be plotted together
mask2 = (Data2021['datetime_utc'] >= timeStampTuple[0]) & (Data2021['datetime_utc'] <= timeStampTuple[1])
optimalChargeData = Data2021.loc[mask2].add_suffix('_2')

# concatenate the dataframes
df_combined = pd.concat([Data2021, optimalChargeData], axis=1)
df_combined = df_combined.set_index('datetime_utc')

# create a second list of emissions we want to track in the optimalChargeData df and combine it with the other indicators
indicators_2 = []
for ind in indicators:
    ind = ind + '_2'
    indicators_2.append(ind)
allInicators = indicators + indicators_2

# display 2020 ERCO Singularity line chart
st.line_chart(data = df_combined[allInicators])