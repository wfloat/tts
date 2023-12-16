import whisper

model = whisper.load_model("tiny")

def transcribe(audio_file_path):
    result = model.transcribe(audio_file_path)
    return result['text']