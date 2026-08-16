import streamlit as st
from pathlib import Path

st.header(":zap: Github Profile Readme Generator", width="content", text_alignment="center")

# Personal info
st.header("Personal Info")
with st.expander("Personal Info"):
    col1, col2 = st.columns(2)
    name = col1.text_input("Name")
    email = col2.text_input("Email")
    phone = col1.text_input("Phone")
    homepage = col2.text_input("Homepage")
    location = st.text_input("Location")
    
# Social Media
st.header("Social Media", )   
with st.expander("Social Media"):
    st.markdown("Enter your social media usernames (not links):")
    col1, col2 = st.columns(2)
    github = col1.text_input("Github")
    linkedin = col2.text_input("LinkedIn")
    twitter = col1.text_input("Twitter")
    facebook = col2.text_input("Facebook")
    instagram = col1.text_input("Instagram")
    youtube = col2.text_input("YouTube")
    medium = col1.text_input("Medium")


# Select Theme
st.header(" Theme")
themes = Path("src/themes").iterdir()
themes = [theme.name for theme in themes]              
theme = st.selectbox("Select Theme", themes)
st.markdown(f"Selected Theme: **{theme}**")

# Generate Readme
st.header("Generate Readme")
if st.bu
