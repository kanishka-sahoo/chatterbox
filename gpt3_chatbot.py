'''
OpenAI Chatbot, Enables a user to communicate with the GPT3 Chatbot in a conversational manner.
This is the user interface for the program.
'''

import tkinter as tk, time
import openai_interface as oif  # uses custom interface to make maintenance easier.

class ChatbotApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chatbot")
        self.geometry("600x600")
        self.convo_filename = "_chat.txt"
        self.last_response = ""
        self.main()

    def main(self): # the main app window
        self.conversation = '''The following Is a conversation with an AI assistant. The assistant Is helpful, creative, clever, and very friendly.\n\nUser:Hello, how are you?\nAI:'''  # variable to keep track of the conversation
        # self.conversation = '''The following is a conversation between two a human user and an advanced AI.\nUser:Hello\nAI:'''
        # Create a frame to hold the chat messages
        messages_frame = tk.Frame(self)
        messages_frame.pack(padx=10, pady=10)

        # Create a text widget to display the chat messages
        self.messages = tk.Text(messages_frame, bg='white', width=100, height=20, font=("ariel", 16), wrap="word")
        self.messages.pack()

        # Create a frame to hold the input widgets
        input_frame = tk.Frame(self)
        input_frame.pack(padx=10, pady=10)

        # Create an entry widget for the user's input
        self.input_entry = tk.Entry(input_frame, width=25, font=("ariel", 16))
        self.input_entry.pack(side='left', padx=5)

        # Create a button to submit the user's input
        submit_button = tk.Button(input_frame, text="Submit", command=self.submit_chat)
        submit_button.pack(side='right')

        # Create a save button to save the current chat to disk
        save_button = tk.Button(input_frame, text="Save Convo", command=self.save_convo)
        save_button.pack(side="left",)
        self.initial = True
        self.submit_chat()

    def submit_chat(self):  # submits the conversation to OpenAI servers for model
        user_input = self.input_entry.get()
        '''
        if self.last_response != "":
            self.conversation = self.conversation.partition('/')[0][:-6:]
            print(self.conversation)
        '''
        if not self.initial:
            self.conversation = self.messages.get(1.0, tk.END)
            # Add the user's input to the conversation
            self.conversation += f"User: {user_input}\nAI: "
        else:
            self.initial = False

        # Add the chatbot's response to the conversation
        self.last_response, self.conversation = oif.process_user_input(self.conversation, user_input)
        # Display the conversation
        self.messages.delete(1.0, tk.END)
        self.messages.insert(tk.END, self.conversation)
        self.input_entry.delete(0, tk.END)
    
    def save_convo(self):   # Saves the conversation to disk
        with open(self.convo_filename, "a") as f:
            f.write(f"\n[{time.time()}]\n\n")
            f.write(self.conversation)

if __name__ == "__main__":
    app = ChatbotApp()
    app.mainloop()
