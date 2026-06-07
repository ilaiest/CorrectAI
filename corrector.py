from providers.gemini_provider import GeminiProvider
from providers.ollama_provider import OllamaProvider
from config import ACTIVE_PROVIDER as model_option

def text_corrector(text):
    prompt = f"""
Corrige solo ortografía, acentos y puntuación. Conserva tono y palabras. No formalices ni des alternativas. Devuelve:
Texto corregido:
Cambios importantes: máximo 3.
Texto: {text}
"""
    if model_option == "gemini":
        provider = GeminiProvider()
    elif model_option == "ollama":
        provider = OllamaProvider()
    elif model_option == "bedrock":
        return {"response": "Model not supported yet. Please change your settings"}
    # Handle other models if needed
    else:
        return {"response": "Model not supported. Please check your settings."}
    model_output = provider.correct(prompt)
    return  {"response": model_output}
