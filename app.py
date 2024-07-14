from checker import *
import streamlit as st

program = st.sidebar.selectbox('Select program',['APP', 'Info'])

if program == 'APP':
	
	col1, col2 = st.columns(2)
	col1.title("Upload")
	uploaded_file = col1.file_uploader("Choose a file")
	
	
	if not uploaded_file:
		st.error("Insert an image")
		st.stop()
		
	if uploaded_file:
		col1.title("Info")
		col1.markdown(check(uploaded_file), unsafe_allow_html=True)

		col2.title("Image")
		col2.image(uploaded_file, width = 350)
