import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_community.document_loaders import YoutubeLoader

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.0-pro")

prompt = """You are youtube video summarizer. You will be taking the transcript text and 
summarizing the entire video and providing the important points in the summary.Please 
provide the summary of the text given here:
"""


def extract_transcript_details(url):
    try:
        loader = YoutubeLoader.from_youtube_url(
            url, add_video_info=True
        )
        documents = loader.load()
        return "".join([doc.page_content for doc in documents]).strip()
    except Exception as e:
        print(e)


st.title("YouTube Video Summarizer")
youtube_link = st.text_input("Enter Your Video link: ")

if youtube_link:
    st.video()

if st.button("Generate Summary"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        response = model.generate_content(prompt + transcript_text)
        st.markdown("## Detailed Notes: ")
        st.write(response.text)