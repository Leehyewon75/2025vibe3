import streamlit as st
import pandas as pd

st.title("CSV 파일 업로드 및 인코딩 문제 처리")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, encoding='cp949')  # 또는 'euc-kr'
        st.write("데이터 미리보기")
        st.dataframe(df.head())
    except UnicodeDecodeError:
        st.error("파일 인코딩 문제 발생! 다른 인코딩(euc-kr, utf-8 등)을 시도하세요.")
else:
    st.info("CSV 파일을 업로드 해주세요.")
