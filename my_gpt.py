import os
import requests
import json

class ChatSession:
    def __init__(self):
        self.messages = []

    def add_message(self, role, content):
        message = {"role": role, "content": content}
        self.messages.append(message)

    def count_tokens(self, text):
        return len(text)

    def ask_gpt3(self, prompt):
        self.add_message("user", prompt)
        max_tokens = 4096
        message_text = "".join([m["content"] for m in self.messages])

        while self.count_tokens(message_text) > (max_tokens - 100):  # Reserve tokens for GPT-3 response and role labels
            self.messages.pop(0)
            message_text = "".join([m["content"] for m in self.messages])

        url = os.environ.get("GPT3_URL")
        headers = {"Content-Type": "application/json"}
        data = {
            "model": "gpt-3.5-turbo",
            "messages": self.messages
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()

        response_data = response.json()
        answer = response_data["choices"][0]["message"]["content"]
        self.add_message("assistant", answer)

        return answer


