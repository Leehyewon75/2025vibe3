import streamlit as st
import pandas as pd

st.title("CSV 컬럼명과 데이터 샘플 확인")

uploaded_file1 = st.file_uploader("첫 번째 CSV 파일 업로드", type=["csv"])
uploaded_file2 = st.file_uploader("두 번째 CSV 파일 업로드", type=["csv"])

if uploaded_file1:
    df1 = pd.read_csv(uploaded_file1, encoding='euc-kr')
    st.write("첫 번째 CSV 컬럼명:", df1.columns.tolist())
    st.write(df1.head())

if uploaded_file2:
    df2 = pd.read_csv(uploaded_file2, encoding='euc-kr')
    st.write("두 번째 CSV 컬럼명:", df2.columns.tolist())
    st.write(df2.head())
