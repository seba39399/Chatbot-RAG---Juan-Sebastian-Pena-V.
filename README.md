# 🤖 RAG Chatbot — Generation Augmented Retrieval

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-green)](https://streamlit.io/)
[![Chroma](https://img.shields.io/badge/VectorStore-Chroma-orange)](https://www.trychroma.com/)

---

## 🧠 Description

This project provides a **Interactive chatbot based on RAG (Retrieval-Augmented Generation)** which allows you to answer questions with context extracted from PDF documents.

General flow:
1. Process and vectorize the PDF content.
2. Query the vector store to retrieve relevant fragments.
3. Use a language model (`gemma:2b`) to generate a contextually consistent response.

---

## 🏗️ System architecture

PDF --> Preprocessing --> Embeddings (Ollama) --> Vector Store (Chroma)
User --> Recovery --> Model Gemma:2b --> Response contextualized

---

## ✨ Characteristics

- 📚 Support for multiple PDF files.
- 💬 Natural language query with rich context.
- 🧠 Using Ollama embeddings.
- 🤖 Generation with model `gemma:2b`. 
- 🖥️ Simple web interface with Streamlit.
- 🧪 Optional integration with LangSmith.

---

## 🧰 Requirements

- Python 3.8 or superior  
- Git  
- Virtual environment (recommended)

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/seba39399/Chatbot-RAG---Juan-Sebastian-Pena-V.git
cd Chatbot-RAG---Juan-Sebastian-Pena-V

# 2. Create virtual environment
python -m venv .venv

# 3. Activate virtual environment
# Windows
.\.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

## 🔐 Configuration (optional)

If you want to enable traceability with LangSmith:

```bash
# Windows
setx LANGCHAIN_API_KEY "tu_api_key_aqui"

# Linux/macOS
export LANGCHAIN_API_KEY="tu_api_key_aqui"

```
## 💬 Examples of use

Question: Who is the main character?
Answer: The main character is Little Red Riding Hood.

Question: What is the story about?
Answer: It's about how Little Red Riding Hood learns not to trust strangers and to follow her mother's instructions.

Question: How does the story end?
Answer: It ends when Little Red Riding Hood arrives at her grandmother's house and encounters a wolf.

---

## 🤝 Contributions and credits

## 👨‍💻 Developed by Biomedical Engineer and Artificial Intelligence Specialist: Juan Sebastián Peña Valderrama

## 🚀 Inspired by RAG paradigms and open-source tools:

-LangChain

-Ollama

-Chroma

-Streamlit

## 🧩 Open contributions: issues, suggestions and PRs are welcome
