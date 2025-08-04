# app/main.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import tempfile

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.rag_chain import rag_chain  # import only the chain, not file-based loading

# Load embedding model once
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# UI
st.set_page_config(page_title="🧠 Chat with Your PDF", layout="centered")
st.title("📄 Upload a PDF & Ask Questions (RAG + Groq)")
st.markdown("This app uses **LangChain + FAISS + Groq** to answer questions from uploaded PDF files.")

uploaded_file = st.file_uploader("📤 Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    # Save to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_pdf_path = tmp_file.name

    # Load + split + embed
    loader = PyPDFLoader(tmp_pdf_path)
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(pages)

    # Embed to FAISS in memory
    vectorstore = FAISS.from_documents(chunks, embedding=embedding_model)

    question = st.text_input("❓ Ask something from this PDF:")
    if st.button("Get Answer") and question:
        with st.spinner("Thinking..."):
            docs = vectorstore.similarity_search(question, k=3)
            answer = rag_chain.invoke({"input_documents": docs, "question": question})
            st.success("✅ Answer:")
            st.markdown(f"**🧠 Answer:** {answer['output_text'].strip()}")


