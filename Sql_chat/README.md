# Streamlit SQL Query Retrieval App

## Overview

This project is a **Streamlit Application** designed to allow users to convert English questions into SQL queries and retrieve corresponding data from an SQLite database. By leveraging the **Google Gemini AI** for intelligent query generation, this application provides users with an intuitive interface to interact with database records seamlessly.

## Features

- **Natural Language Processing**: Users can input questions in English, and the app converts these to SQL queries.
- **Data Retrieval**: Retrieves and displays data from the `STUDENT` table in the SQLite database.
- **Real-time Interaction**: Users receive immediate feedback and results based on their queries.
- **User-Friendly Interface**: The app is easy to navigate, with a clean and simple layout.

## Technologies Used

- **Streamlit**: For building the interactive web interface.
- **Google Gemini AI**: For generating SQL queries from user input.
- **SQLite**: For managing and retrieving student records.
- **dotenv**: For securely managing environment variables, including API keys.

## Usage

1. **Set Up Environment Variables**:
    - Ensure you have your **Google API Key** stored in an environment variable.
    - Use a `.env` file or any other method to store the API key securely.

2. **Run the Streamlit App**:
    - Execute the Streamlit app by running the command: 
      ```bash
      streamlit run app.py
      ```
    - Replace `app.py` with the name of your Python file containing the code.

3. **Interact with the App**:
    - Open the app in your web browser as directed in the terminal.
    - Enter your questions in the input box provided.
    - Click the **"Ask the question"** button to receive responses from the AI model.

4. **View Query Results**:
    - The app displays the results based on the generated SQL query, allowing you to see the retrieved records.
## Streamlit App

You can view and interact with the Streamlit app  [here](<your_streamlit_app_link>).

## Examples
**OUTPUT**:
![image](https://github.com/user-attachments/assets/237070db-c475-4b08-ab4e-626de9347c87)
![image](https://github.com/user-attachments/assets/4f4ae1af-85c7-4408-9d52-ac11c5dbcc2b)
![image](https://github.com/user-attachments/assets/5e57ee82-bbee-4f28-a47c-af535ed26f1e)



## Detailed Workflow

### 1. Environment Variable Setup
   - The application begins by loading environment variables using `dotenv`, which includes configuring the Google API key needed for accessing the Gemini AI.

### 2. Initialize the Google Gemini Model
   - The app initializes the Google Gemini AI model using `genai.GenerativeModel('gemini-pro')`.
   - This step sets up a chat session to manage ongoing conversation history.

### 3. User Input Handling
   - The app creates an input field where users can type their questions.
   - Upon clicking the **"Ask the question"** button, the application processes the input and interacts with the AI model to generate a SQL query.

### 4. Response Generation
   - The function `get_gemini_response(question, prompt)` sends the user’s question to the Gemini model and retrieves the SQL command.
   - The SQL command is then executed against the SQLite database to retrieve the relevant data.

### 5. Display Query Results
   - The app displays the retrieved data from the database, allowing users to see the results of their queries.

## Acknowledgements

- Google for providing the Gemini AI model.
- Streamlit for creating the interactive web interface.
- SQLite for managing the database effectively.
- dotenv for managing environment variables securely.

## Author

- Adil Hayat
- [Hugging Face Profile](https://huggingface.co/AdilHayat173)
- [GitHub Profile](https://github.com/AdilHayat21173)
- [LinkedIn Profile](https://www.linkedin.com/in/adil-hayat-791ab323a/)

## Feedback

If you have any feedback, please reach out to us at hayatadil300@gmail.com.
