# Chatbot RAG - Café Aurora

Chatbot inteligente que responde SOLO con información del documento del negocio.
Usa RAG (Retrieval Augmented Generation) con LangChain, FAISS y OpenAI.

## Setup rápido

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

pip install -r requirements.txt

cp .env.example .env
# Editar .env con tu OPENAI_API_KEY

python app.py
```

## ¿Cómo funciona?

1. `cafeteria.txt` contiene toda la información del negocio
2. Al iniciar, el documento se divide en fragmentos y se indexa con FAISS
3. Cuando el usuario pregunta, se buscan los fragmentos más relevantes
4. El modelo genera una respuesta usando SOLO esos fragmentos
5. Si la info no está en el documento, el bot dice que no sabe

## Stack

| Componente | Tecnología |
|-----------|-----------|
| LLM | OpenAI GPT-4o-mini |
| Embeddings | text-embedding-3-small |
| Vector Store | FAISS (local) |
| Framework | LangChain |
| UI | Gradio |
