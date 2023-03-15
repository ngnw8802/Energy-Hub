import streamlit as st
from components.singularity_table import *
from components.watttime_table import *
from components.histogram import *
from PIL import Image

image = Image.open('./header.png')
st.image(image)
st.header("App Description.....")

col1, col2, col3 = st.columns([1,1,1])

single_page = st.empty()

with single_page.container():
  st.subheader("Set Location:")
  option = st.selectbox(
    'Set Location: ',
    ('Alabama', 'Colorado', 'Oregon'), label_visibility="hidden")
  submit = st.button("Submit Location")


if (submit):
  location = option
  single_page.empty()
  st.pyplot(fig_histogram)
  with col1:
    tech = st.selectbox(
    'Technology: ',
    ('Tesla', 'Dryer', 'Washer'))
  with col2:
    charge = st.selectbox(
    'Charging type: ',
    ('1', '2', '3'))
  with col3:
    interval = st.selectbox(
    'Charging time: ',
    ('1 hr', '2 hrs', '3+ hrs'))
  st.write("Here is where we would put the summary of the calculations")


# def home():
#     st.write("Home")

# def choice_one():
#     st.write("Optimizing clean energy")

# def choice_two():
#     st.write("choice 2")

# def choice_three():
#     st.write("choice 3")

# with col1:
#   homeb = st.button("Home")

# with col2:
#   choice_oneb = st.button("1")

# with col3:
#   choice_twob = st.button("2")

# with col4:
#   choice_threeb = st.button("3")

# if (homeb):
#   home()

# if (choice_oneb):
#   choice_one()

# if (choice_twob):
#   choice_two()
  
# if (choice_threeb):
#   choice_three()














# st.subheader(singsub)
# st.write(SingBANCData)

# st.subheader(wattsub)
# st.write(WattTimeDf)

# Histogram is possible but not contained in the streamlit API so it doesn't look as good
# Requires st.pyplot which just displays a matplotlib.pyplot
# Code for histogram is in histogram.py component

# st.write("Singularity Data Area Chart")
# st.area_chart(data=SingBANCData, x="datetime_utc", y="consumed_co2_rate_lb_per_mwh_for_electricity")

# st.write("WattTime Data Area Chart")
# st.area_chart(data=WattTimeDf, x="timestamp", y="MOER")

# st.write("Singularity Data Line Graph")
# st.line_chart(data= SingBANCData,x="datetime_utc",y="consumed_co2_rate_lb_per_mwh_for_electricity")

# st.write("WattTime Data Line Graph")
# st.line_chart(data= WattTimeDf,x="timestamp",y="MOER")




# print("Mean of CO2 rate lb per mwh for electricity in BANC is(from singulairty) for 2020: ")
# print(SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'].mean())

# print("Variance of CO2 rate lb per mwh for electricity in BANC is(from singulairty) for 2020: ")
# print(SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'].var()) 

# token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6ImJhc2ljLGRhdGE9QVpQUzpTUlA6UEpNX0RDOkVSQ09UX0FVU1RJTjpTUFBfS0M6Q2FsaWZvcm5pYV9hbGwsbWFwcyIsImlhdCI6MTY2NzQwMzgyNywiZXhwIjoxNjY3NDA1NjI3LCJpc3MiOiJXYXR0VGltZSIsInN1YiI6Imp1c3Rpbl9lbmVyZ3lodWIifQ.f-XXRaa0Vw8jLMJRFP7g4fJH59St3uxkCNwAKcgNXIjuOMC9pWwYbuA7YeCpUciKDBCfcVkiwep9yDk4ryidnpL_JoadVFaiOXbdoBSzk5Cx9k2wykKbfNet4cv7DbNk-PnFtJ9sTY5BA43h2DSLQP0fd5MeofPnGRvPDwOD2fK5HQIQtYbyPqS-sIRrztCRpb2JzQIqiGbVsl_TcnfzszaszsNHBMq-sBl52CzYgXQrUjhI7cJ2KtjTB6NWowec9poBEd4o7Y6rVbeD5VfigturGTjJCI2Y2puz2YP2EH1cGW3xjHF5oSxZwTx8m94MoV-Ep9B9wAf4u8AASbOPkg"

# print('Mean of MOER in BANC from Wattime for 2020 is: ')
# print(WattTimeDf['MOER'].mean())

# print('Var of MOER in BANC from Wattime for 2020 is: ')
# print(WattTimeDf['MOER'].var())