

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings

# 1. Load PDF
loader = PyPDFLoader("data/2505.17058v1.pdf")
documents = loader.load()

# 2. Chunk it
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# 3. Embed chunks
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(docs, embedding_model)

# 4. Save vectorstore
db.save_local("vectorstore")

print(f"✅ {len(docs)} chunks embedded and saved to vectorstore/")

