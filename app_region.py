import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("행정구역별 인구수 선그래프 (Matplotlib)")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='cp949')

    # 쉼표 제거 후 숫자 변환
    df["2025년06월_계_총인구수"] = df["2025년06월_계_총인구수"].str.replace(",", "").astype(int)

    st.dataframe(df.head())

    plt.figure(figsize=(12,6))
    plt.plot(df["행정구역"], df["2025년06월_계_총인구수"], marker='o', linestyle='-')
    plt.xticks(rotation=90)
    plt.ylabel("총인구수")
    plt.title("행정구역별 총인구수 선그래프")
    plt.tight_layout()

    st.pyplot(plt)

else:
    st.info("CSV 파일을 업로드 해주세요.")
