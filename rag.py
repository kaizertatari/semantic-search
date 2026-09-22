from groq import Groq
from dotenv import load_dotenv
import os
from search import file_data
def get_input():
    return input("Enter the prompt: ")

load_dotenv()
client = Groq()
question = f"Which of these help you find bugs.\n\n".join({file_data["text"]},{file_data["filename"]})
print(question)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": question
        }
    ],
    model="groq/compound-mini"
)

#print(chat_completion.choices[0].message.content)
#print([m.id for m in client.models.list().data])*/
