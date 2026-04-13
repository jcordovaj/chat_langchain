☕ Chatbot RAG – Café Aurora
Demo práctica de LangChain + FAISS + OpenAI

Chatbot inteligente basado en RAG (Retrieval-Augmented Generation) que responde exclusivamente utilizando información interna de un negocio (en este caso, una cafetería).

Este proyecto está diseñado como un ejemplo simple, práctico y educativo para demostrar cómo construir un sistema completo con LangChain, embeddings, búsqueda vectorial y generación con LLM.

✨ Overview
El chatbot permite hacer preguntas sobre el negocio Café Aurora y garantiza que:
     ✅ Solo responde con información contenida en el documento fuente
     ❌ No inventa respuestas fuera del contexto (reduce alucinaciones) 
     🤖 Utiliza un pipeline completo de RAG

🧠 ¿Qué es RAG?
**RAG** (Retrieval-Augmented Generation) combina:
     🔍 Recuperación de información relevante desde una base de conocimiento
     🧠 Generación de texto usando un modelo de lenguaje

En lugar de depender solo del conocimiento del modelo, el sistema consulta datos específicos antes de responder.

⚙️ ¿Cómo funciona?
El flujo completo es el siguiente:

    Usuario → Pregunta
            ↓
    Búsqueda semántica (FAISS)
            ↓
    Fragmentos relevantes
            ↓
    LLM (OpenAI)
            ↓
    Respuesta contextualizada

**Paso a paso**
1. 📄 Fuente de datos
     - cafeteria.txt contiene toda la información del negocio
2. ✂️ Chunking (fragmentación)
     - El documento se divide en fragmentos más pequeños
3. 🔢 Embeddings
     - Cada fragmento se convierte en vectores usando un modelo de embeddings
4. 🗂️ Vector Store (FAISS)
     - Los vectores se almacenan localmente para búsqueda rápida
5. 🔎 Retrieval
     - Se buscan los fragmentos más relevantes según la pregunta
6. 🧠 Generación (LLM)
     - El modelo genera una respuesta usando solo esos fragmentos
7. 🚫 Control de alucinaciones
     - Si no hay información relevante → el bot responde que no sabe

🧱 Stack Tecnológico
Componente	                Tecnología
LLM	OpenAI                  (GPT-4o-mini)
Embeddings	                text-embedding-3-small
Vector Store	              FAISS (local)
Framework                  	LangChain
UI	                        Gradio
Deploy	                    Render

🔍 Sobre FAISS (Vector Store)
FAISS (Facebook AI Similarity Search) es el motor que permite la búsqueda semántica.
En este proyecto:
     - Convierte texto en vectores numéricos
     - Permite encontrar similitud entre preguntas y contenido
     - Funciona completamente en local (rápido y sin dependencia externa)

👉 Gracias a FAISS, el chatbot puede encontrar información relevante incluso si la pregunta no coincide exactamente con el texto original.

🔗 Rol de LangChain
LangChain orquesta todo el flujo:
     - Maneja la conexión con el LLM
     - Integra embeddings + vector store
     - Implementa el pipeline RAG
     - Controla el prompt para evitar respuestas fuera de contexto

👉 En este proyecto, utilizo LangChain para demostrar cómo construir una aplicación de IA modular y extensible con pocas líneas de código.

🚀 Deploy en Render

La aplicación está diseñada para desplegarse fácilmente en Render, permitiendo:
     🌐 Acceso público y pruebas vía web 
     ⚡ Backend Python listo para producción
     🔐 Uso de variables de entorno (OPENAI_API_KEY)

💻 Setup rápido (Local)
     '''python -m venv venv
     source venv/bin/activate  # Linux/Mac
     # venv\Scripts\activate   # Windows

     pip install -r requirements.txt
     
     cp .env.example .env
     # Editar .env con tu OPENAI_API_KEY

     python app.py'''
     
🧪 Casos de uso
     🏪 Chatbots para negocios pequeños
     📚 Sistemas de consulta sobre documentos internos
     🧾 FAQs inteligentes
     🧠 Introducción práctica a RAG
     🎯 Objetivo del proyecto

Este proyecto busca demostrar de forma clara:
     - Cómo funciona RAG en la práctica
     - Cómo usar LangChain en un caso real
     - Cómo implementar búsqueda semántica con FAISS
     - Cómo integrar un LLM en una aplicación completa

⚠️ Limitaciones
     - Depende completamente del contenido de cafeteria.txt
     - No incluye persistencia avanzada del vector store
     - No optimizado para grandes volúmenes de datos

🔮 Posibles mejoras
      - Persistencia del índice FAISS
      - Soporte para múltiples documentos
      - UI más avanzada
      - Historial de conversación
      - Evaluación de respuestas (RAG eval)
