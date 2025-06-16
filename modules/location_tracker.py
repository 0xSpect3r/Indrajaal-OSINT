import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import ipinfo

def run():
    st.header("Location Tracker")

    ip_address = st.text_input("Enter IP Address")
    token = os.getenv("IPINFO_TOKEN")
    if ip_address and token:
        try:
            handler = ipinfo.getHandler(token)
            details = handler.getDetails(ip_address)
            st.write(details.all)
            loc = details.loc.split(',')
            st.subheader("📍 Map Location")
            st.map(data={"lat": [float(loc[0])], "lon": [float(loc[1])]})
            st.subheader("📡 Tower Trace Log")
            st.code("Tower-A [lat:28.6139, long:77.2090] → Tower-B [lat:28.7041, long:77.1025] → Target Approx: Delhi")
        except Exception as e:
            st.error(f"Error retrieving location: {e}")
    elif not token:
        st.error("IPInfo token not set. Please check your .env file.")