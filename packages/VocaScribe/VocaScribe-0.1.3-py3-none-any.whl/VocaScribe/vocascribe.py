import argparse
import os
import speech_recognition as sr
from pydub import AudioSegment


def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_file)
    audio.export("temp.wav", format="wav")  # Export to wav format

    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        try:
            # Use Google's free speech recognition
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Speech Recognition could not understand the audio."
        except sr.RequestError as e:
            return (
                f"Could not request results from Google Speech Recognition service; {e}"
            )


def save_transcription(text, output_file_name):
    with open(output_file_name, "w") as file:
        file.write(text)


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe speech from an audio file and save the output to a .txt file."
    )
    parser.add_argument(
        "audio_file", type=str, help="Path to the audio file to process."
    )
    args = parser.parse_args()

    if not os.path.isfile(args.audio_file):
        print(f"Error: The file '{args.audio_file}' does not exist.")
        return

    print("Processing the audio file...")

    transcription = transcribe_audio(args.audio_file)
    output_file_name = os.path.splitext(args.audio_file)[0] + ".txt"
    save_transcription(transcription, output_file_name)

    print(f"\nTranscription saved to {output_file_name}")


if __name__ == "__main__":
    main()
