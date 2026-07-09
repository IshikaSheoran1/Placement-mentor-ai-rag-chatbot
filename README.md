# 🤖 Placement Mentor AI

An AI-powered **Retrieval-Augmented Generation (RAG)** chatbot that allows users to upload placement-related PDF documents and ask natural language questions.

Instead of searching manually through lengthy placement brochures, the chatbot retrieves the most relevant information using semantic search and generates accurate, document-grounded responses using Google's Gemini LLM.

---

## 🚀 Features

- 📄 Upload any PDF document
- 💬 Ask questions in natural language
- 🧠 Semantic Search using Sentence Transformers
- ⚡ Fast retrieval using FAISS Vector Database
- 🤖 Context-aware answers using Gemini
- 🌐 Interactive Streamlit interface

---

## 🏗️ Project Architecture

```
                Upload PDF
                     │
                     ▼
              Extract Text
                     │
                     ▼
               Chunk Document
                     │
                     ▼
      Generate Embeddings
      (all-MiniLM-L6-v2)
                     │
                     ▼
          Store in FAISS
                     │
                     ▼
            User Question
                     │
                     ▼
        Generate Query Embedding
                     │
                     ▼
      Retrieve Relevant Chunks
                     │
                     ▼
              Gemini LLM
                     │
                     ▼
              Final Answer
```

---

## 🛠 Tech Stack

- Python
- Streamlit
- Sentence Transformers
- FAISS
- Google Gemini API
- PyPDF
- NumPy

---

## 📂 Project Structure

```
Placement_mentor_ai/

├── app.py
├── chatbot.py
├── src/
│   ├── pdf_loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── llm.py
│   └── __init__.py
│
├── data/
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/IshikaSheoran1/Placement-mentor-ai-rag-chatbot.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

- Improve retrieval quality
- Multi-PDF support
- Conversation history
- Source citations
- Better prompt engineering
- Dark mode

---

## 👩‍💻 Author

**Ishika Sheoran**

B.Tech | MNIT Jaipur

Interested in Data Analytics, AI, Machine Learning and Software Development.
