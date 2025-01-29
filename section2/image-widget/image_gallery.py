import streamlit as st

def main():
    st.title("이미지 갤러리")
    st.subheader("이미지 업로드")
    uploaded_files = st.file_uploader("이미지 파일을 업로드하세요.", accept_multiple_files=True)

    if uploaded_files:
        image_files = list(uploaded_files)
        image_files.sort(key=lambda x: x.name)

        st.subheader("업로드 결과")
        st.success(f"총 {len(image_files)}개의 사진이 업로드 되었습니다.")

        st.subheader("이미지 갤러리")
        
        # 이미지가 1개면 st.image로 이미지 파일만 올리고, 2개 이상이면 st.slider로 갤러리 형식으로 올리기
        if len(image_files) == 1:
            st.image(image_files)
        else:
            index = st.slider("이미지 선택", 0, len(image_files)-1, 0)
            st.image(image_files[index], use_container_width=True, caption=image_files[index].name)
            
        
    
if __name__ == '__main__':
    main()

