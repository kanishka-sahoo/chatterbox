import openai_interface as oif

def main():
    opening_prompt = input("Enter opening prompt: ")
    conversation = opening_prompt + '''\n\nUser:Hello, how are you?\nAI:'''  # variable to keep track of the conversation
    conversation += oif.get_response(conversation)
    print(conversation)
    user_input = input("--> ")
    while user_input:
        conversation += f"User: {user_input}\nAi: "
        resp = oif.get_response(conversation)
        conversation += resp
        print(resp)
        user_input = input("--> ")

if __name__ == "__main__":
    main()
