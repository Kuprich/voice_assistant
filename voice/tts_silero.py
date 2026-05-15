# https://github.com/snakers4/silero-models#v5
from dataclasses import dataclass
from pathlib import Path

import torch
import soundfile as sf

from voice import TTSBase

@dataclass
class SileroConfig:
    """Configuration for Silero TTS. All fields are explicit with types and defaults."""
    language: str = 'ru'
    model_id: str = 'v5_5_ru'
    sample_rate: int = 48000
    speaker: str = 'xenia'
    output_file: str = 'output.wav'

    # Text preprocessing flags
    put_accent: bool = True
    put_yo: bool = True
    put_stress_homo: bool = True
    put_yo_homo: bool = True


class TTSSilero(TTSBase):
    MODELS_URL = 'https://raw.githubusercontent.com/snakers4/silero-models/master/models.yml'
    MODELS_FILE = 'latest_silero_models.yml'

    def __init__(self, device: str = 'cpu', **kwargs):
        # Set device (CPU/GPU)
        self.device = torch.device(device)

        # Configuration: defaults from dataclass + overrides via kwargs
        self.config = SileroConfig(**kwargs)

        # Load and initialize the model
        self.model = self._load_model()
        self.model.to(self.device)

    def _load_model(self):
        """Download config and load model via torch.hub."""
        if not Path(self.MODELS_FILE).exists():
            torch.hub.download_url_to_file(
                self.MODELS_URL,
                self.MODELS_FILE,
                progress=False
            )

        model, _ = torch.hub.load(
            repo_or_dir='snakers4/silero-models',
            model='silero_tts',
            language=self.config.language,
            speaker=self.config.model_id
        )
        return model

    def speak(self, text: str) -> None:
        # Call apply_tts with explicit parameters from config
        audio = self.model.apply_tts(
            ssml_text=text,
            speaker=self.config.speaker,
            sample_rate=self.config.sample_rate,
            put_accent=self.config.put_accent,
            put_yo=self.config.put_yo,
            put_stress_homo=self.config.put_stress_homo,
            put_yo_homo=self.config.put_yo_homo,
        )

        # Save to file
        audio_np = audio.detach().cpu().numpy().reshape(-1, 1)
        sf.write(self.config.output_file, audio_np, self.config.sample_rate)

    def stop(self) -> None:
        pass