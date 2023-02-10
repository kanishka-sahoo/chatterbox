# Chatterbox
Chatterbox is a basic chatbot based on OpenAI's GPT-3 Models. It is based on tkinter and offers a simple way to learn the basics of the OpenAI API

# How to create an OpenAI API Token?
1. Visit [OpenAI's Website](https://beta.openai.com/) and create an account
2. Once done creating your account, visit the [API keys page](https://beta.openai.com/account/api-keys) and click on ```+ Create new secret key```
3. Copy the key generated and paste it into a .env file as ```API_TOKEN="your-API-key"```
4. Save the file.

# Steps to configure
1. Create a virtual environment and activate it.
2. run ```python -m pip install -r requirements.txt``` in your main folder
3. Create a .env file and store your API key in it in the format ```API_TOKEN="Your-Token-Here"```
4. Run gpt3_chatbot.py