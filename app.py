from rag import get_answer

def get_input():
    answer = input("Enter the prompt: ")
    while not answer.strip():
        print("Prompt must not be blank.")
        answer = input("Enter the prompt: ")
    return answer

print(get_answer(get_input()))