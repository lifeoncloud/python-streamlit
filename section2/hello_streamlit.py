import streamlit as st

st.title("파이썬 Streamlit 페이지")
st.write("이것은 st.title 입니다.")
st.write("---")

st.header("Streamlit의 Header")
st.write("이것은 st.header 입니다.")
st.write("---")

st.subheader("Streamlit의 SubHeader")
st.write("이것은 st.subheader 입니다.")
st.write("---")

st.write("st.write")
st.write("st.write()는 print()같은 역할을 해요.")
st.write("---")

st.text("st.text")
st.text("st.text도 쓰지만, 일반적으로는 st.write를 더 많이 사용합니다.")
st.write("---")

st.write("st.write('---')")
st.write("---를 쓰면 구분선이 생깁니다. 바로 이렇게!")
st.write("---")

st.markdown("Markdown도 쓸 수 있어요.")
st.markdown("이것은 **bold** 처리된 텍스트랍니다 :)")
