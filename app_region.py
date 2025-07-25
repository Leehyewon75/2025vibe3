import streamlit as st
import pandas as pd

st.title("인구 피라미드 스타일 차트 (설치 없이)")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    # 데이터 읽기
    df = pd.read_csv(uploaded_file, encoding='cp949')

    # 컬럼명 출력해서 확인
    st.write("컬럼명 리스트:", df.columns.tolist())

    # 아래 컬럼명은 실제 업로드한 CSV의 컬럼명에 맞게 변경해주세요
    age_col = "연령별"  # 예: 연령대, 연령별 등
    male_col = "2025년06월_남_총인구수"
    female_col = "2025년06월_여_총인구수"

    # 컬럼명 유효성 체크
    if male_col in df.columns and female_col in df.columns and age_col in df.columns:
        # 쉼표 제거 후 숫자 변환
        df[male_col] = df[male_col].str.replace(",", "").astype(int)
        df[female_col] = df[female_col].str.replace(",", "").astype(int)

        # 남자 인구는 음수 처리해서 좌측으로 표현하기 위한 복사본 생성
        df['남자_음수'] = -df[male_col]

        st.subheader("남자 인구수")
        st.bar_chart(df.set_index(age_col)['남자_음수'])

        st.subheader("여자 인구수")
        st.bar_chart(df.set_index(age_col)[female_col])

    else:
        st.error("필요한 컬럼명이 데이터에 없습니다. 컬럼명 리스트를 확인해주세요.")
else:
    st.info("CSV 파일을 업로드 해주세요.")
