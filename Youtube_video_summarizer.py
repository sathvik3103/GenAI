import streamlit as st
from dotenv import load_dotenv
from google.generativeai import GenerativeModel
import os
import re
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Load all the environment variables
load_dotenv()

# Configure API key for generative AI
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Google API key is not set. Please add it to your .env file.")
    st.stop()

genai.configure(api_key=api_key)

prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here: """

# Getting the transcript data from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = get_video_id(youtube_video_url)
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise RuntimeError("Failed to extract transcript: " + str(e))

# Getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    try:
        # Import GenerativeModel directly
        model = GenerativeModel("models/gemini-pro")  # Model name
        response = model.generate_content( prompt + transcript_text)

        # Let's inspect the response to see its structure
        print("Response:", response)

        # Assuming the response has 'candidates' attribute:
        return response.candidates[0].output if response.candidates else "No content generated"
    except Exception as e:
        raise RuntimeError(f"Failed to generate content: {e}")



# Extract video ID from URL
def get_video_id(youtube_video_url):
    regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.match(regex, youtube_video_url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")

# Streamlit App
st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    try:
        video_id = get_video_id(youtube_link)
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    except ValueError as e:
        st.error(str(e))

if st.button("Get Detailed Notes"):
    try:
        transcript_text = extract_transcript_details(youtube_link)

        if transcript_text:
            summary = generate_gemini_content(transcript_text, prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)
    except Exception as e:
        st.error(str(e))