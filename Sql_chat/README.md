# SQL Data Retriever & Inserter with Google Gemini Integration

## Overview

This project is a **Streamlit Application** that allows users to create tables, insert records, and retrieve data using SQL queries. The app also leverages **Google Gemini (Generative AI)** to automatically convert natural language questions into SQL queries for tasks like retrieving data from a "BOOK" table in an SQLite database.

## Features

- **Create Tables**: Users can create new tables by specifying the table name and column details.
- **Insert Records**: After creating a table, users can input and insert data into the table.
- **Natural Language Processing**: Users can ask questions in plain English, and the app converts these to SQL queries using Google Gemini.
- **Query Data**: Automatically generated SQL queries retrieve data from the SQLite database.
- **View Results**: The app displays the generated SQL queries and their results for user review.
- **User-Friendly Interface**: The application provides a clean, simple layout, making it easy for users to interact with the database.

## Technologies Used

- **Streamlit**: For building the interactive web interface.
- **Google Gemini AI**: For generating SQL queries from user input.
- **SQLite**: For managing and retrieving records.
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

You can view and interact with the Streamlit app  [here](<https://geminibotapp-jxrqfmusjhkfhlctdlcehq.streamlit.app/>).

## Examples
**OUTPUT**:
![image](https://github.com/user-attachments/assets/82275e07-dc0d-4eb5-8105-add85ad06449)
![image](https://github.com/user-attachments/assets/7e7bbaad-3b9b-4b0f-aa26-818e941a626b)
![image](https://github.com/user-attachments/assets/01b6bf47-fac2-476a-a6e2-c8bec3b0cbf4)
![image](https://github.com/user-attachments/assets/8f1e07e4-7cfa-4246-9c1c-24e3aabdf23d)




## Detailed Workflow

### 1. Environment Variable Setup
The application starts by loading environment variables using `dotenv`, which includes configuring the Google API key for accessing the Gemini AI.

### 2. Initialize the Google Gemini Model
The app initializes the Google Gemini AI model using `genai.GenerativeModel('gemini-pro')`. This setup allows the app to convert user input (in natural language) into SQL queries.

### 3. User Input Handling
The app provides input fields for creating tables, inserting records, and asking questions. For questions in natural language, upon clicking the **"Ask the question"** button, the input is processed and sent to the Google Gemini AI model to generate a SQL query.

### 4. Response Generation
The function `get_gemini_response(question, prompt)` sends the user’s question to the Gemini model and retrieves the generated SQL query. The SQL query is then executed against the SQLite database to retrieve the relevant data.

### 5. Display Results
The app displays the generated SQL queries and the results retrieved from the database, allowing users to see the query process and data output.


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
