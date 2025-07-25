import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("인구 피라미드 예제")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='cp949')

    # 예시 컬럼명 (파일에 맞게 수정 필요)
    age_groups = df["연령대"]  # 연령대
    male = df["남자"].str.replace(",", "").astype(int) * -1  # 남자는 음수로
    female = df["여자"].str.replace(",", "").astype(int)     # 여자는 양수로

    fig = go.Figure()
    fig.add_trace(go.Bar(y=age_groups, x=male, name='남자', orientation='h'))
    fig.add_trace(go.Bar(y=age_groups, x=female, name='여자', orientation='h'))

    fig.update_layout(
        barmode='overlay',
        bargap=0.1,
        xaxis=dict(title='인구수', tickvals=[-10000, 0, 10000],
                   ticktext=['10,000', '0', '10,000']),
        yaxis=dict(title='연령대'),
        title='인구 피라미드',
        template='plotly_white'
    )
    st.plotly_chart(fig)

else:
    st.info("CSV 파일을 업로드 해주세요.")
