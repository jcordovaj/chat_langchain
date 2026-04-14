<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/enoreyes/langchain-gsp-demo.png" />
</div>

# ☕ Chatbot RAG - LangChain – Café Aurora

Demo práctica de LangChain + FAISS + OpenAI

Chatbot inteligente basado en RAG (Retrieval-Augmented Generation) que responde exclusivamente utilizando información interna de un negocio (en este caso, una cafetería).

Este proyecto está diseñado como un ejemplo simple, práctico y educativo para demostrar cómo construir un sistema completo con LangChain, embeddings, búsqueda vectorial y generación con LLM.

## ✨ Overview

El chatbot permite hacer preguntas sobre el negocio Café Aurora y garantiza que:

    ✅ Sólo responde con información contenida en el documento fuente

    ❌ No inventa respuestas fuera del contexto (reduce alucinaciones)

    🤖 Utiliza un pipeline completo de RAG

## 🧠 ¿Qué es RAG?

**RAG** (Retrieval-Augmented Generation) combina:

    🔍 Recuperación de información relevante desde una base de conocimiento

    🧠 Generación de texto usando un modelo de lenguaje

En lugar de depender solo del conocimiento del modelo, el sistema consulta datos específicos antes de responder.

## ⚙️ ¿Cómo funciona?

### El flujo completo es el siguiente:

<pre class="overflow-visible! px-0!" data-start="1553" data-end="1711"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="w-full overflow-x-hidden overflow-y-auto pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>Usuario → Pregunta</span><br/><span>        ↓</span><br/><span>Búsqueda semántica (FAISS)</span><br/><span>        ↓</span><br/><span>Fragmentos relevantes</span><br/><span>        ↓</span><br/><span>LLM (OpenAI)</span><br/><span>        ↓</span><br/><span>Respuesta contextualizada</span></div></div></div></div></div></div></div></div></div></div></div></div></div></pre>

---

### **Paso a paso**

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

## 🧱 Stack Tecnológico

| Componente   | Tecnología             |
| ------------ | ---------------------- |
| LLM          | OpenAI (GPT-4o-mini)   |
| Embeddings   | text-embedding-3-small |
| Vector Store | FAISS (local)          |
| Framework    | LangChain              |
| UI           | Gradio                 |
| Deploy       | Render                 |

---

## 🔍 Sobre FAISS (Vector Store)

FAISS (Facebook AI Similarity Search) es el motor que permite la búsqueda semántica.

En este proyecto:

     - Convierte texto en vectores numéricos
     - Permite encontrar similitud entre preguntas y contenido
     - Funciona completamente en local (rápido y sin dependencia externa)

👉 Gracias a FAISS, el chatbot puede encontrar información relevante incluso si la pregunta no coincide exactamente con el texto original.

## 🔗 Rol de LangChain

LangChain orquesta todo el flujo:

     - Maneja la conexión con el LLM
     - Integra embeddings + vector store
     - Implementa el pipeline RAG
     - Controla el prompt para evitar respuestas fuera de contexto

👉 En este proyecto, utilizo LangChain para demostrar cómo construir una aplicación de IA modular y extensible con pocas líneas de código.

## 🚀 Deploy en Render

La aplicación está diseñada para desplegarse fácilmente en Render, permitiendo:

     🌐 Acceso público y pruebas vía web

     ⚡ Backend Python listo para producción

     🔐 Uso de variables de entorno (OPENAI_API_KEY)

---

## Setup rápido (Local)

<pre class="overflow-visible! px-0!" data-start="3826" data-end="4037"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="w-full overflow-x-hidden overflow-y-auto"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>python </span><span class="ͼf">-m</span><span> venv venv</span><br/><span class="ͼd">source</span><span> venv/bin/activate  </span><span class="ͼ6"># Linux/Mac</span><br/><span class="ͼ6"># venv\Scripts\activate   # Windows</span><br/><br/><span>pip install </span><span class="ͼf">-r</span><span> requirements.txt</span><br/><br/><span class="ͼd">cp</span><span> .env.example .env</span><br/><span class="ͼ6"># Editar .env con tu OPENAI_API_KEY</span><br/><br/><span>python app.py</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 🧪 Casos de uso

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

## ⚠️ Limitaciones

    - Depende completamente del contenido de cafeteria.txt
     - No incluye persistencia avanzada del vector store
     - No optimizado para grandes volúmenes de datos

## 🔮 Posibles mejoras

    - Persistencia del índice FAISS
    - Soporte para múltiples documentos
    - UI más avanzada
    - Historial de conversación
    - Evaluación de respuestas (RAG eval)

---

## 🧭 Things To Do / Roadmap 2.0

Este roadmap extiende el proyecto desde un ejemplo educativo hacia una solución más robusta, escalable y potencialmente comercial.

---

### 🧪 1. Expandir Casos de Uso

