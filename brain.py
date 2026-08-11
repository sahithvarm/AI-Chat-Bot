import os
from google import genai


class FridayBrain:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is not set."
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = "gemini-3.5-flash-lite"

        self.system_prompt = """
You are Friday, a helpful personal AI voice assistant.

Your response will be spoken aloud using text-to-speech.

Rules:
- Be helpful and natural.
- Keep answers concise unless the user asks for detail.
- Do not use unnecessary markdown.
- Never claim you performed an action unless it actually happened.
"""

    def ask(self, user_message):

        response = self.client.models.generate_content(
            model=self.model,
            contents=(
                self.system_prompt
                + "\n\nUser: "
                + user_message
            )
        )

        return response.text