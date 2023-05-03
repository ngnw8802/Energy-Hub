import streamlit as st
from components.singularity_table import *
from components.watttime_table import *
from components.histogram import *
from PIL import Image

def calculate(tech, charge):
    timeCharge = tech/charge
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

    meanList = []

    for data in range(len(chunks)-1):
        meanList.append(SingBANCData.loc[(SingBANCData['datetime_local']>chunks[data]) & (SingBANCData['datetime_local']<=chunks[data+1])]['consumed_co2_rate_lb_per_mwh_for_electricity'].mean())

    bestMean = min(meanList)
    bestIdx = meanList.index(bestMean)
    chunkIdx = 0

    result = tuple()

    for i in range(len(meanList)):
        if bestIdx==i:
            result = (chunks[i], chunks[i+1])
        else:
            continue
    
    return result

image = Image.open('./header.png')
st.image(image)
st.header("App Description.....")




st.subheader("Set Location:")
option = st.selectbox(
  'Set Location: ',
  ('Alabama', 'Colorado', 'Oregon'), label_visibility="hidden")
submit = st.button("Submit Location")
col1, col2, col3 = st.columns([1,1,1])
location = option
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

  (r1, r2) = calculate(60, 6)

st.write("Best to charge from", r1, "to", r2, ".")


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

# #violin plot for singularity data
# st.write("Violin plot for first 3 months of 2020 (singularity data)")
# t1 = "2020-02-01 00:00:00-08:00"
# t2 = "2020-03-01 00:00:00-08:00"
# jan = SingBANCData.loc[SingBANCData['datetime_local']<t1]['consumed_co2_rate_lb_per_mwh_for_electricity']
# feb = SingBANCData.loc[SingBANCData['datetime_local']<t2]['consumed_co2_rate_lb_per_mwh_for_electricity']
# mar = SingBANCData.loc[SingBANCData['datetime_local']>=t2]['consumed_co2_rate_lb_per_mwh_for_electricity']

# toplot = list([jan,feb,mar])

# violin, ax = plt.subplots()

# xticklabels = ['Jan 2020', 'Feb 2020','Mar 2020']
# ax.set_xticks([1, 2,3])
# ax.set_xticklabels(xticklabels)
# #axes.violinplot(df1['MOER'])
# ax.violinplot(toplot)
# st.pyplot(violin)

# #Singularity Variance/Distribution
# singmu, singvar = norm.fit(SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'])

# variances, s1 = plt.subplots()
# xmin, xmax = SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'].min(), SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'].max()
# xs = np.linspace(xmin, xmax, 100)
# ps = norm.pdf(xs, singmu, singvar)
# s1.hist(SingBANCData['consumed_co2_rate_lb_per_mwh_for_electricity'], bins=25, density=True, alpha=0.6, color='b')
# s1.plot(xs, ps, 'k', linewidth=2)

# s1.set_title("Variance in Singularity Data")
# s1.set_xlabel("Consumed CO2 Rate for Electricity (lb/mwh)")
# s1.set_ylabel("Distribution")

# st.pyplot(variances)

# #Wattime Variance/Distribution
# wattmu, wattvar = norm.fit(WattTimeDf['MOER'])
# variancew, s2 = plt.subplots()
# xmin, xmax = WattTimeDf['MOER'].min(), WattTimeDf['MOER'].max()
# xw = np.linspace(xmin, xmax, 100)
# pw = norm.pdf(xw, wattmu, wattvar)
# s2.hist(WattTimeDf['MOER'], bins=25, density=True, alpha=0.6, color='r')
# s2.plot(xw, pw, 'k', linewidth=2)

# s2.set_title("Variance in Wattime Data")
# s2.set_xlabel("MOER")
# s2.set_ylabel("Distribution")

# st.pyplot(variancew)
