from providers.gemini_provider import call_gemini_api
from config import ACTIVE_PROVIDER as model_option

def text_corrector(text):
    prompt = f"""
Corrige solo ortografía, acentos y puntuación. Conserva tono y palabras. No formalices ni des alternativas. Devuelve:
Texto corregido:
Cambios importantes: máximo 3.
Texto: {text}
"""
    if model_option == "gemini":
        model_output = call_gemini_api(prompt)
    elif model_option == "bedrock":
        # Handle other models if needed
        print("Bedrock model selected, but not implemented yet.")
    else:
        model_output = "Model not supported. Please check your settings."
    return  {"response": model_output}
