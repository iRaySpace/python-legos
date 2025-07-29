import os
import time
import argparse
import soundfile
from openai import OpenAI


def main(text: str):
    output_dir = "out"
    os.makedirs(output_dir, exist_ok=True)

    client = OpenAI()
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text
    ) as response:
        timestamp = int(time.time())
        filename = os.path.join(output_dir, f"{timestamp}.wav")
        response.stream_to_file(filename)
        print(f"Audio saved as {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert text to speech using ChatGPT o4-mini TTS.")
    parser.add_argument("text", type=str, help="The text you want to convert to speech.")    
    args = parser.parse_args()
    main(args.text)
