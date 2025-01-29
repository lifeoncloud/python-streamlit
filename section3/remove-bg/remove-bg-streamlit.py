import streamlit as st
from rembg import remove
from PIL import Image

# install rembg(https://github.com/danielgatis/rembg)
# pip3 install "rembg[cpu,cli]"

def remove_background(input_image):
    output_image = remove(input_image)
    return output_image

# Streamlit 앱 
st.title("이미지 배경 제거")

# 이미지 업로드
uploaded_image = st.file_uploader("이미지를 업로드하세요.", type=["png", "jpg"])

if uploaded_image is not None:
    # 업로드한 이미지를 PIL Image인 input_image로 변환하기
    input_image = Image.open(uploaded_image)
