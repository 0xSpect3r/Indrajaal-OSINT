import streamlit as st
import ipinfo
import geopy.distance

def run():
    st.header("Location Tracker")

    ip_address = st.text_input("Enter IP Address")
    if ip_address:
        try:
            access_token = "demo"  # Replace with real token
            handler = ipinfo.getHandler(access_token)
            details = handler.getDetails(ip_address)
            st.write(details.all)

            # Simulated Tower Log
            st.subheader("📡 Tower Trace Log")
            st.code("Tower-A [lat:28.6139, long:77.2090] → Tower-B [lat:28.7041, long:77.1025] → Target Approx: Delhi")

            # Map display
            location = details.loc.split(',')
            st.map(data={"lat": [float(location[0])], "lon": [float(location[1])]})

        except Exception as e:
            st.error(f"Error retrieving location: {e}")