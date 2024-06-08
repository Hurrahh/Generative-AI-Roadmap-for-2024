import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

template = "I want you to act as a Q/A chatbot. Now answer the user's question {user_input}"

prompt = PromptTemplate(
    input_variables=['user_input'],
    template=template
    )

chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

st.title("Q/A chat bot")
st.text("\n You can chat with this chatbot")
input_text = st.text_input("")

if input_text:
    st.write(chain.run(input_text))
    

# To run this file Open terminal and type
# streamlit run app.py