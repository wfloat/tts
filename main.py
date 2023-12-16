import speech_to_text
import agent
import text_to_speech


if __name__ == "__main__":
    input_audio_path = "in.wav"
    output_audio_path = "out.wav"
    message = speech_to_text.transcribe(input_audio_path)
    # message = "Give me a couple sentences that describe starring on the hit Nickelodeon T.V. show SpongeBob Squarepants."
    response = agent.chat(message)
    text_to_speech.create_synthesized_dialog_to_path(response, output_audio_path)
    