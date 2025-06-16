import streamlit as st
import requests

def run():
    st.header("Leak Checker (HaveIBeenPwned)")
    email = st.text_input("Enter email or phone number")
    if email:
        headers = {
            'User-Agent': 'IndrajaalOSINT/1.0',
        }
        st.info("Checking for breaches using HaveIBeenPwned...")
        try:
            response = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}", headers=headers)
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