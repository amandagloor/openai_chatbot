import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key_path = os.getenv('OPENAI_API_KEY')
messages = [
    {"role": "system", "content": "You're an expert in programming Python!"}
]
while True:
    content = input("User: ")
    messages.append({"role": "user", "content": content})


    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )    
    #    {"role": "system", "content": "You're a kind helpful assistant"}
    #    {"role": "system", "content": "You're a recruiter who asks tough interview questions"}


    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    messages.append({"role": "assistant", "content": chat_response})

    if content.lower() in ['bye', 'goodbye']:
        print("Goodbye!")
        break
