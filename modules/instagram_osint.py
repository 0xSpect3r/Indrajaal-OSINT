import streamlit as st
import instaloader

def run():
    st.header("Instagram OSINT")
    username = st.text_input("Enter Instagram username")
    if username:
        st.info(f"Fetching public profile info for: {username}")
        loader = instaloader.Instaloader()
        try:
            profile = instaloader.Profile.from_username(loader.context, username)
            st.write(f"**Full Name:** {profile.full_name}")
            st.write(f"**Username:** {profile.username}")
            st.write(f"**Bio:** {profile.biography}")
            st.write(f"**Followers:** {profile.followers}")
            st.write(f"**Following:** {profile.followees}")
            st.write(f"**Posts:** {profile.mediacount}")
            st.write(f"**Is Private:** {profile.is_private}")
            st.write(f"**Last Activity (approx):** {profile.get_posts().__next__().date_utc}")
        except Exception as e:
            st.error(f"Failed to fetch data: {e}")