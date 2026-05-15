from voice.tts_silero import TTSSilero


def main():
    tts_service = TTSSilero()

    ssml_sample = """
                  <speak>
                  <p>
                      Когда я просыпаюсь, <prosody rate="x-slow">я говорю довольно медленно</prosody>.
                      Пот+ом я начинаю говорить своим обычным голосом,
                      <prosody pitch="x-high"> а могу говорить тоном выше </prosody>,
                      или <prosody pitch="x-low">наоборот, ниже</prosody>.
                      Пот+ом, если повезет – <prosody rate="fast">я могу говорить и довольно быстро.</prosody>
                      А еще я умею делать паузы любой длины, например, две секунды <break time="2000ms"/>.
                      <p>
                        Также я умею делать паузы между параграфами.
                      </p>
                      <p>
                        <s>И также я умею делать паузы между предложениями</s>
                        <s>Вот например как сейчас</s>
                      </p>
                  </p>
                  </speak>
                  """

    tts_service.speak(ssml_sample)


if __name__ == "__main__":
    main()
