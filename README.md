# 🤖 Chatbot RAG — Recuperación Aumentada por Generación

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-green)](https://streamlit.io/)
[![Chroma](https://img.shields.io/badge/VectorStore-Chroma-orange)](https://www.trychroma.com/)

---

## 🧠 Descripción

Este proyecto provee un **chatbot interactivo basado en RAG (Retrieval-Augmented Generation)** que permite responder preguntas con contexto extraído de documentos PDF.

Flujo general:
1. Procesar y vectorizar el contenido del PDF.  
2. Consultar el vector store para recuperar fragmentos relevantes.  
3. Usar un modelo de lenguaje (`gemma:2b`) para generar una respuesta coherente con el contexto.

---

## 🏗️ Arquitectura del sistema

PDF --> Preprocesamiento --> Embeddings (Ollama) --> Vector Store (Chroma)
Usuario --> Recuperación --> Modelo Gemma:2b --> Respuesta contextualizada

---

## ✨ Características

- 📚 Soporte para múltiples archivos PDF.  
- 💬 Consulta en lenguaje natural con contexto enriquecido.  
- 🧠 Uso de embeddings de Ollama.  
- 🤖 Generación con modelo `gemma:2b`.  
- 🖥️ Interfaz web sencilla con Streamlit.  
- 🧪 Integración opcional con LangSmith.

---

## 🧰 Requisitos

- Python 3.8 o superior  
- Git  
- Entorno virtual (recomendado)

---

## ⚙️ Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/seba39399/Chatbot-RAG---Juan-Sebastian-Pena-V.git
cd Chatbot-RAG---Juan-Sebastian-Pena-V

# 2. Crear entorno virtual
python -m venv .venv

# 3. Activar entorno virtual
# En Windows
.\.venv\Scripts\activate
# En Linux/macOS
source .venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt
