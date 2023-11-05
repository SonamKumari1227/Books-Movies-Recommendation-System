import streamlit as st;

from streamlit_option_menu import option_menu

with st.sidebar:selected=option_menu(
    menu_title=None,
    options=["Home","Movies","Contact"],
    icons=["house","bi bi-film","envelope"],
    orientation="horizontal"
)
if selected=="Home":
    
         st.title("hello i am route file")

#routing content
