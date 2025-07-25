import streamlit as st
import folium
from streamlit_folium import st_folium

# 초기화
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

st.title("📍 나만의 북마크 지도")

st.sidebar.header("➕ 장소 추가")

# 입력 폼
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

# 지도 중심 설정
if st.session_state.bookmarks:
    first = st.session_state.bookmarks[0]
    m = folium.Map(location=[first["lat"], first["lon"]], zoom_start=12)
else:
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)  # 기본 서울

# 마커 표시
for b in st.session_state.bookmarks:
    folium.Marker(
        location=[b["lat"], b["lon"]],
        popup=b["name"],
        icon=folium.Icon(color="blue", icon="bookmark")
    ).add_to(m)

# 지도 출력
st_data = st_folium(m, width=700, height=500)

# 북마크 목록 출력
st.subheader("📌 북마크 목록")
if st.session_state.bookmarks:
    for b in st.session_state.bookmarks:
        st.markdown(f"- **{b['name']}**: ({b['lat']}, {b['lon']})")
else:
    st.info("아직 북마크가 없습니다.")