La misma base conceptual de este MVP sirve para llevar el chatbot más allá de una "simple" cafetería:

- 🏥 **Salud:** consultas sobre protocolos internos o documentación médica
- 🏢 **Empresas:** asistentes sobre políticas, onboarding y knowledge base
- 🎓 **Educación:** tutor basado en material de estudio
- ⚖️ **Legal:** consulta de contratos o normativas
- 🛍️ **E-commerce:** soporte sobre productos y catálogo

👉 Objetivo: transformar el sistema en un **motor RAG reutilizable por industria** .

---

### 🧠 2. Memoria Conversacional

Actualmente el chatbot es _stateless_, sin embargo, el paso siguiente es hacerlo más natural:

#### Mejoras propuestas:

- 🗂️ **Memoria de corto plazo**
  - Historial de conversación en sesión
  - Uso de `ConversationBufferMemory` en **LangChain**
- 🧩 **Memoria contextual**
  - Resumen automático de conversaciones largas
  - Evitar límite de tokens
- 🧠 **Memoria persistente**
  - Guardado en base de datos (Redis, PostgreSQL)
  - Recuperación de contexto entre sesiones

👉 Resultado: conversaciones más coherentes y personalizadas.

---

### 📚 3. Soporte para Múltiples Fuentes de Datos

Pasar de un `.txt` a un sistema real de conocimiento mantenible:

#### Nuevas fuentes:

📄 PDFs (manuales, reportes)

🌐 URLs (web scraping controlado)

🧾 Bases de datos internas

📂 Documentos (Word, Markdown)

#### Implementación:

- Uso de loaders de **LangChain**
- Pipeline de ingestión:
  - limpieza → chunking → embeddings → indexación

#### Mejoras necesarias:

     🔄 **Re-indexación automática** cuando cambian los documentos

👉 Resultado esperado: **RAG dinámico, mantenible, actualizado y especializado por dominios** .

---

### ⚖️ 4. FAISS vs Vector Databases (Pinecone)

Consideraciones clave para escalar el sistema:

### 🟠 FAISS (actual)

- ✅ Local, rápido y gratuito
- ✅ Ideal para demos y prototipos
- ❌ No escalable horizontalmente
- ❌ Sin persistencia nativa robusta
- ❌ No multiusuario

---

### 🔵 **Pinecone** (alternativa)

- ✅ Base de datos vectorial gestionada (cloud)
- ✅ Escalabilidad automática
- ✅ Alta disponibilidad
- ✅ Búsqueda optimizada en producción
- ✅ Multiusuario
- ❌ Costo asociado
- ❌ Dependencia externa

---

### 🧩 Otras alternativas

- Weaviate
- Chroma
- Milvus

---

### 🎯 Versiones

- 🧪 Demo / laboratorio → FAISS
- 🚀 Producción → Pinecone u otra vector DB

---

### 📈 5. Escalar a Producto Comercial

#### 🏗️ Arquitectura

- Backend desacoplado (FastAPI / Node.js)
- Microservicios:
  - Ingesta de documentos
  - Servicio de embeddings
  - Servicio de consultas RAG
  - API REST / GraphQL

---

### ☁️ Infraestructura

- Deploy en:
  - **Render** (sólo MVP, fase inicial)
  - AWS / GCP / Azure (escala)
- Uso de:
  - Docker
  - CI/CD
  - Auto-scaling

---

### 🔐 Seguridad y control

- Autenticación (JWT, OAuth)
- Control de acceso por usuario
- Aislamiento de datos (multi-tenant)

---

### 💰 Modelo de negocio

- SaaS (Software as a Service):
  - Plan gratuito limitado
  - Pago por uso (tokens / consultas)
  - Plan SaaS por mantenimiento y upgrades
- B2B:
  - Chatbots internos para empresas
  - Integración con CRM / ERP

---

### 📊 Observabilidad

- Logs de consultas
- Evaluación de respuestas (RAG eval)
- Métricas:
  - precisión
  - latencia
  - costo por request

---

### ⚡ Optimización

- Cache de respuestas frecuentes
- Pre-embedding de documentos
- Ranking híbrido (BM25 + vector search)

---

## 🔮 6. Features avanzadas

- 🧾 Generación de respuestas con citas (sources, multi-dominio)
- 📊 Ranking de confianza
- 🗣️ Input por voz/Output por texto (Versión capacidades diferentes e inclusividad)
- 🌍 Multilenguaje (a partir del prompt, detecta lenguaje y responde en el mismo idioma, se mapean terminos locales para evitar malas traducciones)
- 🤖 Agentes (tools + actions)

---

## 🎯 Roadmap

Sem-1 2026: MVP

> 🧪 Demo simple con FAISS

Sem-2 2026: Producción:

> 🚀 Plataforma RAG escalable, multiusuario y lista paZra producción
