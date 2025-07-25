import streamlit as st
import pandas as pd
import plotly.express as px

st.title("행정구역별 남자 총인구수 시각화")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='cp949')  # 인코딩 맞게 조정

    st.write("데이터 미리보기")
    st.dataframe(df.head())

    # 필요한 컬럼명에 맞게 조정하세요
    if "행정구역" in df.columns and "2025년06월_남_총인구수" in df.columns:
        fig = px.bar(
            df,
            x="행정구역",
            y="2025년06월_남_총인구수",
            title="행정구역별 남자 총인구수",
            labels={"행정구역": "행정구역", "2025년06월_남_총인구수": "남자 총인구수"},
            height=600
        )
        fig.update_layout(xaxis_tickangle=45)
        st.plotly_chart(fig)
    else:
        st.error("필요한 컬럼명이 데이터에 없습니다.")
else:
    st.info("CSV 파일을 업로드 해주세요.")
