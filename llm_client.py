from stt.faster_whisper import FasterWhisper
from tts.silero import Silero


def main():

    # ssml_sample = """Здорова, """
    # tts_service.speak(ssml_sample)

    stt_service = FasterWhisper()
    text = stt_service.recognize('Recording.wav')
    tts_service = Silero()
    tts_service.speak(text)


if __name__ == "__main__":
    main()
