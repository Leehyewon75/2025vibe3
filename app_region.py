import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='cp949')
    st.dataframe(df.head())

    if "행정구역" in df.columns and "2025년06월_계_총인구수" in df.columns:
        chart_data = df.set_index("행정구역")["2025년06월_계_총인구수"]
        st.bar_chart(chart_data)
    else:
        st.error("필요한 컬럼명이 데이터에 없습니다.")
else:
    st.info("CSV 파일을 업로드 해주세요.")
