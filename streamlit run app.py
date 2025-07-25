import streamlit as st
import pandas as pd
import plotly.express as px

st.title("행정구역별 총인구수 시각화")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
if uploaded_file:
    # 인코딩 문제 있으면 바꿔보세요
    df = pd.read_csv(uploaded_file, encoding='euc-kr')
    
    # 숫자 데이터는 쉼표 제거하고 정수로 변환
    df['2025년06월_총인구수'] = df['2025년06월_총인구수'].str.replace(',', '').astype(int)
    
    fig = px.bar(df, 
                 x='행정구역', 
                 y='2025년06월_총인구수', 
                 title='행정구역별 총인구수',
                 labels={'2025년06월_총인구수': '총인구수', '행정구역': '행정구역'},
                 template='plotly_white')
    
    fig.update_layout(xaxis_tickangle=-45)
    
    st.plotly_chart(fig, use_container_width=True)
