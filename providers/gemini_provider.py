from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL


def call_gemini_api(prompt):
    if not GEMINI_API_KEY:
        return "API key not configured. Please check your settings."
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        api_response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )
        return api_response.text
    except Exception as e:
        print (f"type error: {type(e).__name__}, message: {str(e)}")
        return "Error while processing the text. Please try again later."