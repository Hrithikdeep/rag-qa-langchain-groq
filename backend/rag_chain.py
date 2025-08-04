# backend/rag_chain.py

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

# Load env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# LLM
llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    groq_api_key=GROQ_API_KEY
)

# Prompt
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful assistant. Use the context below to answer the question.
If the answer isn't in the context, say "I don't know".

Context:
{context}

Question: {question}
Answer:
"""
)

# Final chain
rag_chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

