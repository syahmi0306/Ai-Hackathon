# ShieldAI - Scam & Fraud Detection Assistant 🛡️

ShieldAI is an intelligent system designed to protect users from digital threats by analyzing messages, emails, and links for scam indicators. This project was developed for the **National Level AI Hackathon 2026**.

## Features
- **Message/Email Analysis**: Paste any suspicious text to get a risk score and detailed breakdown of scam indicators.
- **Link/URL Analysis**: Check suspicious URLs for phishing or malicious patterns.
- **AI-Powered Insights**: Utilizes Google Gemini API for advanced natural language understanding and threat detection.
- **Explainable AI**: Provides clear explanations and actionable recommendations for every analysis.

## Setup Instructions

### 1. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 2. Get a Gemini API Key
You will need a Google Gemini API key to power the "brain" of the application.
- Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
- Create a new API key.

### 3. Run the Application
Start the Streamlit server:
```bash
streamlit run app.py
```

### 4. Usage
- Open the URL provided by Streamlit (usually `http://localhost:8501`).
- Enter your Gemini API key in the sidebar.
- Start analyzing suspicious content!

## Future Improvements
- [ ] Add support for image/screenshot analysis (using Gemini Vision).
- [ ] Integrate with real-world threat intelligence feeds.
- [ ] Browser extension for real-time protection.
- [ ] Multi-language support for global scam detection.
