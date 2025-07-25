import streamlit as st
import pandas as pd
import plotly.express as px

st.title("연령별 인구현황 (합계) 시각화")

# CSV 파일 업로드 받기
uploaded_file = st.file_uploader("CSV 파일을 업로드 해주세요", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='utf-8')  # 필요시 encoding 조정

    st.write("데이터 미리보기")
    st.dataframe(df.head())

    # 예시: '연령' 컬럼과 '인구수' 컬럼이 있다고 가정
    # 컬럼명은 실제 파일에 맞게 변경 필요
    if "연령" in df.columns and "인구수" in df.columns:
        fig = px.line(df, x="연령", y="인구수", title="연령별 인구수")
        st.plotly_chart(fig)
    else:
        st.error("데이터에 '연령' 또는 '인구수' 컬럼이 없습니다.")
else:
    st.info("CSV 파일을 업로드 해주세요.")
