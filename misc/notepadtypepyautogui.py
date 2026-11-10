import pyautogui
import time

def type_text_in_notepad(text):
    # Open Notepad
    pyautogui.press('win')
    pyautogui.write('notepad')
    pyautogui.press('enter')
    time.sleep(2)  # Wait for Notepad to open

    # Type text into Notepad
    pyautogui.write(text)

# Example usage
text_to_type = "are you sure?"
type_text_in_notepad(text_to_type)
