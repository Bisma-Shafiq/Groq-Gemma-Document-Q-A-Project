import os
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv

load_dotenv()

# load groq and google api key from env

groq_api_key=os.getenv("GROQ_API_KEY")
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

st.header("Gemma-Model Document Q&A")


llm = ChatGroq(groq_api_key=groq_api_key,model_name ="Gemma-7b-it")

# Prompt 
prompt = ChatPromptTemplate.from_template(
    """
Answer the question based on provided context only.
Please provide the most accurate response based on question
<context>
{context}
<context>
Questions:{input}

"""
)
# Vector Embedding

def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        st.session_state.loader= PyPDFDirectoryLoader("pdfs")   #ingestion
        st.session_state.doc = st.session_state.loader.load()  # doc loading
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        st.session_state.final_doc = st.session_state.text_splitter.split_documents(st.session_state.doc)
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_doc, st.session_state.embeddings)

prompt1 = st.text_input("What you want to ask from documents?")

if st.button("Click-to-Create vector-store"):
    vector_embedding()
    st.write("Vector Store 'FAISS-DB' is Ready")

import time
if prompt1:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retriever_chain = create_retrieval_chain(retriever,document_chain)

    start = time.process_time()
    response = retriever_chain.invoke({'input':prompt1})
    st.write(response['answer'])

# # gemma gives extra doc
#     with st.expander("Document Similarity Search"): 
#         for i in enumerate(response['context']):
#             st.write(doc.page_content)
#             st.write("-----------------------")