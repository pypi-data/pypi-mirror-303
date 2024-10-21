from collections import deque
from typing import override

from pyttsx3 import init as init_tts_engine

from trainerbase.logger import logger
from trainerbase.scriptengine import AbstractBaseScript


class TTSManager(AbstractBaseScript):
    def __init__(self, queue_length_limit: int = 5):
        try:
            self.__engine = init_tts_engine()
        except NameError:
            self.__engine = None
            logger.error(
                "Failed to initialize TTS Engine. Installed version of pyttsx3 does not support Python 3.13 yet."
                " Consider using Python 3.12 or continue with Python 3.13 without TTS."
                " Also there is maybe new TrainerBase version with fixed pyttsx3."
            )

        self.__queue = deque(maxlen=queue_length_limit)

    @override
    def __call__(self):
        if not self.__queue:
            return

        try:
            self.__say_sync(*self.__queue[0])
        except RuntimeError:
            return

        self.__queue.popleft()

    def __say_sync(self, text: str, rate: int = 210, volume: float = 1.0):
        if self.__engine is None:
            logger.debug(f"TTS should say: {text}. But TTS Engine is not initialized!")
            return

        self.__engine.setProperty("rate", rate)
        self.__engine.setProperty("volume", volume)
        self.__engine.say(text)
        self.__engine.runAndWait()

    @property
    def queue_length_limit(self):
        return self.__queue.maxlen

    @queue_length_limit.setter
    def queue_length_limit(self, limit: int):
        self.__queue = deque(self.__queue, maxlen=limit)

    def schedule(self, text: str, rate: int = 210, volume: float = 1.0):
        self.__queue.append((text, rate, volume))


tts_manager = TTSManager()
say = say_sync = tts_manager.schedule
