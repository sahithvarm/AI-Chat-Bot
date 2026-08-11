import webbrowser
from urllib.parse import quote


def handle_browser_command(command):

    if "open youtube" in command:

        webbrowser.open("https://www.youtube.com")

        return "Opening YouTube."

    if "open google" in command:

        webbrowser.open("https://www.google.com")

        return "Opening Google."

    if command.startswith("search for "):

        query = command.replace(
            "search for ",
            "",
            1
        ).strip()

        if query:

            url = (
                "https://www.google.com/search?q="
                + quote(query)
            )

            webbrowser.open(url)

            return f"Searching Google for {query}."

    if "search youtube for " in command:

        query = command.replace(
            "search youtube for ",
            "",
            1
        ).strip()

        if query:

            url = (
                "https://www.youtube.com/results?search_query="
                + quote(query)
            )

            webbrowser.open(url)

            return f"Searching YouTube for {query}."

    return None