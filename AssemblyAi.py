
import assemblyai as aai
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import asyncio

import PDFGenerator

# Replace with your API token
aai.settings.api_key = f"a25224e43fc343ef922375eb280196e4"

async def start_transcription(Audio):
    Video2Text(Audio)


def Video2Text(VideoURL):

    # URL of the file to transcribe
    #FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(VideoURL)

    modified_str = transcript.text.strip("\n")
    #print(modified_str)

    paragraphs = text_separator(modified_str)
    print("Paragraphs: listo")
    print(len(paragraphs))
    PDFGenerator.start_pdf(paragraphs)


def text_separator(text):
    sentences = sent_tokenize(text)
    paragraphs = group_into_paragraphs(sentences, sentences_per_paragraph=20)
    #print(paragraphs)
    return paragraphs

# Define a function to group sentences into paragraphs based on your criteria (e.g., a fixed number of sentences per paragraph).
def group_into_paragraphs(sentences, sentences_per_paragraph=3):
    paragraphs = []
    current_paragraph = []

    for sentence in sentences:
        current_paragraph.append(sentence)
        if len(current_paragraph) == sentences_per_paragraph:
            paragraphs.append(" ".join(current_paragraph))
            current_paragraph = []

    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph))

    return paragraphs



