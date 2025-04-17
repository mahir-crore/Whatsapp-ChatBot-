import pyautogui
import time
import pyperclip
import webbrowser
from openai import OpenAI


print (" Please set all curser according your screen size before run the code ")
time.sleep(10)

client = OpenAI(
  api_key="<Your Key Here>",
)

def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False
    
    

  # 🚀 Step 2: Open WhatsApp Web
print("📲 Opening WhatsApp Web in default browser...")
webbrowser.open("https://web.whatsapp.com")
time.sleep(45)  # Time to scan QR

# 🖱 Step 3: Auto-click on first chat using cursor
print("🖱 Moving cursor to first chat and clicking...")
pyautogui.moveTo(280, 520, duration=0.5)  # 👈 Adjust if needed #value edit
pyautogui.click()
  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse 
    pyautogui.moveTo(972,202)#value edit
    pyautogui.dragTo(2213, 1278, duration=2.0, button='left')  # Drag for 1 second #value edit

    # Step 3: Copy the selected text 
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2) 
    pyautogui.click(1994, 281)#value edit

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named relaxmsz.in who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] myself : "},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates 
        pyautogui.click(1808, 1328)#value edit
        time.sleep(1)  

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1) 

        # Step 7: Press Enter
        pyautogui.press('enter')
