import streamlit as st
from PIL import Image

# 페이지 기본 설정
st.set_page_config(page_title="부산시네마 영화요금 안내기 순서도", layout="wide")

st.markdown("<h1 style='text-align: center;'>부산시네마 영화요금 안내기 순서도</h1>", unsafe_allow_html=True)
# 이미지 로드 및 출력
try:
    image = Image.open("미션-순서도.png")
    st.image(image)
except FileNotFoundError:
    st.error("이미지 파일을 찾을 수 없습니다.")
    
    
# , use_container_width=True