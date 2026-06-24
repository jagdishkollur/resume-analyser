# Resume Analyzer

A Streamlit web app that analyzes resumes using Groq LLM and provides recruiter-style feedback.

## What it does

This project allows users to upload a resume in PDF or TXT format and receive AI-generated analysis.

The app reviews the resume and provides:

- Key strengths
- Weaknesses
- One suggestion to improve the resume

The goal is to help job seekers quickly understand how their resume may look from a recruiter's perspective.

## Tech Stack

- Python
- Streamlit
- Groq API
- python-dotenv
- pypdf

## Live Demo

https://resume-analyser-vmdwrereb4ogrxt6nxkz95.streamlit.app/

## Run Locally

Clone the repository:

```bash
git clone https://github.com/jagdishkollur/resume-analyser.git
cd resume-analyser
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

Start the app:

```bash
streamlit run app.py
```

Open in browser:

```text
http://localhost:8501
```

## Privacy Note

Uploaded resumes are processed in memory during analysis and are not stored or logged by this application.

## Future Improvements

- Resume score out of 100
- Better recruiter prompts
- Support DOCX uploads
- Download analysis as PDF

## What it does
This project allows users to upload a resume in PDF or TXT format and receive AI-generated analysis.
The app reviews the resume and provides:

* Key strengths
* Weaknesses
* One suggestion to improve the resume

The goal is to help job seekers quickly understand how their resume may look from a recruiter's perspective.

The interface uses a custom design (navy/gold color scheme, serif headings) for a polished, professional feel.