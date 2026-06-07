from config import MODEL
from providers.base import BaseProvider
import ollama


class OllamaProvider(BaseProvider):
    def correct(self, prompt):
        if not MODEL:
            return "Model not configured. Please check your settings."
        try:
            api_response = ollama.chat(
                model = MODEL,
                messages=[{
                    "role":"user",
                    "content": prompt
                }
            ])
            return api_response["message"]["content"]
        except Exception as e:
            print (f"type error: {type(e).__name__}, message: {str(e)}")
            return "Error while processing the text. Please try again later."


