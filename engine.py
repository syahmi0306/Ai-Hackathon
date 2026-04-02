from google import genai
import prompts

# Configuration
GEMINI_API_KEY = "AIzaSyD-m3QjtAqZes4bcBRap3CZWdgLPz4zqwo"

def get_ai_response(content):
    """
    Core AI logic: Communicates with Gemini API using prompts from prompts.py
    """
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        # Build prompt from our prompts module
        full_prompt = prompts.get_analysis_prompt(content)
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=full_prompt
        )
        return response.text

    except Exception as e:
        return f"❌ Error: {str(e)}"
