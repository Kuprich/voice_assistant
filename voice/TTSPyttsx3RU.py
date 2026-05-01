# Реализация контракта TTSBase
from voice.TTSBase import TTSBase


class TTSPyttsx3RU(TTSBase):
    def speak(self, text: str) -> None:
        pass

    def stop(self) -> None:
        pass

def create_tts() -> TTSBase:
    pass