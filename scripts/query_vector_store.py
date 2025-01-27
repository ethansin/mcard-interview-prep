from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from nltk.corpus import movie_reviews

from utils.logging_utils import create_logger
from logging import Logger
from pathlib import Path

def query_vector_store(query: str, vector_store: FAISS, embeddings: OpenAIEmbeddings, logger: Logger, k: int = 2):
    results = vector_store.similarity_search(
        query,
        k=k,
    )
    for res in results:
        print(f"* {res.page_content} [{res.metadata}]")


def main():
    logger = create_logger()

    query=input("Enter query: ")
    vector_store_path = Path("./movie_reviews_vector_store")
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    vector_store = FAISS.load_local(vector_store_path, embeddings, "index", allow_dangerous_deserialization=True)

    query_vector_store(
        query=query,
        vector_store=vector_store,
        embeddings=embeddings,
        logger=logger,
        k=2,
    )

if __name__ == "__main__":
    main()