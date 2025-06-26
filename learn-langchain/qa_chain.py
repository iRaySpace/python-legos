from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA


def load_qa_chain():
    loader = TextLoader("datasets/ExpenseLogService.kt")
    docs = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    
    embeddings = HuggingFaceEmbeddings(model_name="microsoft/codebert-base")
    db = FAISS.from_documents(chunks, embeddings)

    return RetrievalQA.from_chain_type(
        llm=OllamaLLM(model="mistral"),
        retriever=db.as_retriever(),
    )
