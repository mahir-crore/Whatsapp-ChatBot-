import webbrowser
import pyautogui
import time 
import pyperclip


print (" Please set all curser according your screen size before run the code ")
time.sleep(10)

# 🚀 Step 1: Open WhatsApp Web
print("📲 Opening WhatsApp Web in default browser...")
webbrowser.open("https://web.whatsapp.com")
print("opening whatsapp")
time.sleep(2)
webbrowser.open("https://chatgpt.com")
time.sleep(2)
pyautogui.hotkey('ctrl', '1')
time.sleep(40)  # Time to scan QR


# 🖱 Step 2: Auto-click on first chat using cursor
print("🖱 Moving cursor to first chat and clicking...")
pyautogui.moveTo(280, 520, duration=0.5)  # 👈 Adjust if needed
pyautogui.click()


clicked = False
while True:
    time.sleep(5)
    # Step 3: Drag the 
    pyautogui.moveTo(858,158)#value edit
    pyautogui.dragTo(828, 681, duration=2.0, button='left')  # Drag for 1 second #value edit

    # Step 4: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    chat_history = pyperclip.paste() + "\n\n\n only 5 ,6 word mai reply karo faltu nahi time  aur  name  to katai  nahi    "
    pyperclip.copy(chat_history)

    pyautogui.hotkey('ctrl', '2')
    time.sleep(5)
 
    if not clicked:
        pyautogui.click(515, 347)#value edit
        clicked = True 
    else:
        pyautogui.click(574,621)#value edit
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.moveTo(858,158)#value edit
    pyautogui.dragTo(828, 681, duration=2.0, button='left') #value edit
    pyautogui.click(426, 522)#value edit
    time.sleep(2)
    if  not clicked:
        pyautogui.click(426,522)#value edit
        pyautogui.click(427,473)#value edit
        pyautogui.click(427,472)#value edit
        clicked=True
    else:
        pyautogui.click(427,238)#value edit
        pyautogui.click(427,238)#value edit
        pyautogui.click(426,269)#value edit
        pyautogui.click(426,269)#value edit
        pyautogui.click(427,297)#value edit
        pyautogui.click(427,297)#value edit

        
    time.sleep(3)# value edit 

    pyautogui.hotkey('ctrl', '1')
    time.sleep(2)
    pyautogui.click(628, 694)#value edit 
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)












    