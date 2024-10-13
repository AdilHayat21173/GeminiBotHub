# MultiLanguage Invoice Extractor

## Overview

The **MultiLanguage Invoice Extractor** is an AI-powered application designed to extract information from invoice images. It utilizes the **Google Gemini AI** for understanding and processing invoices in multiple languages. Users can upload images of invoices and receive detailed insights and answers based on the content of the uploaded images.

## Technologies Used

- **Streamlit**: For creating the interactive web interface.
- **Google Gemini AI**: For processing the invoice images and generating responses.
- **Pillow (PIL)**: For handling image uploads and processing.

## Installation

### Prerequisites

Ensure you have Python installed on your system. It is recommended to create a virtual environment for this project.

### Steps to Install

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

   Create a `.env` file in the root of the project and add your Google API key:

    ```makefile
    GOOGLE_API_KEY=your_google_api_key
    ```
## Streamlit App

You can view and interact with the Streamlit app for multi-language invoice extraction [here](<your_streamlit_app_link>).


## Usage

1. **Input Prompt**: Enter a specific prompt or question related to the invoice.
2. **Upload Invoice Image**: Choose an invoice image file in JPG, JPEG, or PNG format.
3. **Submit**: Click the "Tell me about the invoice" button to get insights based on the uploaded invoice.

### Example Input

- **Input Prompt**: 
![input](https://github.com/user-attachments/assets/dc89f0c6-af68-4609-b589-a056372701c8)
- **Uploaded Image**: 
![data](https://github.com/user-attachments/assets/0a989fe8-7b07-4507-af11-e41dd41391a3)

### Example Output

- **Response**: 
![Output](https://github.com/user-attachments/assets/a8144e88-c7e8-4605-86dd-02e93fcd0223)

## How It Works

- **Image Upload**: The application allows users to upload an invoice image.
- **Image Processing**: The uploaded image is processed, and its details are sent to the Google Gemini model.
- **Response Generation**: The model generates a response based on the content of the invoice, which is displayed to the user.

## Acknowledgements

- **Google Gemini AI**: For providing powerful generative AI capabilities.
- **Streamlit**: For enabling the development of interactive web applications.

## Author

- Adil Hayat
- [Hugging Face Profile](https://huggingface.co/AdilHayat173)
- [GitHub Profile](https://github.com/AdilHayat21173)
- [LinkedIn Profile](https://www.linkedin.com/in/adil-hayat-791ab323a/)

## Feedback

If you have any feedback or suggestions, please reach out at [hayatadil300@gmail.com](mailto:hayatadil300@gmail.com).
