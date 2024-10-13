# YouTube Transcript to Detailed Notes Converter

## Overview

This project is a **YouTube Transcript to Detailed Notes Converter** designed to help users summarize video content effectively. The application leverages **Google Gemini AI** to generate concise summaries of YouTube video transcripts, providing users with important points in an easily digestible format. This tool is particularly useful for educators, students, and content creators who need quick access to video information without watching the entire video.

## Features

- **YouTube Link Input**: Users can input the URL of any YouTube video to retrieve the transcript.
- **Transcript Extraction**: The app extracts the transcript from the specified YouTube video using the YouTube Transcript API.
- **Content Summarization**: Using Google Gemini AI, the app summarizes the transcript into key points within 250 words.
- **Visual Representation**: The app displays a thumbnail image of the YouTube video alongside the generated summary.

## Technologies Used

- **Streamlit**: For creating the interactive web application.
- **Google Gemini AI**: For generating intelligent summaries based on the transcript.
- **YouTube Transcript API**: For retrieving transcripts from YouTube videos.
- **dotenv**: For managing environment variables.

## Usage

1. **Set Up Environment Variables**:
    - Ensure you have your **Google API Key** set up in your environment variables. This is necessary for authenticating with the Google Gemini AI.
    - Use a `.env` file or any other method to store the API key securely.

2. **Run the Streamlit App**:
    - Execute the Streamlit app by running the command: 
      ```bash
      streamlit run app.py
      ```
    - Replace `app.py` with the name of your Python file containing the code.

3. **Interact with the App**:
    - Open the app in your web browser as directed in the terminal.
    - Enter your YouTube video link in the input box provided.
    - Click the **"Get Detailed Notes"** button to retrieve the transcript and generate a summary.

4. **View Summary**:
    - The generated summary will be displayed under the **"Detailed Notes"** section.

## Streamlit App

You can view and interact with the Streamlit app for converting YouTube transcripts to detailed notes [here](<your_streamlit_app_link>).

## Examples

**User Interaction:**
![image](https://github.com/user-attachments/assets/ff2c4804-2412-4ed5-a388-98c595254635)

**Detailed Notes Display:**

![image](https://github.com/user-attachments/assets/168a2016-6ef1-4c27-bc25-271c7496973b)
![image](https://github.com/user-attachments/assets/13a6723f-5f53-4f1d-93c2-32d681cafeb4)


## Detailed Workflow

### 1. Environment Variable Setup
   - The application begins by loading environment variables using `dotenv`, which includes configuring the Google API key needed for accessing the Gemini AI.
   - The line `load_dotenv()` loads all the environment variables specified in the `.env` file.

### 2. Initialize the Gemini AI Model
   - The app initializes the Google Gemini AI model using the `genai.GenerativeModel("gemini-pro")`.

### 3. User Input Handling
   - The app creates an input field where users can type their YouTube video link.
   - Upon clicking the **"Get Detailed Notes"** button, the application processes the input and interacts with the AI model to generate a summary.

### 4. Transcript Extraction
   - The function `extract_transcript_details(youtube_video_url)` extracts the transcript from the provided YouTube link.
   - If the transcript is retrieved successfully, it is passed to the AI model for summarization.

### 5. Response Generation
   - The function `generate_gemini_content(transcript_text, prompt)` sends the transcript text along with a predefined prompt to the Gemini AI model to generate a summary.
   - The summary is then displayed in the application.

### 6. Display Summary
   - The app provides a section displaying the generated summary under the **"Detailed Notes"** heading.

## Acknowledgements

- Google for providing the Gemini AI model.
- YouTube for the transcript API.
- Streamlit for creating the interactive web interface.
- dotenv for managing environment variables securely.

## Author

- Adil Hayat
- [Hugging Face Profile](https://huggingface.co/AdilHayat173)
- [GitHub Profile](https://github.com/AdilHayat21173)
- [LinkedIn Profile](https://www.linkedin.com/in/adil-hayat-791ab323a/)

## Feedback

If you have any feedback, please reach out to us at hayatadil300@gmail.com.
