from langchain.chains import ConversationChain
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from jinja2 import Template

from utils.utils import read_markdown_file
from scripts.query_vector_store import query_vector_store
from pathlib import Path

from utils.logging_utils import create_logger

def main():
    logger = create_logger()

    prompt = PromptTemplate(
        input_variables=["retrieved_reviews", "history", "user_input"],
        template=read_markdown_file(Path("./templates/chat_prompt.md"))
    )
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
    )
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    memory = ConversationBufferMemory(memory_key="history", return_messages=True)

    vector_store = FAISS.load_local("movie_reviews_vector_store", embeddings, "index", allow_dangerous_deserialization=True)

    conversation = ConversationChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
    )
    while True:
        user_input = input("Enter message: ")
        if user_input.lower() == "exit":
            break

        retrieved_reviews = query_vector_store(user_input, vector_store)
        retrieved_context = ""
        for review in retrieved_reviews:
            retrieved_context += f"{review.page_content}\n"

        response = conversation.run(
            input=user_input, 
            retrieved_context=retrieved_context
        )
        logger.info(response)

if __name__ == "__main__":
    main()