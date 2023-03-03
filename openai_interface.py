'''
OpenAI Chatbot, Enables a user to communicate with the GPT3 Chatbot in a conver
sational manner.
This is the interface between the chatbot and the program.
Author: Kanishka Sahoo
'''
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set up the OpenAI API key, loaded from a .env file containing the token as AP
# I_TOKEN=""
openai.api_key = str(os.environ["API_TOKEN"])

messages = []
use_model = 'text-davinci-003'
def get_response(prompt):
    global messages
    # Send the conversation to the OpenAI API
    # Change engine="" to change the text completion engine used
    messages.append({'role':'system', 'content': 'You are a helpful AI assistant.'})
    messages.append({'role':'user', 'content':str(prompt)})
    response = openai.ChatCompletion.create(
        model=use_model,
        messages=messages
    )
    resp = response['choices'][0]['message']
    messages.append(resp)
    return f"""{resp['content']}\n"""


def process_user_input(conversation: str, user_input: str):
    # Checks the user input and allows for sending of command starting with '/'
    # if not user_input.startswith('/'):
    return "", get_response(conversation)
    '''
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
    '''
