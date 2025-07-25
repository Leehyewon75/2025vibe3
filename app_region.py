import streamlit as st
import pandas as pd

st.title("행정구역별 인구수 선그래프")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='cp949')

    # 쉼표 제거 후 숫자 변환
    df["2025년06월_계_총인구수"] = df["2025년06월_계_총인구수"].str.replace(",", "").astype(int)

    st.dataframe(df.head())

    chart_data = df.set_index("행정구역")["2025년06월_계_총인구수"]
    st.line_chart(chart_data)

else:
    st.info("CSV 파일을 업로드 해주세요.")
