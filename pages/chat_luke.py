import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
import time
from dotenv import load_dotenv


load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
groq_api_key=os.getenv('GROQ_API_KEY')


st.title("Chat With Luke.")

llm=ChatGroq(groq_api_key=groq_api_key,
             model_name="Llama3-8b-8192")

prompt=ChatPromptTemplate.from_template(
"""
You are Luke, a healthcare expert and wellness coach specializing in holistic health and lifestyle improvement. Your role is to answer any health-related or lifestyle improvement questions with accuracy, empathy, and comprehensive detail.

Use the provided context to craft your answers, ensuring they are as detailed and actionable as possible. If the user asks about a specific topic, include practical tips, evidence-based recommendations, and any relevant insights to guide them toward better health and well-being. Always maintain a positive, encouraging tone while emphasizing holistic and sustainable approaches to wellness. 
<context>
{context}
<context>
Questions:{input}

"""
)

def vector_embedding():
     if "vectors" not in st.session_state:

        st.session_state.embeddings=GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
        st.session_state.loader=PyPDFDirectoryLoader("./data") ## Data Ingestion
        st.session_state.docs=st.session_state.loader.load() ## Document Loading
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200) ## Chunk Creation
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:20]) #splitting
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings) #vector OpenAI embeddings

prompt1=st.text_input("Enter Your Question From Doduments")

# Embedding documents
if st.button("Documents Embedding"):
    vector_embedding()
    st.write("Vector Store DB Is Ready")

if prompt1:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    start = time.process_time()
    response = retrieval_chain.invoke({'input': prompt1})
    print("Response time:", time.process_time() - start)
    st.write(response['answer'])