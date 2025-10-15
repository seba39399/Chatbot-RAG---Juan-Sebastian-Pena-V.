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
