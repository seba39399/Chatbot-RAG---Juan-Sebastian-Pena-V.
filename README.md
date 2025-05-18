# Chatbot RAG

Proyecto de chatbot con recuperación aumentada por generación (RAG).

## Descripción

El chatbot permite cargar una base de conocimiento (preprocesada y almacenada en un vector store Chroma) para responder preguntas con contexto extraído del contenido PDF. Usa embeddings de Ollama y un modelo `gemma:2b` para generación de respuestas.

## Requisitos

- Python 3.8+
- Crear entorno virtual (recomendado)

## Instalación y configuración

1. Clonar este repositorio:

```bash
git clone https://tu-repositorio.git
cd chatbot-rag

2. Crear y activar un entorno virtual:

python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate


3.  Instalar dependencias

4. Configurar variables de entorno si usas Langsmith :

setx LANGCHAIN_API_KEY "tu_api_key_aqui"  # Windows (cerrar/abrir terminal)
export LANGCHAIN_API_KEY="tu_api_key_aqui" # Linux/macOS

Este punto no fue posible realizarlo debido a que el tiempo me limito en su ejecucion y solo obtuve errores, fue el unico punto que me falto.

5. Ejecutar la aplicación:

streamlit run src/app.py

## Uso

Escribe una pregunta relacionada con el contenido de la base de conocimiento (PDF).

El chatbot buscará los fragmentos relevantes en la base vectorial y generará una respuesta contextualizada.


## Preguntas y respuestas contextualizadas de ejemplo

Pregunta: Cuál es el personaje principal?

Respuesta: El personaje principal es Caperucita Roja.

-----

Pregunta: ¿De que trata la historia?

Respuesta: La historia trata sobre cómo Caperucita Roja aprendió a no confiar en desconocidos y seguir las indicaciones de su madre.

-----

Pregunta: ¿Como finalizo la historia?

Respuesta: La historia termina cuando Caperucita Roja llega a la casa de su abuela y se encuenta con un lobo astuto que la escucha y le cuenta todo.





