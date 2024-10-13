# Smart ATS for CV

## Overview

This project is an AI-powered **Applicant Tracking System (ATS)** designed to help job seekers enhance their resumes. By uploading a resume in PDF format and providing a job description, the app analyzes the resume, offers professional evaluation, provides constructive tips to improve the resume, and calculates the percentage match between the resume and the job description.

The system uses **Google Gemini AI** for generating responses and is deployed via **Streamlit**. It's tailored to help individuals optimize their resumes for better ATS compatibility, particularly for data science roles.

## Features

- **Job Description Analysis**: Paste a job description and upload a resume to get detailed feedback.
- **Resume Tips**: Get actionable suggestions to improve your resume’s ATS compatibility.
- **Match Percentage**: Receive a percentage match between the resume and the job description, along with key missing keywords.

## Technologies Used

- **Streamlit**: For creating the interactive web interface.
- **Google Gemini AI**: For generating intelligent responses.
- **PyPDF2**: For extracting text from uploaded PDF resumes.
- **dotenv**: For managing environment variables.
### Usage

- **Upload Resume**: Upload your resume in PDF format.
- **Paste Job Description**: Provide the job description for the role you're applying for.
- **Get Feedback**: Click on one of the buttons to:
  - **Review Resume**: Get a detailed evaluation of how well your resume fits the job.
  - **Improve Resume**: Receive specific tips to enhance your resume for better ATS results.
  - **Match Percentage**: See the percentage match between your resume and the job description, with a breakdown of missing keywords.


## Streamlit App
You can view and interact with the Streamlit app for token classification [here]().
## Examples
Here are some examples of outputs from the model:

**Improve Resume**
![tips](https://github.com/user-attachments/assets/d1b9bbb5-7ea4-4c0c-9c1d-dae8e3cedda7)
![tip](https://github.com/user-attachments/assets/de76097f-fc99-4768-b3b6-4654f0ffc216)
![tips](https://github.com/user-attachments/assets/08388cd5-3139-4125-bc13-a1fc522dd0fb)
**Match Percentage**:
![percentage](https://github.com/user-attachments/assets/888259ba-435e-467c-a98c-41908ac66f76)

## Acknowledgements
- Hugging Face for transformer models and libraries.
- Streamlit for creating the interactive web interface.
- [Your Dataset Provider] for the token classification dataset.

## Author
- AdilHayat
- [Hugging Face Profile](https://huggingface.co/AdilHayat173)
- [GitHub Profile](https://github.com/AdilHayat21173)

## Feedback
If you have any feedback, please reach out to us at hayatadil300@gmail.com.