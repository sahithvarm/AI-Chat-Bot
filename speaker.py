import pyttsx3


class Speaker:

    def __init__(self):
        self.engine = pyttsx3.init()

        # Speech speed
        self.engine.setProperty("rate", 175)

        # Volume: 0.0 to 1.0
        self.engine.setProperty("volume", 1.0)

        # Select a voice
        voices = self.engine.getProperty("voices")

        if voices:
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, text):

        print(f"🤖 Friday: {text}")

        self.engine.say(text)
        self.engine.runAndWait()