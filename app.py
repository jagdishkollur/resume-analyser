import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader
import os

load_dotenv(".env")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📋",
    layout="centered"
)

# ---- Custom styling ----
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Lora:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');

    .stApp {
        background-color: #FAF8F5;
    }

    h1 {
        font-family: 'Lora', serif !important;
        color: #1A2332 !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
    }

    .subtitle {
        font-family: 'Inter', sans-serif;
        color: #5A5A5A;
        font-size: 1rem;
        margin-top: -10px;
        margin-bottom: 30px;
    }

    .stButton button {
        background-color: #1A2332 !important;
        color: #FAF8F5 !important;
        border: none !important;
        border-radius: 4px !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        padding: 0.6rem 1.5rem !important;
        transition: background-color 0.2s ease;
    }

    .stButton button:hover {
        background-color: #C9A227 !important;
        color: #1A2332 !important;
    }

    [data-testid="stFileUploader"] {
        border: 1.5px dashed #1A2332;
        border-radius: 6px;
        padding: 10px;
        background-color: #FFFFFF;
    }

    h3 {
        font-family: 'Lora', serif !important;
        color: #1A2332 !important;
        border-bottom: 2px solid #C9A227;
        padding-bottom: 6px;
        margin-top: 30px !important;
    }

    .analysis-box {
        background-color: #FFFFFF;
        border-left: 4px solid #C9A227;
        padding: 20px 24px;
        border-radius: 4px;
        font-family: 'Inter', sans-serif;
        line-height: 1.7;
        color: #2A2A2A;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-left: 4px solid #C9A227 !important;
        border-top: none !important;
        border-right: none !important;
        border-bottom: none !important;
        border-radius: 4px !important;
        background-color: #FFFFFF;
    }

    [data-testid="stVerticalBlockBorderWrapper"] p,
    [data-testid="stVerticalBlockBorderWrapper"] li {
        font-family: 'Inter', sans-serif;
        line-height: 1.7;
        color: #2A2A2A;
    }

    .footer-note {
        font-family: 'Inter', sans-serif;
        font-size: 0.8rem;
        color: #999999;
        text-align: center;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# ---- Header ----
st.title("Resume Analyzer")
st.markdown('<p class="subtitle">Get instant, recruiter-style feedback on your resume — powered by AI.</p>', unsafe_allow_html=True)

# ---- Upload ----
uploaded_file = st.file_uploader(
    "Upload your resume (PDF or TXT)",
    type=["txt", "pdf"]
)

if st.button("Analyze Resume"):

    if uploaded_file is not None:

        with st.spinner("Analyzing your resume..."):

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
                    {"role": "user", "content": prompt}
                ]
            )

        st.markdown("### Analysis")
        with st.container(border=True):
            st.markdown(response.choices[0].message.content)

    else:
        st.warning("Please upload a file first.")

st.markdown('<p class="footer-note">Your resume is processed in-memory and is not stored or logged.</p>', unsafe_allow_html=True)