from pydantic import BaseModel, Field
from typing import Optional, Literal
from fastapi import FastAPI, HTTPException
from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()
PORT = int(os.getenv('PORT'))

app = FastAPI()

voice_name_option = Literal["Jenny", "Guy", "Aria", "Davis", "Amber", "Ana", "Andrew", "Ashley", "Brandon", "Brian", "Christopher",
                            "Cora", "Elizabeth", "Emma", "Eric", "Jacob", "Jane", "Jason", "Michelle", "Monica", "Nancy", "Roger", "Sara", "Steffan", "Tony"]


class PredictFileArgs(BaseModel):
    voice_name: voice_name_option = Field(
        ..., description="Name of the voice model to use.")
    inputText: str


class PredictFileResponse(BaseModel):
    deg: str
    mos_pred: float
    noi_pred: Optional[float] = None
    dis_pred: Optional[float] = None
    col_pred: Optional[float] = None
    loud_pred: Optional[float] = None
    model: str


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
    # input_audio_path = "in.wav"
    # output_audio_path = "out.wav"
    # message = speech_to_text.transcribe(input_audio_path)
    # # message = "Give me a couple sentences that describe starring on the hit Nickelodeon T.V. show SpongeBob Squarepants."
    # response = agent.chat(message)
    # text_to_speech.create_synthesized_dialog_to_path(response, output_audio_path)
