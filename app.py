from checker import *
import streamlit as st

col1, col2 = st.columns(2)
uploaded_file = col1.file_uploader("Choose a file")
if uploaded_file is not None:
	col1.markdown(check(uploaded_file), unsafe_allow_html=True)
	col2.image(uploaded_file, width = 350)
