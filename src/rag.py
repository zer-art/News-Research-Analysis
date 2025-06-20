from src.utils import Knowledgebase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from src.prompt import system_prompt
from dotenv import load_dotenv
import os

load_dotenv()

def load_rag_chain(urls: str):
    url_list = [u.strip() for u in urls.split(",") if u.strip()]
    if not url_list:
        raise ValueError("No URLs provided.")
    kb = Knowledgebase(URL=url_list)
    docs = kb.load()
    if not docs:
        raise ValueError("No documents loaded from the provided URLs.")
    embd = kb.model()
    vectorstore = kb.vectorstore(docs, embd)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 2})

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}\n\nContext:\n{context}"),
        ]
    )

    gemini_api = os.getenv("GEMINI_API_KEY")
    gemini = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2,
        max_output_tokens=1024,
        top_p=0.95,
        top_k=40,
        google_api_key=gemini_api
    )

    qa_chain = create_stuff_documents_chain(llm=gemini, prompt=prompt)
    rag = create_retrieval_chain(retriever, qa_chain)
    return rag