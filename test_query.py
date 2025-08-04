from backend.rag_chain import get_answer

# Ask any question based on your uploaded PDF
question = "What is DO-RAG and how does it improve RAG performance?"

answer = get_answer(question)
print("🧠 Answer:\n", answer)
