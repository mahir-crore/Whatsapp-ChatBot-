import os
import subprocess
import time 
from openai import OpenAI
 

print (" Please set all curser according your screen size before run the code ")
time.sleep(10)

client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''

'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "history and respond like relaxmsz.in"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)





def has_api_key():
    try:
        with open("bot.py", "r") as file:
            content = file.read()
            return (
                "api_key=" in content and
                "<Your Key Here>" not in content and
                "sk-" in content
            )
    except FileNotFoundError:
        return False

if has_api_key():
    print("✅ API key detected! Running bot.py automatically...")
    subprocess.run(["python", "bot.py"])
else:
    print("❌ No valid API key found. Falling back to what.py...")
    subprocess.run(["python", "chatgpt.py"])
