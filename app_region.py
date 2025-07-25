import streamlit as st
import pandas as pd
import altair as alt

# 데이터 불러오기 (예시)
df = pd.read_csv("population_data.csv")

# 1. 시도별 인구수 막대 차트
st.header("시도별 총 인구수")
pop_by_region = df.groupby("region")["total_population"].sum().reset_index()

bar_chart = alt.Chart(pop_by_region).mark_bar().encode(
    x=alt.X('region', sort='-y'),
    y='total_population',
    tooltip=['region', 'total_population']
).properties(width=700)

st.altair_chart(bar_chart)

# 2. 성별 인구 비율 파이 차트
st.header("성별 인구 비율")
gender_pop = df[["male_population", "female_population"]].sum().reset_index()
gender_pop.columns = ["gender", "count"]
gender_pop["gender"] = gender_pop["gender"].map({"male_population": "남성", "female_population": "여성"})

pie_chart = alt.Chart(gender_pop).mark_arc().encode(
    theta='count',
    color='gender',
    tooltip=['gender', 'count']
)

st.altair_chart(pie_chart)
