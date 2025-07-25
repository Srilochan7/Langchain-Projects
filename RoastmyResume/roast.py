import os 
import fitz
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")


def extract_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc :
        text += page.get_text()
    return text


model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
parser = StrOutputParser()

prompt = PromptTemplate(
    template="""
    You are a brutally honest resume critic with Gen Z humor.

    Given this resume text:
    ---
    {text}
    ---

    1. Roast the resume like you're on a comedy stage (but still somewhat helpful).
    2. Give 2-3 savage suggestions like: “Bro add projects that don’t look like tutorial copy-paste,” or “You used 5 buzzwords but zero impact.”
    3. End with one roast that’s so good it hurts.

    Be funny, sarcastic, and helpful. Don’t hold back.
    """,
    input_variables=['text']
    )

def get_roast(text) :
    chain = prompt | model | parser
    
    return chain.invoke({'text': text})

