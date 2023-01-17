'''
OpenAI Chatbot, Enables a user to communicate with the GPT3 Chatbot in a conversational manner.
This is the interface between the chatbot and the program.
'''
import openai, os
import time
from dotenv import load_dotenv

load_dotenv()

openai.api_key = str(os.environ["API_TOKEN"])

def get_response(conversation):
    # Send the conversation to the OpenAI API
    # Change engine="" to change the text completion engine used
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"{conversation}"),
        max_tokens=2048,
        n = 1,
        stop=None,
        temperature=0.7,
    )
    conversation += f"{response['choices'][0]['text']}\n"
    return conversation

def process_user_input(conversation: str, user_input: str):
    # Checks the user input and allows for sending of commands starting with '/'
    if not user_input.startswith('/'):
        return "", get_response(conversation)
    match user_input[1::]:
        case "time":
            response = time.strftime("%H:%M:%S")
        case "date":
            response = time.strftime("%d/%m/%Y")
        case "close":
            exit()
        case "":
            pass
        case other:
            response = "The command could not be found"
    return user_input + response, conversation + response