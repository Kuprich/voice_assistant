from services.faster_whisper import FasterWhisper
from services.local_llm import LocalLLM
from services.silero import Silero


def main():

    stt_service = FasterWhisper()
    text = stt_service.recognize('rec.mp3')

    llm_service = LocalLLM()
    response = llm_service.get_response(text)

    print(response)

    tts_service = Silero()
    tts_service.speak(response)


if __name__ == "__main__":
    main()
