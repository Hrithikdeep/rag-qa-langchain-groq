# 🧠 RAG PDF Q&A App using LangChain + Groq

🚀 **Live Demo:** [Try it on Streamlit](https://rag-app-langchain-groq-jmv7qhq4cpfyzaj9zahwlb.streamlit.app/)  
📦 **GitHub Repo:** https://github.com/Hrithikdeep/rag-qa-langchain-groq

---

## 📸 Demo Preview

| Upload PDF | Ask Questions | Smart Answers |
|------------|----------------|----------------|
| ![upload](<img width="250" height="150" alt="image" src="https://github.com/user-attachments/assets/da3c39fd-5047-4a13-a812-568e2da07f3e" />
) | ![question](<img width="250" height="150" alt="Screenshot 2025-08-05 at 11 55 12 AM" src="https://github.com/user-attachments/assets/6e56414e-a79f-4e4b-a7c9-de72af7c259c" />
) | ![answer](<img width="250" height="150" alt="Screenshot 2025-08-05 at 11 55 12 AM" src="https://github.com/user-attachments/assets/26e18d86-107a-4a9c-b0ee-1eb656fff99d" />
) |

---

## 📦 What I Built

This is a full-stack **RAG (Retrieval-Augmented Generation) app** that:

✅ Uploads any PDF  
✅ Splits into text chunks  
✅ Converts to embeddings using Hugging Face  
✅ Saves vectors in FAISS  
✅ Retrieves relevant chunks based on user question  
✅ Uses **Groq (Mixtral LLM)** for context-aware answers  
✅ Fully deployed on **Streamlit Cloud**

---

## 🧠 Why I Built This

Large language models (LLMs) forget documents quickly.  
This app uses **RAG** to "remind" the LLM by retrieving exact text chunks from the source document before generating answers — making responses more accurate and grounded.

---

## 🔨 Built With

- 🧠 [LangChain](https://github.com/langchain-ai/langchain)
- ⚡ [Groq LLM](https://console.groq.com)
- 🤗 [Hugging Face Embeddings](https://huggingface.co/sentence-transformers)
- 🔎 [FAISS Vector Store](https://github.com/facebookresearch/faiss)
- 🖥️ [Streamlit](https://streamlit.io)

---

## 📁 Project Structure

```
rag-qa-langchain-groq/
├── app/
│   └── main.py              # Streamlit UI
├── backend/
│   └── rag_chain.py         # RAG logic (retrieve + generate)
├── .streamlit/
│   └── secrets.toml         # Groq API key for Streamlit Cloud
├── requirements.txt         # Clean dependencies
├── .gitignore
└── README.md
```

---

## 🧪 Run Locally in 3 Minutes

```bash
# 1️⃣ Clone the Repo
git clone https://github.com/Hrithikdeep/rag-qa-langchain-groq.git
cd rag-qa-langchain-groq

# 2️⃣ Set Up Virtual Environment
python3 -m venv venv
source venv/bin/activate

# 3️⃣ Install Required Packages
pip install -r requirements.txt

# 4️⃣ Add Your Groq API Key
# Option A: for local dev
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

# Option B: for Streamlit Cloud
mkdir -p .streamlit && echo 'GROQ_API_KEY = "your_groq_api_key_here"' > .streamlit/secrets.toml

# 5️⃣ Run the App
streamlit run app/main.py
```

Then open http://localhost:8501 in your browser.

---

## 🤖 How the App Works (Step-by-Step)

1. 📄 **Upload a PDF**
2. ✂️ **Split it into small text chunks**
3. 🤗 **Convert text into vector embeddings** using Hugging Face
4. 🧠 **Save to FAISS** vector database
5. ❓ **User asks a question**
6. 🔍 **Retrieve relevant chunks**
7. ⚡ **Groq Mixtral LLM generates final answer**

---

## 💾 requirements.txt (Minimal)

```txt
streamlit
langchain==0.3.27
langchain-core
langchain-community
langchain-groq
sentence-transformers
faiss-cpu
pypdf
python-dotenv
```

---

## 🚀 Deploying to Streamlit Cloud

1. Push this project to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Add secret key in **Secrets** tab:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

5. Click **Deploy**

✅ Done — now your app runs live in the cloud.

---
## 🙏 Credits

- [@Hrithikdeep](https://github.com/Hrithikdeep)  
- Built with ❤️ using LangChain + Groq + Streamlit
