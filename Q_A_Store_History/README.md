# Chat with Gemini LLM

## Overview

This project is a **Chat Application** designed to allow users to interact with the **Google Gemini AI** for generating intelligent responses based on user queries. Using **Streamlit** for the web interface, the application enables real-time Q&A sessions, providing users with an engaging conversational experience.

The app is particularly useful for individuals looking to obtain information quickly and efficiently through conversational interaction.

## Features

- **User Input**: Users can enter questions and receive responses in real-time.
- **Chat History**: The app maintains a chat history, allowing users to review previous interactions.
- **Dynamic Responses**: Users receive detailed responses from the Google Gemini AI model based on their queries.
- **Easy-to-Use Interface**: A simple and intuitive interface for seamless interaction.

## Technologies Used

- **Streamlit**: For creating the interactive web interface.
- **Google Gemini AI**: For generating intelligent responses and understanding context.
- **dotenv**: For managing environment variables, specifically for API keys.

## Usage

1. **Set Up Environment Variables**:
    - Ensure you have your **Google API Key** set up in your environment variables. This is necessary for authenticating with the Google Gemini AI.
    - Use a `.env` file or any other method to store the API key securely.

2. **Run the Streamlit App**:
    - Execute the Streamlit app by running the command: 
      ```bash
      streamlit run qchat.py
      ```
    - Replace `qchat.py` with the name of your Python file containing the code.

3. **Interact with the App**:
    - Open the app in your web browser as directed in the terminal.
    - Enter your questions in the input box provided.
    - Click the **"Ask the question"** button to receive responses from the AI model.

4. **View Chat History**:
    - The app displays the conversation history, allowing you to see both your queries and the bot's responses.

## Streamlit App

You can view and interact with the Streamlit app for chatting with Gemini [here](<your_streamlit_app_link>).

## Examples

**User Interaction:**
![image](https://github.com/user-attachments/assets/fbb1d5ce-7e7a-43fc-9d1c-4533cfda7fdc)


**Chat History Display:**
![image](https://github.com/user-attachments/assets/460d6bcb-1a6e-4a17-ac01-6bdd27440267)


## Detailed Workflow

### 1. Environment Variable Setup
   - The application begins by loading environment variables using `dotenv`, which includes configuring the Google API key needed for accessing the Gemini AI.
   - The line `load_dotenv()` loads all the environment variables specified in the `.env` file.

### 2. Initialize the Gemini AI Model
   - The app initializes the Google Gemini AI model using the `genai.GenerativeModel("gemini-pro")`.
   - A chat session is started, allowing for ongoing conversation history management.

### 3. User Input Handling
   - The app creates an input field where users can type their questions.
   - Upon clicking the **"Ask the question"** button, the application processes the input and interacts with the AI model to get a response.

### 4. Response Generation
   - The function `get_gemini_response(question)` sends the user’s question to the Gemini model and retrieves the response.
   - The responses are displayed in the application, and both user queries and bot responses are stored in the session state for chat history tracking.

### 5. Display Chat History
   - The app provides a section displaying the entire chat history, allowing users to review their interactions.

## Acknowledgements

- Google for providing the Gemini AI model.
- Streamlit for creating the interactive web interface.
- dotenv for managing environment variables securely.

## Author

- Adil Hayat
- [Hugging Face Profile](https://huggingface.co/AdilHayat173)
- [GitHub Profile](https://github.com/AdilHayat21173)
- [LinkedIn Profile](https://www.linkedin.com/in/adil-hayat-791ab323a/)

## Feedback

If you have any feedback, please reach out to us at hayatadil300@gmail.com.
