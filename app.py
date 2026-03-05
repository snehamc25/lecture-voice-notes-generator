import streamlit as st
import speech_recognition as sr

st.title("Lecture Voice to Notes Generator")

st.write("Upload lecture audio to convert speech into text notes")

audio_file = st.file_uploader("Upload Audio File", type=["wav"])

if audio_file is not None:
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)

        st.subheader("Generated Notes:")
        st.write(text)

    except:
        st.write("Could not understand the audio")