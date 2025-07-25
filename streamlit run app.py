import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("행정구역별 남자/여자 인구수 비교 인구 피라미드")

uploaded_file1 = st.file_uploader("기본 인구정보 CSV 업로드", type=["csv"])
uploaded_file2 = st.file_uploader("성별 인구수 포함 CSV 업로드", type=["csv"])

if uploaded_file1 and uploaded_file2:
    # 인코딩은 데이터에 맞게 변경하세요
    df_basic = pd.read_csv(uploaded_file1, encoding='euc-kr')
    df_gender = pd.read_csv(uploaded_file2, encoding='euc-kr')
    
    # 남자/여자 인구 컬럼명 예시
    male_col = '2025년06월_남자 인구수'
    female_col = '2025년06월_여자 인구수'
    region_col = '행정구역'
    
    # 숫자 데이터 쉼표 제거 후 정수 변환
    df_gender[male_col] = df_gender[male_col].str.replace(',', '').astype(int)
    df_gender[female_col] = df_gender[female_col].str.replace(',', '').astype(int)
    
    # 남성 인구는 음수 처리 (왼쪽에 표시하기 위해)
    df_gender[male_col] = -df_gender[male_col]
    
    # 정렬(행정구역명 기준)
    df_gender = df_gender.sort_values(region_col)
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=df_gender[region_col],
        x=df_gender[male_col],
        name='남자 인구수',
        orientation='h',
        marker_color='blue'
    ))
    
    fig.add_trace(go.Bar(
        y=df_gender[region_col],
        x=df_gender[female_col],
        name='여자 인구수',
        orientation='h',
        marker_color='pink'
    ))
    
    fig.update_layout(
        title='행정구역별 남자/여자 인구수 비교',
        barmode='overlay',
        xaxis=dict(title='인구수', tickvals=[-5000000, -2500000, 0, 2500000, 5000000],
                   ticktext=['5M', '2.5M', '0', '2.5M', '5M']),
        yaxis=dict(title='행정구역'),
        template='plotly_white',
        xaxis_range=[-6000000, 6000000]
    )
    
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("두 개 CSV 파일 모두 업로드 해주세요.")
