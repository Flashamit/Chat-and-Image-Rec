#Chat with Luke: 
An AI-Powered Wellness Chatbot
Chat with Luke is an AI-powered chatbot designed to assist users with health and wellness-related queries. Built using cutting-edge AI technologies, it leverages document embeddings, vector similarity search, and large language models to provide detailed, accurate, and empathetic responses to user questions.


#Features
Holistic Health Guidance: Acts as a virtual wellness coach, answering questions with accuracy and empathy.
Document Embedding: Supports document ingestion, chunking, and embedding for efficient retrieval.
Interactive Query Handling: Allows users to ask questions based on uploaded PDF documents.
Powered by Advanced AI Models: Utilizes ChatGroq, Google Generative AI Embeddings, and FAISS for seamless performance.


#Technologies Used
Python: Core language for implementation.
Streamlit: For building the interactive web application.
LangChain: For managing LLM integrations, document processing, and retrieval chains.
Google Generative AI: Provides embeddings for document vectors.
FAISS: For vector-based document retrieval.
ChatGroq: The underlying large language model for generating responses.
PyPDFDirectoryLoader: For loading PDF documents.


#Setup Instructions
1. Clone the Repositorybash
git clone  
cd chat-with-luke

2. Install Dependencies
Use pip to install required libraries.
bash
Copy code
pip install -r requirements.txt

3. Set Environment Variables
Create a .env file and add your API keys:

makefile
Copy code
GOOGLE_API_KEY=your-google-api-key
GROQ_API_KEY=your-groq-api-key

4. Prepare Data
Add your PDF documents to the data/ directory for ingestion.

5. Run the Application
bash
Copy code
streamlit run main.py


#Environment Variables
Make sure to configure the following variables in the .env file:

GOOGLE_API_KEY: API key for Google Generative AI.
GROQ_API_KEY: API key for ChatGroq.
