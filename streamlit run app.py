import streamlit as st
import pandas as pd

st.title("CSV 컬럼명과 데이터 확인")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
if uploaded_file:
    # 파일 인코딩이 euc-kr일 가능성이 높으니 기본은 euc-kr로, 안 맞으면 utf-8로 바꿔서 시도해보세요.
    try:
        df = pd.read_csv(uploaded_file, encoding='euc-kr')
    except:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    
    st.write("컬럼명 리스트:")
    st.write(df.columns.tolist())  # 컬럼명 리스트 출력
    
    st.write("데이터 샘플:")
    st.write(df.head())
