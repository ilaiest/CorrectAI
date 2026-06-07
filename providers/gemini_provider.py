from google import genai
from config import API_KEY, MODEL
from providers.base import BaseProvider

class GeminiProvider(BaseProvider):
    def correct(self, prompt):
        if not API_KEY:
            return "API key not configured. Please check your settings."
        try:
            client = genai.Client(api_key=API_KEY)
            api_response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )
            return api_response.text
        except Exception as e:
            print (f"type error: {type(e).__name__}, message: {str(e)}")
            return "Error while processing the text. Please try again later."