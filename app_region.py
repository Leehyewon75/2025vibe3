import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("인구 피라미드 시각화")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.loc[df['성별'] == '남', '인구수'] = -df.loc[df['성별'] == '남', '인구수']
    df = df.sort_values('나이')
    pivot_df = df.pivot(index='나이', columns='성별', values='인구수')
    
    fig, ax = plt.subplots(figsize=(10,8))
    pivot_df.plot(kind='barh', stacked=False, color=['skyblue', 'pink'], ax=ax)
    ax.set_title('인구 피라미드')
    ax.set_xlabel('인구수')
    ax.set_ylabel('나이')
    ax.grid(True)
    st.pyplot(fig)
