from abc import ABC, abstractmethod

# Text To Speach contract
class TTSBase(ABC):
    @abstractmethod
    def speak(self, text:str) -> None:
        """Озвучить текст"""
        pass

    @abstractmethod
    def stop(self) -> None:
        """Принудительно остановить озвучку"""
        pass