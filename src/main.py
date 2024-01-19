from pydantic import BaseModel, Field
from typing import Optional, Literal
from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse
from dataclasses import dataclass
from dotenv import load_dotenv
import os
from util.text_to_speech import SynthesizeSpeechArgs, synthesize_speech

load_dotenv()
PORT = int(os.getenv('PORT'))

app = FastAPI()


@app.post("/text_to_speech")
async def text_to_speech(args: SynthesizeSpeechArgs) -> Response:
    # TODO support selecting voice
    file_path = synthesize_speech(args.inputText, args.voice)

    return FileResponse(
        file_path,
        media_type="audio/wav",
        filename="speech.wav",
        headers={"Content-Disposition": "inline; filename=speech.wav"}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
    # input_audio_path = "in.wav"
    # output_audio_path = "out.wav"
    # message = speech_to_text.transcribe(input_audio_path)
    # # message = "Give me a couple sentences that describe starring on the hit Nickelodeon T.V. show SpongeBob Squarepants."
    # response = agent.chat(message)
    # text_to_speech.create_synthesized_speech_to_path(response, output_audio_path)
