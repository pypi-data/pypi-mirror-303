from langchain_ollama import ChatOllama

DEFAULT_MODEL = "llama3.1"
# llama3.1 tests performance (2024-10-22) => 12/12 in 15.69s (categories) | 43/43 in 29.77s (headlines)

def get_json_local_model(model_name: str = DEFAULT_MODEL):
    return ChatOllama(model=model_name, format="json", temperature=0)


def get_text_local_model(model_name: str = DEFAULT_MODEL):
    return ChatOllama(model=model_name, temperature=0)
