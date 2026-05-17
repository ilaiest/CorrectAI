from google import genai

GEMINI_MODEL = "gemini-3.1-flash-lite-preview"


def text_corrector(text):
    prompt = f"""
Corrige solo ortografía, acentos y puntuación. Conserva tono y palabras. No formalices ni des alternativas. Devuelve:
Texto corregido:
Cambios importantes: máximo 3.
Texto: {text}
"""

    model_output = call_gemini_api(prompt)
    return  {"respuesta": model_output}


def call_gemini_api(prompt):
    try:
        client = genai.Client()
        api_response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )
        return api_response.text
    except Exception as e:
        print (f"type error: {type(e).__name__}, message: {str(e)}")
        return "Error while processing the text. Please try again later."