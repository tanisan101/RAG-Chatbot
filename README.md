
---

# RAG-Chatbot: Legal Assistance Chatbot

## Overview

The **RAG-Chatbot** is an AI-powered chatbot designed to provide legal assistance by answering questions related to legal documents. Utilizing Retrieval-Augmented Generation (RAG) techniques, this chatbot processes and understands legal documents to deliver accurate and contextually relevant responses.

## Features

- **Document Ingestion**: Upload and process legal documents (e.g., PDFs) for analysis.
- **Contextual Understanding**: Leverages RAG to comprehend and answer questions based on document content.
- **User-Friendly Interface**: Interact with the chatbot through a conversational UI.
- **Scalability**: Designed to handle a wide range of legal documents and queries.

## Technologies Used

- **Python**: Programming language for backend development.
- **Streamlit**: Framework for building the web interface.
- **Langchain**: Library for document processing and RAG implementation.
- **OpenAI GPT-3.5**: Language model for generating responses.
- **FAISS**: Vector store for efficient similarity search.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tanisan101/RAG-Chatbot.git
   cd RAG-Chatbot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   Create a `.env` file and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. Start the application:

   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to `http://localhost:8501` to interact with the chatbot.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License.

---
