import streamlit as st;


st.header("Welcome to Recommendation for You")
st.subheader("Discover Your Next Favorite Movies and Books!")

st.text("Are you tired of endlessly scrolling through countless titles, unsure of what to watch or read next? Look no further!")
st.text("Recommendation for You, is here to curate personalized suggestions tailored just for you") 
st.text("Our cutting-edge recommendation engine analyzes your preferences, ensuring that each suggestion is a perfect match for your unique taste.")


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



    
