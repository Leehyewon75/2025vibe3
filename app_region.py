import streamlit as st
import pandas as pd

st.title("CSV 업로드 및 인구수 시각화")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='cp949')
    st.write("컬럼명:", df.columns.tolist())

    # 컬럼명 직접 지정 (컬럼명 리스트 확인 후 수정)
    col_name = "2025년06월_계_총인구수"  # 예시, 실제 컬럼명에 맞게 변경

    if col_name in df.columns:
        # 쉼표 제거 후 숫자 변환
        df[col_name] = df[col_name].str.replace(",", "").astype(int)
        st.dataframe(df.head())

        st.bar_chart(df.set_index("행정구역")[col_name])
    else:
        st.error(f"컬럼 '{col_name}' 이(가) 데이터에 없습니다.")
else:
    st.info("CSV 파일을 업로드 해주세요.")
