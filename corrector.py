from providers.gemini_provider import GeminiProvider
from providers.ollama_provider import OllamaProvider
from config import ACTIVE_PROVIDER as model_option

def text_corrector(text):
    prompt = f"""
Corrige únicamente errores de ortografía, acentos, puntuación y palabras mal escritas.
Conserva el significado, tono y estilo del texto.
No agregues explicaciones, títulos, comillas ni introducciones.
Devuelve solo el texto corregido.
Texto:{text}
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
