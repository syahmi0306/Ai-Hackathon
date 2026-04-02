from google import genai

GEMINI_API_KEY = "AIzaSyD-m3QjtAqZes4bcBRap3CZWdgLPz4zqwo"
client = genai.Client(api_key=GEMINI_API_KEY)

print("Listing available models for this API key:")
try:
    for model in client.models.list():
        print(f"- {model.name}")
except Exception as e:
    print(f"Error: {e}")
