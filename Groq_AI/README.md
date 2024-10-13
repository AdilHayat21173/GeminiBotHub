# Gemma Model Document Q&A

## Overview

This project is an AI-powered **Document Question & Answering System** designed to help users extract information from PDF documents. By uploading PDF files and entering specific questions, the app analyzes the content and provides relevant answers based on the context of the documents.

The system uses **Google Gemini AI** for generating embeddings and responses and is deployed via **Streamlit**. It aims to facilitate easy and efficient access to information contained within documents, particularly for research and academic purposes.

## Features

- **Document Upload**: Load PDF documents for analysis and question answering.
- **Contextual Q&A**: Ask questions related to the document content to receive accurate answers.
- **Document Similarity Search**: Find and display relevant chunks of text from the documents related to the user's questions.

## Technologies Used

- **Streamlit**: For creating the interactive web interface.
- **Google Gemini AI**: For generating intelligent embeddings and responses.
- **Langchain**: For managing document handling and processing.
- **dotenv**: For managing environment variables.

### Usage

- **Upload Documents**: Place your PDF documents in the `./pdf_data` directory.
- **Enter Your Question**: Input a question related to the document content.
- **Get Answer**: Click the "Documents Embedding" button to generate document embeddings, then click to retrieve the answer.

## Streamlit App
You can view and interact with the Streamlit app for document Q&A [here](<your_streamlit_app_link>).

## Examples
Here are some examples of outputs from the model:
![image](https://github.com/user-attachments/assets/4187a6ae-f94d-4c85-b3a2-a56ac12c8dc5)
![image](https://github.com/user-attachments/assets/b6da41aa-493d-4e11-b389-4b3015913ef8)
![image](https://github.com/user-attachments/assets/6bb1a496-dc3e-4bb6-97a2-c856340fb515)




## Acknowledgements
- **Langchain** for providing tools for document processing and embeddings.
- **Google Gemini AI** for enabling advanced embedding capabilities.

## Author
- Adil Hayat
- [Hugging Face Profile](https://huggingface.co/AdilHayat173)
- [GitHub Profile](https://github.com/AdilHayat21173)
- [LinkedIn Profile](https://www.linkedin.com/in/adil-hayat-791ab323a/)

## Feedback
If you have any feedback, please reach out to us at hayatadil300@gmail.com.
