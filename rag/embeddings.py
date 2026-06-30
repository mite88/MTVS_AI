from langchain_ollama.embeddings import OllamaEmbeddings

MODEL_NAME = "nomic-embed-text"

def get_embeddings():
    return OllamaEmbeddings(model=MODEL_NAME)

