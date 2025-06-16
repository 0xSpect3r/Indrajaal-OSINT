import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import requests

def run():
    st.header("Leak Checker (HaveIBeenPwned)")
    email = st.text_input("Enter email or phone number")
    hibp_key = os.getenv("HIBP_API_KEY")

    if email and hibp_key:
        headers = {
            'hibp-api-key': hibp_key,
            'User-Agent': 'IndrajaalOSINT/1.0',
        }
        try:
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                breaches = response.json()
                for breach in breaches:
                    st.subheader(breach['Name'])
                    st.write(f"- Domain: {breach['Domain']}")
                    st.write(f"- Breach Date: {breach['BreachDate']}")
                    st.write(f"- Compromised Data: {', '.join(breach['DataClasses'])}")
            elif response.status_code == 404:
                st.success("No breach found for this identifier.")
            else:
                st.warning(f"Response: {response.status_code}, possibly rate-limited.")
        except Exception as e:
            st.error(f"Error: {e}")
    elif not hibp_key:
        st.error("HIBP API key not set. Please check your .env file.")