import streamlit as st
import pandas as pd

# 세션 상태 초기화
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

st.title("🗺️나만의 북마크 지도")

# 사이드바: 북마크 추가 폼
st.sidebar.header("➕장소 추가")
with st.sidebar.form("add_bookmark"):
    name = st.text_input("장소 이름")
    lat = st.number_input("위도 (예: 37.5665)", format="%.6f", value=37.5665)
    lon = st.number_input("경도 (예: 126.9780)", format="%.6f", value=126.9780)
    submitted = st.form_submit_button("추가하기")
    if submitted:
        if name:
            st.session_state.bookmarks.append({
                "name": name,
                "lat": lat,
                "lon": lon
            })
            st.success(f"'{name}'이(가) 추가되었습니다!")
        else:
            st.error("장소 이름을 입력해주세요!")

# 지도에 표시할 데이터 준비
if st.session_state.bookmarks:
    df = pd.DataFrame(st.session_state.bookmarks)
else:
    # 기본 서울 시청 위치 + 광주광역시 교육청 위치 두 개 표시
    df = pd.DataFrame([
        {"name": "서울 시청 (기본)", "lat": 37.5665, "lon": 126.9780},
        {"name": "광주광역시 교육청 (기본)", "lat": 35.1595, "lon": 126.8519}
    ])

# 지도 표시
st.map(df.rename(columns={"lat": "latitude", "lon": "longitude"}))

# 북마크 목록과 삭제 버튼
st.subheader("📌북마크 목록")
if st.session_state.bookmarks:
    for i, b in enumerate(st.session_state.bookmarks):
        col1, col2 = st.columns([8, 1])
        with col1:
            st.markdown(f"- **{b['name']}**: ({b['lat']}, {b['lon']})")
        with col2:
            if st.button("삭제", key=f"delete_{i}"):
                del st.session_state.bookmarks[i]
                st.experimental_rerun()
else:
    st.info("아직 북마크가 없습니다. 사이드바에서 추가해보세요!")
