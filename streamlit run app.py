import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("두 개 CSV 파일로 인구 피라미드 그리기")

uploaded_male = st.file_uploader("남성 인구 CSV 파일 업로드", type=["csv"])
uploaded_female = st.file_uploader("여성 인구 CSV 파일 업로드", type=["csv"])

if uploaded_male and uploaded_female:
    # 인코딩은 데이터에 맞게 변경하세요
    df_male = pd.read_csv(uploaded_male, encoding='euc-kr')
    df_female = pd.read_csv(uploaded_female, encoding='euc-kr')

    # 컬럼명은 업로드 파일에 맞게 수정하세요
    # 예: 'Age' 컬럼, 'Population' 컬럼이 있다고 가정
    # 아래는 예시로 컬럼명 변경 코드 넣음
    df_male = df_male.rename(columns={'연령별(5세계급)': 'Age', '인구수': 'Population'})
    df_female = df_female.rename(columns={'연령별(5세계급)': 'Age', '인구수': 'Population'})

    # 남성 인구는 음수 처리
    df_male['Population'] = -df_male['Population']

    # 나이순 정렬 (같은 기준으로)
    df_male = df_male.sort_values('Age')
    df_female = df_female.sort_values('Age')

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=df_male['Age'],
        x=df_male['Population'],
        name='남성',
        orientation='h',
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        y=df_female['Age'],
        x=df_female['Population'],
        name='여성',
        orientation='h',
        marker_color='red'
    ))

    fig.update_layout(
        title='인구 피라미드 (남녀 인구 비교)',
        barmode='overlay',
        xaxis=dict(title='인구수', tickvals=[-500000, -250000, 0, 250000, 500000],
                   ticktext=['500k', '250k', '0', '250k', '500k']),
        yaxis=dict(title='연령'),
        template='plotly_white'
    )

    st.plotly_chart(fig, use_container_width=True)
