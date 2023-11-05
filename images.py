import streamlit as st;
st.subheader("hello set image here")

movie_name=""

page_bg_image= """
    <style>
   [data-testid="stAppViewContainer"]{
   background-color:#5e5f88;
   background-image:url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTC6goKaanirGao3AE0drDUrZAgcRHtdmDTQdBTJeAZQQ&s");
   background-size:cover;
   opacity:0.8;
   }
   </style>
    """
st.markdown(page_bg_image,unsafe_allow_html=True)
    