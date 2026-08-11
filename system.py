import os


def handle_system_command(command):

    if "open calculator" in command:

        os.system("start calc")

        return "Opening calculator."

    if "open notepad" in command:

        os.system("start notepad")

        return "Opening Notepad."

    if "open command prompt" in command:

        os.system("start cmd")

        return "Opening Command Prompt."

    return None