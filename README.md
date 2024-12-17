# Gemma-Model Document Q&A

This project leverages **Groq's Gemma-7B-IT Model**, **Google Generative AI Embeddings**, and the **LangChain** framework to create a dynamic question-answering application for PDF documents. Users can interact with uploaded documents by asking context-based questions and receiving accurate, detailed responses.

---


<video controls src="gemma with groq.mp4" title="Title"></video>


---

## Features

1. **Context-Aware Q&A**: Ask questions from PDF files, and receive precise answers based only on the document context.
2. **Automated Vector Store Creation**: Process and embed PDF content into a **FAISS** vector store for efficient similarity search.
3. **Streamlit User Interface**: Simple and intuitive interface for uploading PDFs, generating embeddings, and querying documents.

---

## Tools & Technologies

### Core Tools:
- **Groq API**: Utilized the powerful **Gemma-7B-IT** language model for Q&A.
- **Google Generative AI Embeddings**: Converts document content into vector embeddings for similarity search.
- **LangChain**: Orchestrates the document retrieval and LLM-based response generation.
- **FAISS**: Vector store for efficient document similarity search.

### Python Libraries:
- `streamlit`: For building the interactive user interface.
- `PyPDFDirectoryLoader`: Efficiently loads and processes PDF files.
- `langchain`: Facilitates chaining prompts, LLMs, and retrieval mechanisms.
- `langchain_community`: Community tools for document processing.
- `langchain_groq`: Integration for Groq models.
- `dotenv`: For managing environment variables securely.

---

## Installation & Setup

Follow the steps below to set up and run the project:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up Virtual Environment (Optional)**:
   ```bash
   python -m venv env
   source env/bin/activate   # For Linux/Mac
   env\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add API Keys**:
   - Create a `.env` file in the project root directory.
   - Add your Groq and Google Generative AI API keys:
     ```env
     GROQ_API_KEY=your_groq_api_key_here
     GOOGLE_API_KEY=your_google_api_key_here
     ```

5. **Prepare PDF Directory**:
   - Place the PDF files you want to process in a folder named `pdfs` at the project root.

---

## Usage

1. **Run the Streamlit Application**:
   ```bash
   streamlit run app.py
   ```

2. **Upload and Process PDFs**:
   - On the sidebar, upload PDF files into the `pdfs` directory.
   - Click the **"Click-to-Create vector-store"** button to process the documents and create the FAISS vector store.

3. **Ask Questions**:
   - Enter your query in the text box.
   - The application will return context-based answers extracted from the documents.

---

## Example Interaction

**User Input:**
```
What is the main topic of the document?
```

**Response:**
```
The document discusses the impact of climate change on global agriculture, highlighting challenges and potential solutions.
```

---

## Project Structure
```
.
├── app.py                     # Main Streamlit app
├── pdfs/                      # Folder to store PDF documents
├── .env                       # Environment file for API keys
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── ...                        # Other supporting files
```

---

## How It Works

1. **Document Processing**:
   - PDFs are loaded using `PyPDFDirectoryLoader`.
   - Text is split into manageable chunks using `RecursiveCharacterTextSplitter`.
   - Chunks are embedded into vectors using **Google Generative AI Embeddings**.

2. **Vector Store Creation**:
   - FAISS stores the vectorized chunks for efficient similarity search.

3. **Q&A Retrieval Chain**:
   - A user question triggers a retrieval of relevant document chunks.
   - The Groq **Gemma-7B-IT** model generates answers based on the retrieved context.

4. **Streamlit Interface**:
   - Provides an easy-to-use platform for document upload, processing, and querying.

---

## Requirements
- Python 3.8+
- Valid API keys for **Groq** and **Google Generative AI**.
- Streamlit for running the web interface.

---

## Author
**Bisma Shafiq**  
Connect with me on [LinkedIn](https://www.linkedin.com/in/bisma-shafiq-3a3b31242/)

---

## Contributing
Feel free to contribute to the project by submitting issues or pull requests. Any suggestions for improving functionality or features are welcome!

---

## Acknowledgments
- **Groq AI** for providing the Gemma-7B-IT model.
- **Google Generative AI** for its powerful embeddings.
- **LangChain** for enabling seamless integration of LLMs and vector search tools.


