# import streamlit as st
# import fitz  # PyMuPDF
# import os
# from dotenv import load_dotenv
# from roast import get_roast  # 👈 Make sure roast.py is in the same directory

# # Load environment variables
# load_dotenv()
# API_KEY = os.getenv("GEMINI_API_KEY")

# # Streamlit Page Config
# st.set_page_config(
#     page_title="🔥 Roast My Resume",
#     page_icon="😈",
#     layout="centered"
# )

# # Custom Styles
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
#     html, body, [class*="css"] {
#         font-family: 'Poppins', sans-serif;
#         background-color: #111111;
#         color: #ffffff;
#     }
#     h1, h2 {
#         color: #ff4b2b;
#         text-align: center;
#         text-shadow: 1px 1px #000;
#     }
#     .stButton>button {
#         background: linear-gradient(to right, #ff416c, #ff4b2b);
#         border: none;
#         color: white;
#         padding: 12px 30px;
#         font-size: 18px;
#         border-radius: 12px;
#         font-weight: bold;
#         transition: 0.2s;
#     }
#     .stButton>button:hover {
#         background: linear-gradient(to right, #ff4b2b, #ff416c);
#         transform: scale(1.05);
#     }
#     .box {
#         background-color: #1e1e1e;
#         padding: 25px;
#         border-radius: 15px;
#         box-shadow: 0 0 20px rgba(255, 75, 43, 0.4);
#         margin-top: 20px;
#     }
#     .small-text {
#         text-align: center;
#         font-size: 0.9rem;
#         color: #bbbbbb;
#         margin-bottom: 2rem;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Title
# st.markdown("<h1>🔥 Roast My Resume</h1>", unsafe_allow_html=True)
# st.markdown("<p class='small-text'>Upload your PDF resume. We'll roast it harder than HR after 6 p.m.</p>", unsafe_allow_html=True)

# # File Upload
# uploaded_file = st.file_uploader("📄 Upload your resume (PDF only)", type=["pdf"])

# if uploaded_file:
#     # Extract text
#     doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#     resume_text = ""
#     for page in doc:
#         resume_text += page.get_text()

#     # Show Resume Preview
#     st.markdown("<div class='box'>", unsafe_allow_html=True)
#     st.markdown("### 📝 Resume Preview", unsafe_allow_html=True)
#     st.text_area(" ", resume_text.strip(), height=300, label_visibility="collapsed")
#     st.markdown("</div>", unsafe_allow_html=True)

#     # Roast Button
#     st.markdown("<h3>😈 Ready to get roasted?</h3>", unsafe_allow_html=True)
#     if st.button("🔥 Roast Me"):
#         with st.spinner("Roasting your resume... 🔥"):
#             roast_result = get_roast(resume_text.strip())
#             st.markdown("<div class='box'>", unsafe_allow_html=True)
#             st.markdown("### 🎤 Roast Result", unsafe_allow_html=True)
#             st.write(roast_result)
#             st.markdown("</div>", unsafe_allow_html=True)
# else:
#     st.info("Please upload a PDF to start the roast.")





import streamlit as st
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --- Setup and Function Definitions ---

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the generative model
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash', api_key=API_KEY)
parser = StrOutputParser()

# Define the prompt template
prompt = PromptTemplate(
    template="""
    You are a brutally honest resume critic with a sharp, sarcastic, Gen Z wit. Your goal is to deliver feedback that is equal parts hilarious and indispensable.

    Given this resume text:
    ---
    {text}
    ---

    1.  **The Vibe Check (Roast):** In under 75 words, roast the resume's core identity. Pinpoint its most glaring weakness (e.g., vagueness, buzzword abuse, generic projects) and build the roast around that.

    2.  **Actionable Savagery (Suggestions):** Provide 2-3 brutally direct suggestions. Each one must expose a specific weakness and offer a concrete alternative.
    * Instead of "Quantify your achievements," say "Your resume reads like a list of job duties, not accomplishments. 'Responsible for reports' is not an achievement. 'Automated reports with Python, saving 10 hours per week' is."
    * Instead of "Add projects," say "Delete the 'Calculator App' project. It screams 'I just finished chapter 3 of a coding bootcamp.' Add a project that solves a unique problem, not one that every other applicant has."

    3.  **The Coup de Grâce (Final Roast):** Deliver one final, piercing roast that summarizes the resume's fatal flaw so perfectly it hurts.
    """,
    input_variables=['text']
)

def get_roast(text: str) -> str:
    """Invokes the LangChain chain to get the resume roast."""
    chain = prompt | model | parser
    return chain.invoke({'text': text})

# --- Streamlit App UI ---

# Page Configuration
st.set_page_config(
    page_title="🔥 Roast My Resume",
    page_icon="😈",
    layout="centered"
)

# Custom Styles
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-color: #111111;
        color: #ffffff;
    }
    h1, h2 {
        color: #ff4b2b;
        text-align: center;
        text-shadow: 1px 1px #000;
    }
    .stButton>button {
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        border: none;
        color: white;
        padding: 12px 30px;
        font-size: 18px;
        border-radius: 12px;
        font-weight: bold;
        transition: 0.2s;
        display: block;
        margin: 0 auto;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #ff4b2b, #ff416c);
        transform: scale(1.05);
    }
    .box {
        background-color: #1e1e1e;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(255, 75, 43, 0.4);
        margin-top: 20px;
    }
    .small-text {
        text-align: center;
        font-size: 0.9rem;
        color: #bbbbbb;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Subtitle
st.markdown("<h1>🔥 Roast My Resume</h1>", unsafe_allow_html=True)
st.markdown("<p class='small-text'>Upload your PDF. We'll roast it harder than HR after 6 p.m.</p>", unsafe_allow_html=True)

# File Uploader
uploaded_file = st.file_uploader("📄 Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    # Extract text from the uploaded PDF
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    resume_text = ""
    for page in doc:
        resume_text += page.get_text()
    doc.close()

    # Show Resume Preview
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("### 📝 Resume Preview", unsafe_allow_html=True)
    st.text_area(" ", resume_text.strip(), height=300, label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

    # Roast Button
    st.markdown("<h3 style='text-align: center; margin-top: 2rem;'>😈 Ready to get roasted?</h3>", unsafe_allow_html=True)
    if st.button("🔥 Roast Me"):
        with st.spinner("Cooking up a fresh roast... 🔥"):
            roast_result = get_roast(resume_text.strip())
            st.markdown("<div class='box'>", unsafe_allow_html=True)
            st.markdown("### 🎤 The Roast", unsafe_allow_html=True)
            st.write(roast_result)
            st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("Please upload a PDF to start the roast.")