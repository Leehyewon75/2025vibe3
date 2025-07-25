import streamlit as st
import pandas as pd

# 초기화
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = [{"name": "서울", "lat": 37.5665, "lon": 126.978}]

st.title("📍 나만의 북마크 지도")

# 지도 표시
df = pd.DataFrame(st.session_state.bookmarks)
st.map(df.rename(columns={"lat": "latitude", "lon": "longitude"}))

st.subheader("📌 북마크 목록")

def delete_bookmark(idx):
    del st.session_state.bookmarks[idx]

for i, b in enumerate(st.session_state.bookmarks):
    col1, col2 = st.columns([8, 1])
    with col1:
        st.markdown(f"- **{b['name']}**: ({b['lat']}, {b['lon']})")
    with col2:
        if st.button("삭제", key=f"delete_{i}"):
            delete_bookmark(i)
            st.experimental_rerun()
