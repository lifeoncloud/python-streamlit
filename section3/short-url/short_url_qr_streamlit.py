import pyshorteners
import streamlit as st
import qrcode
from PIL import Image
import io

# pip install qrcode
# pip install Image

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    return short_url

def generate_qrcode(url):
    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.make()
    qr_img = qr.make_image()

    # Convert PIL Image to bytes. 임시로 저장하게 되는 방식.
    img_byte_array = io.BytesIO()
    qr_img.save(img_byte_array, format="PNG")
    img_bytes = img_byte_array.getvalue()

    return img_bytes

def main():
    st.title("URL 단축 및 QR 코드 생성 사이트")
    st.write("URL 주소를 입력하시면, 단축 URL과 해당 URL의 QR 코드가 생성됩니다.")

    url = st.text_input("URL 입력")

    if st.button("QR코드 생성하기"):
        if url is not None:
            short_url = shorten_url(url)
            qr_img_bytes = generate_qrcode(short_url)

            st.success("URL 단축이 성공했습니다.")
            st.write(short_url)
            # The use_column_width parameter has been deprecated and will be removed in a future release. Please utilize the use_container_width parameter instead.
            st.image(qr_img_bytes, caption=f"{short_url}'s QRcode", use_container_width=True)
        else:
            st.warning("URL을 입력하세요.")

if __name__ == "__main__":
    main()
