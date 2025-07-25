import streamlit as st
import pandas as pd

st.title("연령별 인구현황 (합계) 시각화")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())

    if "연령" in df.columns and "인구수" in df.columns:
        chart_data = df.set_index("연령")["인구수"]
        st.line_chart(chart_data)
    else:
        st.error("'연령' 또는 '인구수' 컬럼이 없습니다.")
else:
    st.info("CSV 파일을 업로드해주세요.")
