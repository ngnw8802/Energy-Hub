import streamlit as st
from components.singularity_banc_2020 import *
from components.watttime_banc_2020 import *
from components.histogram import *
from components.variance import *

st.subheader(singsub)
st.write(SingBANCData)

st.subheader(wattsub)
st.write(WattTimeDf)

st.subheader(CISO_histogram_tile)
st.pyplot(fig_histogram)

st.write("Singularity Data Line Graph")
st.line_chart(data= SingBANCData,x="datetime_utc",y="consumed_co2_rate_lb_per_mwh_for_electricity")

#st.write("WattTime Data Line Graph")
#st.line_chart(data= WattTimeDf,x="timestamp",y="MOER")

st.write("Singularity Variance")
st.pyplot(fig_variance)



# print("Mean of CO2 rate lb per mwh for electricity in BANC is(from singulairty) for 2020: ")
# print(SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'].mean())

# print("Variance of CO2 rate lb per mwh for electricity in BANC is(from singulairty) for 2020: ")
# print(SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'].var()) 

# token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6ImJhc2ljLGRhdGE9QVpQUzpTUlA6UEpNX0RDOkVSQ09UX0FVU1RJTjpTUFBfS0M6Q2FsaWZvcm5pYV9hbGwsbWFwcyIsImlhdCI6MTY2NzQwMzgyNywiZXhwIjoxNjY3NDA1NjI3LCJpc3MiOiJXYXR0VGltZSIsInN1YiI6Imp1c3Rpbl9lbmVyZ3lodWIifQ.f-XXRaa0Vw8jLMJRFP7g4fJH59St3uxkCNwAKcgNXIjuOMC9pWwYbuA7YeCpUciKDBCfcVkiwep9yDk4ryidnpL_JoadVFaiOXbdoBSzk5Cx9k2wykKbfNet4cv7DbNk-PnFtJ9sTY5BA43h2DSLQP0fd5MeofPnGRvPDwOD2fK5HQIQtYbyPqS-sIRrztCRpb2JzQIqiGbVsl_TcnfzszaszsNHBMq-sBl52CzYgXQrUjhI7cJ2KtjTB6NWowec9poBEd4o7Y6rVbeD5VfigturGTjJCI2Y2puz2YP2EH1cGW3xjHF5oSxZwTx8m94MoV-Ep9B9wAf4u8AASbOPkg"

# print('Mean of MOER in BANC from Wattime for 2020 is: ')
# print(WattTimeDf['MOER'].mean())

# print('Var of MOER in BANC from Wattime for 2020 is: ')
# print(WattTimeDf['MOER'].var())