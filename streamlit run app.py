import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.title("Plotly 인구 피라미드")

# 업로드 파일 받기
uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='euc-kr')  # 인코딩은 필요하면 조정
    
    # 데이터 컬럼 확인
    st.write("데이터 미리보기", df.head())
    
    # 컬럼명에 맞게 수정 필요 (예시)
    # '연령' 또는 '나이', '성별', '인구수'가 있다고 가정
    # 컬럼명이 다르면 아래 부분을 맞게 바꿔주세요
    df = df.rename(columns={
        '연령별(5세계급)': 'Age',
        '성별': 'Sex',
        '인구수': 'Population'
    })
    
    # 남성 인구는 음수 처리
    df.loc[df['Sex'] == '남자', 'Population'] *= -1
    
    # 나이순 정렬
    df = df.sort_values('Age')
    
    male = df[df['Sex'] == '남자']
    female = df[df['Sex'] == '여자']
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=male['Age'],
        x=male['Population'],
        name='남자',
        orientation='h',
        marker_color='skyblue'
    ))
    
    fig.add_trace(go.Bar(
        y=female['Age'],
        x=female['Population'],
        name='여자',
        orientation='h',
        marker_color='pink'
    ))
    
    fig.update_layout(
        title='인구 피라미드',
        barmode='overlay',
        xaxis=dict(title='인구수', tickvals=[-500000, -250000, 0, 250000, 500000],
                   ticktext=['500k', '250k', '0', '250k', '500k']),
        yaxis=dict(title='연령'),
        bargap=0.1,
        plot_bgcolor='white',
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
