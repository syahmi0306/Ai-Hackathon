import json
import os

# Local database file
DB_FILE = "chat_history.json"

def save_chat_to_db(role, content):
    """
    Saves message to a local JSON file for history persistence.
    """
    history = load_history()
    history.append({"role": role, "content": content})
    with open(DB_FILE, 'w') as f:
        json.dump(history, f, indent=4)

def load_history():
    """
    Loads chat history from the local JSON file.
    """
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def clear_history():
    """
    Deletes the local chat history.
    """
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

def get_stats():
    """
    Calculates statistics from the chat history.
    """
    history = load_history()
    total_scams_detected = 0
    high_risk_count = 0
    medium_risk_count = 0
    low_risk_count = 0
    
    for msg in history:
        if msg['role'] == 'assistant':
            if "High Risk" in msg['content']:
                high_risk_count += 1
            elif "Medium Risk" in msg['content']:
                medium_risk_count += 1
            elif "Low Risk" in msg['content']:
                low_risk_count += 1
                
    return {
        "total_analyzed": len([m for m in history if m['role'] == 'user']),
        "high_risk": high_risk_count,
        "medium_risk": medium_risk_count,
        "low_risk": low_risk_count
    }
