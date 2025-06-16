# Indrajaal OSINT 🔱

A modular OSINT dashboard for Indian cybersecurity and cybercrime analysts. Built with ❤️ by Specter 🇮🇳

## 📦 Features
- Instagram, Twitter, Facebook OSINT (public data scraping)
- Dark web & data breach lookup via HaveIBeenPwned
- IP + tower-based location simulator
- Streamlit-powered UI with tabs and branding

## 🚀 Run Locally

```bash
# Setup environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create a .env file
echo "HIBP_API_KEY=your_key" >> .env
echo "IPINFO_TOKEN=your_key" >> .env

# Run app
streamlit run dashboard.py
```

## ☁️ Streamlit Cloud Deployment

Just push this to GitHub and connect your repo to [streamlit.io/cloud](https://streamlit.io/cloud)

Add your environment secrets under:
- `HIBP_API_KEY`
- `IPINFO_TOKEN`