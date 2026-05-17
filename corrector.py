from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite-preview")

def text_corrector(text):
    prompt = f"""
Corrige solo ortografía, acentos y puntuación. Conserva tono y palabras. No formalices ni des alternativas. Devuelve:
Texto corregido:
Cambios importantes: máximo 3.
Texto: {text}
"""

    model_output = call_gemini_api(prompt)
    return  {"response": model_output}


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