from core.listener import VoiceListener
from core.speaker import Speaker
from core.brain import FridayBrain


def main():

    listener = VoiceListener()
    speaker = Speaker()
    brain = FridayBrain()

    speaker.speak(
        "Friday is online and ready."
    )

    while True:

        print("\n🎤 Listening...")

        command = listener.listen(
            timeout=None,
            phrase_time_limit=15
        )

        if not command:
            continue

        print(f"👤 You: {command}")

        # Exit commands
        if (
            "exit friday" in command
            or "shutdown friday" in command
            or "goodbye friday" in command
        ):

            speaker.speak(
                "Goodbye. I'll be here when you need me."
            )

            break

        try:

            # Send everything directly to Gemini
            answer = brain.ask(command)

            speaker.speak(answer)

        except Exception as error:

            print(f"❌ AI Error: {error}")

            speaker.speak(
                "Sorry, I couldn't connect to my AI brain."
            )


if __name__ == "__main__":
    main()