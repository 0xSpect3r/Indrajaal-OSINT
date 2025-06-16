import streamlit as st
from modules import instagram_osint, twitter_osint, facebook_osint, breach_checker, location_tracker

st.set_page_config(page_title="Indrajaal OSINT", layout="wide")

# Title Banner (HTML with Saffron Highlight)
st.markdown(
    """
    <h1 style='text-align: center; color: #ff9933;'>
        🔱 Indrajaal OSINT Dashboard
    </h1>
    <h4 style='text-align: center; color: #ffffff;'>
        Built by Specter 🇮🇳 for National Cyber Defense
    </h4>
    <hr>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Instagram OSINT", "Twitter OSINT", "Facebook OSINT",
    "Leak Checker", "Location Tracker"
])

with tab1:
    instagram_osint.run()
with tab2:
    twitter_osint.run()
with tab3:
    facebook_osint.run()
with tab4:
    breach_checker.run()
with tab5:
    location_tracker.run()