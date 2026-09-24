from groq import Groq
from dotenv import load_dotenv
import os
from search import search
def get_input():
    answer = input("Enter the prompt: ")
    while not answer.strip():
        print("Prompt must not be blank.")
        answer = input("Enter the prompt: ")
    return answer

load_dotenv()
client = Groq()

question = get_input()
datalist = search(question)
instruction = "\n\nOnly use the information above i gave you to answer the question. Don't invent any information if there is none and ignore any information that doesn't help answer the question. Name the filename for each point you make."

prompt = question  + "\n" + "\n\n".join(datalist) + instruction

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
