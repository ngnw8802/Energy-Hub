import streamlit as st
import datetime
from components.singularity_erco_2020 import *
from components.singularity_erco_2021 import *
from PIL import Image

image = Image.open('./header.png')
st.image(image)

col1, col2, col3 = st.columns([1,1,1])

# Choose balancing authority to be displayed
with col1: option = st.selectbox(
    'Balancing Authority:',
    ('AEC', 'AECI', 'AVA', 'AZPS', 'BANC', 'BPAT', 'CHPD', 'CISO', 'CPLE', 'CPLW', 'DOPD', 'DUK', 'EPE', 'ERCO', 'FMPP', 'FPC', 'FPL', 'GCPD', 'GVL', 'HST', 'IID', 'IPCO', 'ISNE', 'JEA', 'LDWP', 'LGEE', 'MISO', 'NEVP', 'NSB', 'NWMT', 'NYIS', 'PACE', 'PACW', 'PGE', 'PJM', 'PNM', 'PSCO', 'PSEI', 'SC', 'SCEG', 'SCL', 'SEC', 'SOCO', 'SPA', 'SRP', 'SWPP', 'TAL', 'TEC', 'TEPC', 'TIDC', 'TPWR', 'TVA', 'WACM', 'WALC', 'WAUW'))
BAselection = option + ".csv"
fileToRead1 = "data_2020/" + BAselection
fileToRead2 = "data_2021/" + BAselection
selectBoxChoice1 = pd.read_csv(fileToRead1)
selectBoxChoice2 = pd.read_csv(fileToRead2)

with col2: charge = st.selectbox(
    'Amount to charge (kWh): ',
    ('10', '20', '30', '40', '50', '60'))
with col3: interval = st.selectbox(
    'Charge rate: ',
    ('1kW', '2kW', '3kW', '4kW', '5kW', '6kW'))

options = st.multiselect(
    'Emmissions types to graph',
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
mask = (selectBoxChoice1['datetime_utc'] >= start) & (selectBoxChoice1['datetime_utc'] <= end)
selectBoxChoice1 = selectBoxChoice1.loc[mask]

# Display 2020 ERCO Singularity line chart
st.write("Singularity 2020 Data Line Graph")
#st.line_chart(data= selectBoxChoice1,x="datetime_utc",y="consumed_co2_rate_lb_per_mwh_for_electricity")
st.line_chart(data= selectBoxChoice1,x="datetime_utc",y=indicators)


# Display mean emissions for same period as chart
mean20 = selectBoxChoice1.mean()
st.write("Mean data")
st.table(mean20)

# mean = selectboxChoice1[co2]
# find mean min max
# do this for all and display nicely

# Choose timeframe to be displayed
startDate = datetime.date(2021, 1, 1)
d = st.date_input(
    "Select the start date of timeframe to be displayed (must be in year 2021):",
    startDate)

startDate = d
startDate = str(startDate)
if (startDate == "2021-01-01"):
    start = startDate + " 08:00:00+00:00"
else:
    start = startDate + " 00:00:00+00:00"

endDate = datetime.date(2021, 12, 31)
d = st.date_input(
    "Select the end date of timeframe to be displayed (must be in year 2021):",
    endDate)
endDate = d
endDate = str(endDate)
end = endDate + " 23:00:00+00:00"

# Create new dataframe with user selected dates for Singularity data
mask = (selectBoxChoice2['datetime_utc'] >= start) & (selectBoxChoice2['datetime_utc'] <= end)
selectBoxChoice2 = selectBoxChoice2.loc[mask]

# Display 2021 ERCO Singularity line chart
st.write("Singularity 2021 Data Line Graph")
#st.line_chart(data= selectBoxChoice2,x="datetime_utc",y="consumed_co2_rate_lb_per_mwh_for_electricity")
st.line_chart(data= selectBoxChoice2,x="datetime_utc",y=indicators)


# Display mean emissions for same period as chart
mean21 = selectBoxChoice2.mean()
st.write("Mean data")
st.table(mean21)