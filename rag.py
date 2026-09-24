from groq import Groq
from dotenv import load_dotenv
import os
from search import search
def get_input():
    return input("Enter the prompt: ")

load_dotenv()
client = Groq()

question = "how to find a bug?\n"
datalist = search(question)
prompt = question  + "\n\n".join(datalist) + "\n\nOnly use the information above i gave you to answer the question. Don't invent any information if there is none."

print(prompt)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    model="openai/gpt-oss-20b"
)

print(chat_completion.choices[0].message.content)
