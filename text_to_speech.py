import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os
import tempfile
from . import ssml

load_dotenv()

AZURE_SPEECH_KEY = os.getenv("AZURE_AZURE_SPEECH_KEY")
AZURE_SPEECH_REGION = os.getenv("AZURE_AZURE_SPEECH_REGION")

voice_name = "en-US-DavisNeural"
speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION)
speech_config.speech_synthesis_voice_name=voice_name
# speech_config.set_property(speechsdk.PropertyId.Speech_LogFilename, "azure_logfile")


def synthesize_dialog(message):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
        audio_config = speechsdk.audio.AudioOutputConfig(filename=temp_file_path)
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        message_ssml = ssml.build_ssml(message=message, voice=voice_name, style="cheerful")
        speech_synthesizer.speak_ssml(message_ssml)
        temp_file.flush()
        temp_file.close()
    return temp_file_path

def create_synthesized_dialog_to_path(message, output_path):
    temp_file_path = synthesize_dialog(message)
    with open(temp_file_path, "rb") as temp_file:
        with open(output_path, "wb") as permanent_file:
            permanent_file.write(temp_file.read())
