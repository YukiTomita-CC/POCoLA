from openai import OpenAI
import streamlit as st


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    
    def generate_response(self, messages):
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            stream=True
            )

        for chunk in completion:
            content = chunk.choices[0].delta.content
            if content:
                yield content
