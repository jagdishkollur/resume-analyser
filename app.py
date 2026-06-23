import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader
import os

load_dotenv(".env")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.title("Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["txt", "pdf"]
)

if st.button("Analyze Resume"):

    if uploaded_file is not None:

        with st.spinner("Analyzing resume..."):

            filename = uploaded_file.name

            if filename.endswith(".txt"):
                resume = uploaded_file.read().decode("utf-8")

            elif filename.endswith(".pdf"):
                pdf = PdfReader(uploaded_file)

                resume = ""

                for page in pdf.pages:
                    page_text = page.extract_text()

                    if page_text:
                        resume += page_text

            else:
                st.error("Unsupported file format")
                st.stop()

            prompt = f"""
Act as a recruiter.

Analyse this resume and provide:

1. Key strengths
2. Weaknesses
3. One suggestion to improve it

Resume:
{resume}
"""

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.subheader("Analysis")
        st.write(response.choices[0].message.content)

    else:
        st.warning("Please upload a file first.")