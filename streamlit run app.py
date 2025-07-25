import streamlit as st
import pandas as pd
import plotly.express as px

st.title("CSV 컬럼명 확인 + 행정구역별 총인구수 그래프")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    # 인코딩 문제 있으면 euc-kr, 안 맞으면 utf-8로 바꿔서 시도 가능
    try:
        df = pd.read_csv(uploaded_file, encoding='euc-kr')
    except:
        df = pd.read_csv(uploaded_file, encoding='utf-8')

    # 컬럼명 출력
    st.write("컬럼명 리스트:")
    st.write(df.columns.tolist())

    # 데이터 샘플 출력
    st.write("데이터 샘플:")
    st.write(df.head())

    # 컬럼명에 맞게 숫자 데이터 정리 (아래는 예시, 상황에 맞게 수정하세요)
    # 쉼표 제거 후 int 변환
    pop_col = '2025년06월_총인구수'  # 예시: 총인구수 컬럼명
    if pop_col in df.columns:
        df[pop_col] = df[pop_col].str.replace(',', '').astype(int)

        # 그래프 그리기
        fig = px.bar(df, x='행정구역', y=pop_col, 
                     title='행정구역별 총인구수',
                     labels={pop_col: '총인구수', '행정구역': '행정구역'},
                     template='plotly_white')
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning(f"'{pop_col}' 컬럼을 데이터에서 찾을 수 없습니다. 컬럼명을 확인하세요.")
