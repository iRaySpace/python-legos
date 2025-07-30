import time
import streamlit as st
from io import BytesIO
from openai import OpenAI
from dotenv import load_dotenv


def _generate_speech(text: str):
    audio_buffer = BytesIO()

    client = OpenAI()
    with st.spinner("Generating speech..."):
        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=text
        ) as response:
            for chunk in response.iter_bytes():
                audio_buffer.write(chunk)
            audio_buffer.seek(0)

    timestamp = int(time.time())
    file_name = f"{timestamp}.wav"

    st.success("Audio generated!")
    st.audio(audio_buffer, format="audio/wav")


def main():
    st.title("Text-to-Speech Generator (GPT‑4o‑mini‑TTS)")
    text_input = st.text_area("Enter text:", height=150)
    if st.button("Generate Speech"):
        text = text_input.strip()
        _generate_speech(text)


if __name__ == "__main__":
    load_dotenv()
    main()
