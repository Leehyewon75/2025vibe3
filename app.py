import streamlit as st
import pandas as pd

# 초기화
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = [
        {"name": "서울", "lat": 37.5665, "lon": 126.978},
        {"name": "부산", "lat": 35.1796, "lon": 129.0756},
        {"name": "대구", "lat": 35.8722, "lon": 128.6025},
        {"name": "울산", "lat": 35.5384, "lon": 129.3114},
        {"name": "제주", "lat": 33.4996, "lon": 126.5312},
        {"name": "인천", "lat": 37.4563, "lon": 126.7052},
        {"name": "광주", "lat": 35.1595, "lon": 126.8526},
        {"name": "대전", "lat": 36.3504, "lon": 127.3845},
        {"name": "우리집", "lat": 35.2079246, "lon": 126.8701459},
        {"name": "도쿄", "lat": 35.6895, "lon": 139.6917},
        {"name": "베이징", "lat": 39.9042, "lon": 116.4074},
    ]

st.title("📍 나만의 북마크 지도")

# 지도 출력
if st.session_state.bookmarks:
    df = pd.DataFrame(st.session_state.bookmarks)
    st.map(df.rename(columns={"lat": "latitude", "lon": "longitude"}))
else:
    st.info("북마크가 없습니다. 장소를 추가해보세요!")

st.subheader("📌 북마크 목록")

# 삭제를 위한 인덱스 추적용 함수
def delete_bookmark(idx):
    del st.session_state.bookmarks[idx]

# 각 북마크별로 삭제 버튼 만들기
for i, b in enumerate(st.session_state.bookmarks):
    col1, col2 = st.columns([8, 1])
    with col1:
        st.markdown(f"- **{b['name']}**: ({b['lat']}, {b['lon']})")
    with col2:
        if st.button("삭제", key=f"delete_{i}"):
            delete_bookmark(i)
            st.experimental_rerun()
