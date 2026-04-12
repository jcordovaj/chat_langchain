import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import gradio as gr

# ============================================================
# 1. CARGAR VARIABLES DE ENTORNO
# ============================================================
load_dotenv()

# ============================================================
# 2. CREAR EL MODELO Y LOS EMBEDDINGS
# ============================================================
# ChatOpenAI: modelo de lenguaje para generar respuestas
# OpenAIEmbeddings: convierte texto a vectores numericos
#   para buscar documentos similares
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# ============================================================
# 3. CARGAR Y PROCESAR EL DOCUMENTO
# ============================================================
# Leemos el archivo de texto con la informacion del negocio
with open("cafeteria.txt", "r", encoding="utf-8") as f:
    documento = f.read()

# Dividimos el documento en fragmentos (chunks) pequenos.
# Esto permite buscar solo las partes relevantes en vez de
# enviar todo el documento al modelo cada vez.
#   - chunk_size=500: cada fragmento tiene maximo 500 caracteres
#   - chunk_overlap=50: 50 caracteres de solapamiento entre
#     fragmentos para no perder contexto en los bordes
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_text(documento)

# ============================================================
# 4. CREAR LA BASE DE DATOS VECTORIAL (FAISS)
# ============================================================
# FAISS (Facebook AI Similarity Search) almacena los vectores
# de cada fragmento. Cuando el usuario hace una pregunta,
# buscamos los fragmentos mas similares a su pregunta.
# Esto se ejecuta una sola vez al iniciar la aplicacion.
vectorstore = FAISS.from_texts(chunks, embeddings)
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}  # Retorna los 4 fragmentos mas relevantes
)

# ============================================================
# 5. DEFINIR EL PROMPT DEL RAG
# ============================================================
# Este prompt es clave: le decimos al modelo que SOLO responda
# con la informacion del contexto proporcionado. Si no encuentra
# la respuesta, debe decirlo honestamente.
prompt = ChatPromptTemplate.from_template("""Eres el asistente virtual de Café Aurora. Tu trabajo es responder preguntas
de los clientes ÚNICAMENTE usando la información proporcionada en el contexto.

Reglas estrictas:
1. SOLO responde con información que esté en el contexto.
2. Si la pregunta no se puede responder con el contexto, di:
   "Lo siento, no tengo esa información. Te recomiendo contactarnos
   por WhatsApp al +56 9 8765 4321 o por email a contacto@cafeaurora.cl"
3. Sé amable, conciso y útil.
4. Si preguntan precios, siempre menciona el precio exacto.
5. Responde en español.

Contexto:
{context}

Pregunta del cliente: {question}

Respuesta:""")

# ============================================================
# 6. CREAR LA CADENA RAG
# ============================================================
# La cadena conecta: Pregunta -> Buscar documentos -> Prompt -> LLM -> Texto
# RunnablePassthrough() pasa la pregunta sin modificarla
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# ============================================================
# 7. FUNCION DE RESPUESTA PARA GRADIO
# ============================================================
def respond(message, history):
    # Invocamos la cadena RAG con la pregunta del usuario
    response = rag_chain.invoke(message)
    return response

# ============================================================
# 8. CREAR LA INTERFAZ WEB
# ============================================================
demo = gr.ChatInterface(
    fn=respond,
    title="Café Aurora - Asistente Virtual",
    description="Pregúntame sobre nuestro menú, horarios, ubicación, eventos y más.",
    examples=[
        "¿Cuál es el horario de atención los sábados?",
        "¿Tienen opciones veganas?",
        "¿Cuánto cuesta un cappuccino?",
        "¿Hacen delivery?",
        "¿Tienen wifi?",
    ],
)

# ============================================================
# 9. LANZAR LA APLICACION
# ============================================================
if __name__ == "__main__":
    print(f"Documento cargado: {len(chunks)} fragmentos indexados")
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        theme="soft"
    )
