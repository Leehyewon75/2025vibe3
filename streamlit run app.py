import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("두 개 CSV 파일 업로드 후 함께 그래프 그리기")

uploaded_file1 = st.file_uploader("첫 번째 CSV 파일 업로드", type=["csv"])
uploaded_file2 = st.file_uploader("두 번째 CSV 파일 업로드", type=["csv"])

if uploaded_file1 and uploaded_file2:
    # 파일 읽기 (인코딩은 필요시 바꾸기)
    df1 = pd.read_csv(uploaded_file1, encoding='euc-kr')
    df2 = pd.read_csv(uploaded_file2, encoding='euc-kr')
    
    # 컬럼명 확인 및 필요시 rename (예시)
    # 실제 컬럼명에 맞게 바꿔주세요
    df1 = df1.rename(columns={'연령별(5세계급)': 'Age', '인구수': 'Population'})
    df2 = df2.rename(columns={'연령별(5세계급)': 'Age', '인구수': 'Population'})
    
    # 남성 데이터는 음수 처리 (예: df1이 남성)
    df1['Population'] = -df1['Population']
    
    # 나이순 정렬
    df1 = df1.sort_values('Age')
    df2 = df2.sort_values('Age')
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=df1['Age'],
        x=df1['Population'],
        name='파일1 (남성 등)',
        orientation='h',
        marker_color='blue'
    ))
    
    fig.add_trace(go.Bar(
        y=df2['Age'],
        x=df2['Population'],
        name='파일2 (여성 등)',
        orientation='h',
        marker_color='red'
    ))
    
    fig.update_layout(
        title='두 개 CSV 파일 데이터 비교 그래프',
        barmode='overlay',
        xaxis=dict(title='인구수'),
        yaxis=dict(title='연령'),
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("두 개의 CSV 파일을 모두 업로드 해주세요.")
