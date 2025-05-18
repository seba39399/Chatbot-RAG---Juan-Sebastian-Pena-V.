import os
import streamlit as st
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

@st.cache_resource
def cargar_vectordb():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    return vectordb

def main():
    st.title("🤖 Chatbot RAG - PDF Knowledge Base - Juan Sebastián Peña V.")

    vectordb = cargar_vectordb()

    st.sidebar.header("Configuración del modelo")
    temperature = st.sidebar.slider("Temperatura", 0.0, 1.0, 0.7, 0.01)
    top_p = st.sidebar.slider("Top-p", 0.0, 1.0, 0.9, 0.01)
    top_k = st.sidebar.number_input("Top-k", min_value=1, max_value=100, value=40)

    # No usar variable de entorno LANGCHAIN_API_KEY por ahora
    # api_key = os.getenv("LANGCHAIN_API_KEY")
    # if api_key is None:
    #     st.warning("⚠️ No se encontró la variable de entorno LANGCHAIN_API_KEY para Langsmith.")
    #     st.stop()

    # No usar LangChainTracer para evitar error
    # llm con parámetros de temperatura, top_p y top_k
    llm = OllamaLLM(
        model="gemma:2b",
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        verbose=True,
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
Eres un asistente útil y conciso. Usa el siguiente contexto para responder la pregunta.

Contexto:
{context}

Pregunta:
{question}

Respuesta útil y concisa:
"""
    )

    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

    if "historial" not in st.session_state:
        st.session_state.historial = []

    pregunta = st.text_input("Escribe tu pregunta:")

    if st.button("Enviar") and pregunta:
        docs = vectordb.similarity_search(pregunta, k=3)
        inputs = {"input_documents": docs, "question": pregunta}
        respuesta = chain.invoke(input=inputs)["output_text"]
        st.session_state.historial.append((pregunta, respuesta))

    if st.session_state.historial:
        for q, r in st.session_state.historial:
            st.markdown(f"**Pregunta:** {q}")
            st.markdown(f"**Respuesta:** {r}")
            st.markdown("---")

if __name__ == "__main__":
    main()
