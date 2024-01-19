import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os
import tempfile
from . import ssml
from pydantic import BaseModel, Field
from typing import Literal
from dataclasses import dataclass


load_dotenv()
AZURE_SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
AZURE_SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION")


voice_option = Literal["Jenny", "Guy", "Aria", "Davis", "Amber", "Ana", "Andrew", "Ashley", "Brandon", "Brian", "Christopher",
                            "Cora", "Elizabeth", "Emma", "Eric", "Jacob", "Jane", "Jason", "Michelle", "Monica", "Nancy", "Roger", "Sara", "Steffan", "Tony"]
class SynthesizeSpeechArgs(BaseModel):
    voice: voice_option = Field(
        ..., description="Name of the voice model to use.")
    inputText: str

# speech_config.set_property(speechsdk.PropertyId.Speech_LogFilename, "azure_logfile")


def synthesize_speech(message: str, name: str) -> str:
    name = name.capitalize()
    voice = f"en-US-{name}Neural"
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION)
    speech_config.speech_synthesis_voice=voice
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
        audio_config = speechsdk.audio.AudioOutputConfig(filename=temp_file_path)
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        message_ssml = ssml.build_ssml(message=message, voice=voice, style="cheerful")
        speech_synthesizer.speak_ssml(message_ssml)
        temp_file.flush()
        temp_file.close()
    return temp_file_path

def synthesize_speech_to_path(message: str, output_path: str):
    temp_file_path = synthesize_speech(message)
    with open(temp_file_path, "rb") as temp_file:
        with open(output_path, "wb") as permanent_file:
            permanent_file.write(temp_file.read())
