import streamlit as st
import json
import re
import time

# Custom Module Imports (Modular Architecture)
import engine    # The "Brain" (AI logic)
import database  # The "Database" (History/Stats logic)

# Page configuration
st.set_page_config(
    page_title="ShieldAI - Scam & Fraud Detection Assistant",
    page_icon="🛡️",
    layout="centered"
)

# UI/UX: Custom CSS
st.markdown("""
<style>
    .risk-score {
        font-size: 1.2rem; font-weight: bold; padding: 5px 10px; border-radius: 5px; margin-bottom: 10px; display: inline-block;
    }
    .low-risk { background-color: #d4edda; color: #155724; }
    .medium-risk { background-color: #fff3cd; color: #856404; }
    .high-risk { background-color: #f8d7da; color: #721c24; }
</style>
""", unsafe_allow_html=True)

# UI/UX: Sidebar
with st.sidebar:
    st.header("ShieldAI Control Panel")
    
    if st.button("New Chat", use_container_width=True):
        database.clear_history()
        st.session_state.messages = []
        st.rerun()
        
    if st.button("Statistic data", use_container_width=True):
        stats = database.get_stats()
        st.subheader("ShieldAI Statistics")
        st.metric("Total Analyzed", stats['total_analyzed'])
        st.metric("High Risk Scams", stats['high_risk'], delta_color="inverse")
        st.write(f"Medium Risk: {stats['medium_risk']} | Low Risk: {stats['low_risk']}")
        
    if st.button("History", use_container_width=True):
        history = database.load_history()
        if not history:
            st.info("No chat history available.")
        else:
            st.write("---")
            for h in history[-5:]: # Last 5 messages
                st.caption(f"{h['role'].upper()}: {h['content'][:50]}...")

# Initialize Session State Chat History
if "messages" not in st.session_state:
    st.session_state.messages = database.load_history()
    if not st.session_state.messages:
        st.session_state.messages = [
            {"role": "assistant", "content": "🛡️ **Welcome to ShieldAI!** I am your digital protector. Paste any suspicious message, email, or link here, and I will analyze it for scams and fraud."}
        ]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message[ "content"], unsafe_allow_html=True)

# Accept user input
if prompt := st.chat_input("Paste a suspicious message or link here..."):
    # Save User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    database.save_chat_to_db("user", prompt)
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("ShieldAI is analyzing..."):
            # Call the AI Engine (Brain Module)
            raw_ai_response = engine.get_ai_response(prompt)
            
            # Post-processing the raw AI response (UI Formatting)
            data_match = re.search(r'<data>(.*?)</data>', raw_ai_response, re.DOTALL)
            clean_text = re.sub(r'<data>.*?</data>', '', raw_ai_response, flags=re.DOTALL).strip()
            
            if data_match:
                try:
                    data = json.loads(data_match.group(1))
                    score, status = data['risk_score'], data['status']
                    css_class = "low-risk" if score < 30 else "medium-risk" if score < 70 else "high-risk"
                    full_response = f"### Analysis Result: {status}\n" + \
                                   f'<div class="risk-score {css_class}">Risk Score: {score}/100</div>\n\n' + clean_text
                except:
                    full_response = raw_ai_response
            else:
                full_response = raw_ai_response

            # Simulate streaming (UI/UX effect)
            displayed_text = ""
            for chunk in full_response.split(' '):
                displayed_text += chunk + " "
                message_placeholder.markdown(displayed_text + "▌", unsafe_allow_html=True)
                time.sleep(0.02)
            message_placeholder.markdown(displayed_text, unsafe_allow_html=True)
            
    # Save Assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    database.save_chat_to_db("assistant", full_response)
