import streamlit as st
import pandas as pd

st.title("간단 인구 피라미드 스타일 차트 (설치 없이)")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='cp949')

    # 컬럼명은 파일에 맞게 변경하세요
    age_col = "연령대"
    male_col = "남자"
    female_col = "여자"

    df[male_col] = df[male_col].str.replace(",", "").astype(int)
    df[female_col] = df[female_col].str.replace(",", "").astype(int)

    # 두 개 차트를 나란히 표시
    st.write("남자 인구수")
    st.bar_chart(df.set_index(age_col)[male_col])

    st.write("여자 인구수")
    st.bar_chart(df.set_index(age_col)[female_col])

else:
    st.info("CSV 파일을 업로드 해주세요.")
