import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.title("Plotly 인구 피라미드")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='euc-kr')
    
    st.write("컬럼명:", df.columns.tolist())
    st.write(df.head())

    # 컬럼명 예시 맞춤 수정 필요!
    # 아래는 예시이므로, 실제 컬럼명 확인 후 수정하세요.
    sex_col = '성별'  
    age_col = '연령별(5세계급)'
    pop_col = '계'
    
    # 남성 인구 음수 처리
    df.loc[df[sex_col] == '남자', pop_col] *= -1
    
    df = df.sort_values(age_col)
    
    male = df[df[sex_col] == '남자']
    female = df[df[sex_col] == '여자']
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=male[age_col],
        x=male[pop_col],
        name='남자',
        orientation='h',
        marker_color='skyblue'
    ))
    fig.add_trace(go.Bar(
        y=female[age_col],
        x=female[pop_col],
        name='여자',
        orientation='h',
        marker_color='pink'
    ))
    
    fig.update_layout(
        title='인구 피라미드',
        barmode='overlay',
        xaxis=dict(title='인구수'),
        yaxis=dict(title='연령'),
        bargap=0.1,
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
