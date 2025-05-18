import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM

from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

def cargar_pdf(ruta_pdf):
    print("📄 Cargando PDF...")
    loader = PyPDFLoader(ruta_pdf)
    return loader.load()

def dividir_chunks(docs):
    print("✂️ Dividiendo en chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)

def crear_base_vectorial(chunks):
    print("🧠 Generando embeddings con nomic-embed-text desde Ollama...")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    
    print("💾 Guardando en base Chroma persistente...")
    vectordb = Chroma.from_documents(chunks, embedding=embeddings, persist_directory="chroma_db")
    vectordb.persist()
    return vectordb

def cargar_vectorstore():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    return vectordb

def consulta_rag():
    vectordb = cargar_vectorstore()
    
    llm = OllamaLLM(model="gemma:2b")
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

    while True:
        pregunta = input("Pregunta ('salir' para terminar): ")
        if pregunta.lower() == "salir":
            break
        docs = vectordb.similarity_search(pregunta, k=3)
        respuesta = chain.invoke({"input_documents": docs, "question": pregunta})
        print(f"\n💬 Respuesta:\n{respuesta}\n")

def main():
    if not os.path.exists("chroma_db"):
        documentos = cargar_pdf("C:\\Users\\juan_\\Downloads\\chatbot-rag\\data\\documento.pdf")  # Cambia aquí la ruta a tu PDF
        chunks = dividir_chunks(documentos)
        crear_base_vectorial(chunks)
    else:
        print("🗃️ Base de datos vectorial encontrada, cargando...")

    print("🤖 Iniciando chatbot RAG...")
    consulta_rag()

if __name__ == "__main__":
    main()
