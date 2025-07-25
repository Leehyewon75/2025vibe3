import streamlit as st
import pandas as pd

# 세션 상태 초기화
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

st.title("🗺️나만의 북마크 지도")

st.sidebar.header("➕ 장소 추가")

# 장소 입력 폼
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

# 북마크가 있을 경우 지도 출력
if st.session_state.bookmarks:
    df = pd.DataFrame(st.session_state.bookmarks)
    st.map(df.rename(columns={"lat": "latitude", "lon": "longitude"}))
else:
    st.info("북마크가 없습니다. 장소를 추가해보세요!")

# 북마크 목록 출력
st.subheader("📌 북마크 목록")
if st.session_state.bookmarks:
    for b in st.session_state.bookmarks:
        st.markdown(f"- **{b['name']}**: ({b['lat']}, {b['lon']})")
