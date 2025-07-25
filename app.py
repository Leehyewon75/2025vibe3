import streamlit as st
import pandas as pd

# 세션 상태 초기화
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

st.title("🗺️나만의 북마크 지도")

# 사이드바: 장소 추가
st.sidebar.header("➕장소 추가")
with st.sidebar.form("add_bookmark"):
    name = st.text_input("장소 이름")
    lat = st.number_input("위도 (예: 37.5665)", format="%.6f")
    lon = st.number_input("경도 (예: 126.9780)", format="%.6f")
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

# 북마크 데이터 준비
if st.session_state.bookmarks:
    df = pd.DataFrame(st.session_state.bookmarks)
else:
    # 기본 좌표(서울 시청) 한 개 넣기
    df = pd.DataFrame([{"name": "서울 시청 (기본)", "lat": 37.5665, "lon": 126.9780}])

# 지도 출력
st.map(df.rename(columns={"lat": "latitude", "lon": "longitude"}))

# 북마크 목록
st.subheader("📌북마크 목록")
if st.session_state.bookmarks:
    for b in st.session_state.bookmarks:
        st.markdown(f"- **{b['name']}**: ({b['lat']}, {b['lon']})")
else:
    st.info("북마크가 없습니다. 장소를 추가해보세요!")
