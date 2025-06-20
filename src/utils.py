from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS    
from langchain_huggingface import HuggingFaceEmbeddings
import pickle
import os


class Knowledgebase(): 
    def __init__(self, URL):
        self.URL = URL if isinstance(URL, list) else [URL]

    def load(self): 
        loaders = UnstructuredURLLoader(urls=self.URL)
        documents = loaders.load() 
        return documents
    
    def split(self, documents):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
        return texts
    
    def model(self): 
        embd  = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        return embd
    
    def vectorstore(self, texts, embd):
        texts = self.split(texts)
        if not texts:
            raise ValueError("No text chunks to index. Please check your URLs or document loader.")
        embd = self.model()
        vectorstore = FAISS.from_documents(texts, embd)
        with open("vectorstore.pkl", "wb") as f:
            pickle.dump(vectorstore, f)
        return vectorstore
        