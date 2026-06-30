from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStore
from embeddings import get_embeddings


import json

from typing import List

FAISS_DIR = 'faiss_index'

def load_docs() -> List[Document]:
    JSON_PATH_STR = 'docs/data/qna_data.json'

    loader = TextLoader(JSON_PATH_STR, encoding='utf-8')

    loaded_docs = loader.load()
    json_docs = json.loads(loaded_docs[0].page_content)

    return [
        Document(
            page_content=f'질문: {doc["question"]} \n\n 답변: {doc["answer"]}',
            metadata={
                "id": doc["id"],
                "category": doc["category"],
                "keywords": doc["keywords"],
            }
        )
        for doc in json_docs
    ]


def embedding(docs: List[Document]):
    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(
        documents=docs,
        embedding=embeddings,
    )

    return vectorstore

def save_vector_to_local(vectorstore):
    vectorstore.save_local(FAISS_DIR)

def load_vector_from_local():
    return FAISS.load_local(
        FAISS_DIR,
        embeddings=get_embeddings(),
        allow_dangerous_deserialization=True,
    )

def init_vectorstore():
    docs = load_docs()
    vectorstore = embedding(docs)
    save_vector_to_local(vectorstore)
    return vectorstore