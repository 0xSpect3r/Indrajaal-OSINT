import streamlit as st
from facebook_scraper import get_profile

def run():
    st.header("Facebook OSINT")
    username = st.text_input("Enter Facebook username or ID")
    if username:
        st.info(f"Trying to get public info for: {username}")
        try:
            profile = get_profile(username, cookies="cookies.txt")
            for key, value in profile.items():
                st.write(f"**{key.capitalize()}**: {value}")
        except Exception as e:
            st.error(f"Failed to retrieve profile: {e}")