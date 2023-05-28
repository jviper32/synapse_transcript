from deepgram import Deepgram
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')

AUDIO = input("Enter audo file location: ")
FILE = input("Enter text file name: ")
PATH = input("Enter file save location: ")

async def main():
    print ("Working")
    deepgram = Deepgram(DEEPGRAM_API_KEY)

    with open(AUDIO, 'rb') as audio:
        source = { 'buffer': audio, 'mimetype': 'audio/mp3' }

        transcription_options = { 'punctuate': True, 'diarize': True, 'paragraphs': True }
        response = await deepgram.transcription.prerecorded(source, transcription_options)

        transcript = response['results']['channels'][0]['alternatives'][0]['paragraphs']['transcript']

        completeName = os.path.join(PATH, FILE+".txt")

        with open(completeName, 'w') as f:
            f.write(transcript)

if __name__ == '__main__':
    asyncio.run(main())