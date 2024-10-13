# Chat with PDF using Gemini

## Overview

This project is a **Chat PDF application** designed to empower users to upload PDF documents and engage in a Q&A session based on the document's content. Leveraging **Google Gemini AI** for natural language understanding and **LangChain** for vector storage and question answering, the app allows users to extract and interact with information seamlessly.

The system is particularly useful for individuals needing to quickly access and understand information within multiple documents.

## Features

- **PDF Upload**: Users can upload multiple PDF files for analysis through the sidebar.
- **Document Processing**: The app extracts text from uploaded PDFs, splits the text into manageable chunks, and stores the embeddings in a FAISS vector store for efficient searching.
- **Question Answering**: Users can ask specific questions about the uploaded PDFs, receiving accurate answers based on the extracted content.
- **Contextual Responses**: The app provides detailed and contextual answers to user queries.

## Technologies Used

- **Streamlit**: For creating the interactive web interface.
- **Google Gemini AI**: For generating intelligent responses and understanding context.
- **PyPDF2**: For extracting text from uploaded PDF documents.
- **LangChain**: For handling vector storage (FAISS) and implementing question-answering chains.
- **dotenv**: For managing environment variables.

## Usage

1. **Upload PDF Documents**:
    - Open the app, and in the sidebar, locate the PDF upload section.
    - Use the file uploader to select and upload multiple PDF files.
    - Click on the **"Submit & Process"** button to begin analyzing the documents.

2. **Document Processing**:
    - Upon clicking the submit button, the app reads the uploaded PDFs, extracts the text content, and splits the text into manageable chunks.
    - These text chunks are then embedded using Google Gemini AI embeddings.
    - The embeddings are stored in a FAISS vector store for quick retrieval.

3. **Ask Questions**:
    - After processing, you can enter your question in the **"Ask a Question from the PDF Files"** input box.
    - The app uses the stored vector embeddings to find relevant text chunks and generate a response based on your question.

4. **View Responses**:
    - The app will display the response generated from the context of the uploaded documents below the question input.

## Streamlit App

You can view and interact with the Streamlit app for chatting with PDFs [here](<your_streamlit_app_link>).

## Examples

**Upload_Data and Q_A:**
![image](https://github.com/user-attachments/assets/422683ae-3a3f-44d0-ac9e-4b658acc5b65)
![image](https://github.com/user-attachments/assets/73a1cf58-743d-4f5f-9406-0d15cee686cc)


## Detailed Workflow

### 1. PDF Upload and Processing
   - The user uploads PDFs through the sidebar.
   - When the user clicks **"Submit & Process"**, the following occurs:
     - The text is extracted from each page of the PDFs.
     - The extracted text is split into chunks using a `RecursiveCharacterTextSplitter`.
     - The text chunks are embedded using Google Gemini AI embeddings.
     - These embeddings are stored in a FAISS vector store, allowing for quick retrieval during question answering.

### 2. Question Answering
   - When a user enters a question and submits it, the app performs the following:
     - It loads the FAISS vector store to find the most relevant document chunks based on the user's query.
     - A conversational chain is created with a prompt template that guides the model to answer questions based on the provided context.
     - The model generates a response that is displayed to the user.

## Acknowledgements

- Hugging Face for transformer models and libraries.
- Streamlit for creating the interactive web interface.
- LangChain for enabling vector storage and question-answering capabilities.


## Author

- Adil Hayat
- [Hugging Face Profile](https://huggingface.co/AdilHayat173)
- [GitHub Profile](https://github.com/AdilHayat21173)
- [LinkedIn Profile](https://www.linkedin.com/in/adil-hayat-791ab323a/)

## Feedback

If you have any feedback, please reach out to us at hayatadil300@gmail.com.
