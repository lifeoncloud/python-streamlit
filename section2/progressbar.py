import streamlit as st
import time

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()


for i in range(1, 101):
    if i == 100:
        status_text.text("진행 완료✅")
    else:
        status_text.text(f"{i} 진행중🏃🏻")
    progress_bar.progress(i)
    time.sleep(0.05)
    
progress_bar.empty()

st.button("다시 진행")
