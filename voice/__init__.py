from abc import ABC, abstractmethod

class TTSBase(ABC):
    @abstractmethod
    def speak(self, text: str) -> None:
        """Convert text to speech and play it. Blocks until finished."""
        pass

    @abstractmethod
    def stop(self) -> None:
        """Forcefully stop playback."""
        pass