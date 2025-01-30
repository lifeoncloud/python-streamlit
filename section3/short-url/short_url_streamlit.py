import pyshorteners
import streamlit as st

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    return short_url

def main():
    st.title("URL 단축 사이트")
    st.write("URL 주소를 입력하시면, 단축 URL이 생성됩니다.")
    
    url = st.text_input("URL 입력")
    
    if st.button("URL 단축하기"):
        if url is not None:
            shorten_url_result = shorten_url(url)
            
            st.success("URL 단축을 성공했습니다!")
            st.write(shorten_url_result)
        else:
            st.warning("입력된 URL이 없습니다. URL을 입력해주세요.")


if __name__ == "__main__":
    main()
