

import streamlit as st;
st.subheader("welcome to")
st.header("Recomendation for you.")
st.text("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
st.text("Lorem Ipsum has been the industry's standard dummy text ever since the 1m")
st.text("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
st.text("Lorem Ipsum has been the industry's standard dummy text ever since the 1m")

movie_name=""

page_bg_image= """
    <style>
   [data-testid="stAppViewContainer"]{
   background-color:#5e5f88;
   background-image:url("https://img.freepik.com/free-vector/film-stripes-reels-realistic-composition-with-curvy-strip-front-neon-lights-background-with-glows_1284-59000.jpg?size=626&ext=jpg&ga=GA1.1.9915666.1698340496&semt=ais");
   background-size:cover;
   opacity:0.8;
   }
   </style>
    """
st.markdown(page_bg_image,unsafe_allow_html=True)