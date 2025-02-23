import streamlit as st
import os
from docx import Document
from docx2pdf import convert
import comtypes

# Streamlit 교육 수료증 자동 생성 및 PDF 다운로드 기능
# To be updated for Mac OS

def main():
    comtypes.init()
    st.title("교육 수료증생성 및 PDF 다운로드")
    
    name = st.text_input("이름을 입력하세요.")
    course = st.text_input("교육명을 입력하세요.")
    date = st.text_input("수료일을 입력하세요.(예: 2025 1월 3일) : ")
    
    if st.button("수료증 생성"):
        doc = Document("template.docx")
        for paragraph in doc.paragraphs:
            if "NAME" in doc.paragraph.text:
                paragraph.text = paragraph.text.replace("NAME", name)
            elif "COURSE" in doc.paragraph.text:
                paragraph.text = paragraph.text.replace("COURSE", course)
            elif "DATE" in doc.paragraph.text:
                paragraph.text = paragraph.text.replace("DATE", date)
                
        
        doc_filename = f"{name}_{course}_수료증.docx"  
        pdf_filename = f"{name}_{course}_수료증.pdf"  
        
        doc.save(doc_filename)
        
        convert(doc_filename, pdf_filename)
        st.success("교육 수료증 생성이 완료되었습니다. 아래에서 다운로드 받으세요.")
        
        # pdf_filename을 바이너리 형식으로 읽기
        with open(pdf_filename, "rb") as f:
            pdf_bytes = f.read()
            
        st.download_button(Label="수료증 다운로드", data=pdf_bytes, file_name=pdf_filename)
        
        os.remove(doc_filename)
        os.remove(pdf_filename)
        
                
    
if __name__ == '__main__':
    main()
