from faster_whisper import WhisperModel

class FasterWhisper:

    def __init__(self, model_size: str = 'medium', device: str = 'cpu'):
        self.model = WhisperModel(model_size, device=device, compute_type="float32")

    def recognize(self, audio_path: str) -> str:
        segments, info = self.model.transcribe(audio_path, beam_size=5)
        print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
        segments_list = list(segments)
        for segment in segments_list:
            print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        return "".join([i.text for i in segments_list])
