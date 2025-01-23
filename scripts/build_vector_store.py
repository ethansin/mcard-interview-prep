import langchain_openai
import langchain_community
import faiss
import nltk

from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from uuid import uuid4
from nltk.corpus import movie_reviews

from utils.corpus_utils import check_corpus_downloaded
from utils.logging_utils import create_logger
from pathlib import Path

def create_document(document_contents: str, sentiment: str):
    return Document(
        page_content=document_contents,
        metadata={"sentiment": sentiment}
    )

def main():

    logger = create_logger()

    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    dim = len(embeddings.embed_query("Initialize embedding dimensions for index."))
    index = faiss.IndexFlatL2(dim)


    vector_store = FAISS(
        embedding_function=embeddings,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={},
    )

    if not check_corpus_downloaded("movie_reviews", logger=logger):
        nltk.download("movie_reviews")

    documents = [
        create_document(movie_reviews.raw(file), movie_reviews.categories(file))
        for file in movie_reviews.fileids()
        ]
    
    uuids = [str(uuid4()) for _ in range(len(documents))]
    vector_store.add_documents(documents=documents, ids=uuids)
    vector_store.save_local(Path("./movie_reviews_vector_store"))
    
if __name__ == "__main__":
    main()

    