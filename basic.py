from datetime import datetime


def handle_basic_command(command):

    if "hello" in command or "hi" in command:

        return "Hello! How can I help you?"

    if "how are you" in command:

        return "I'm doing great. Ready to help you."

    if "your name" in command:

        return "My name is Nova. Your personal AI assistant."

    if "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}."

    if "date" in command:

        current_date = datetime.now().strftime("%d %B %Y")

        return f"Today is {current_date}."

    return None