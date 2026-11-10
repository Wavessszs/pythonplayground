import tkinter as tk
from tkinter import ttk
import json
import os
import pyautogui
import time
import webbrowser
import subprocess

# Define the questions and choices
questions = [
    "Hi, [player name]. Do you have an ideal day filled with joy and fulfillment?",
    "Do you value qualities like honesty, kindness, and resilience in yourself?",
    "Can you handle setbacks or failures with resilience and learn from them?",
    "Can you recall a time when you felt like someone was watching you?",
    "Do you look for specific qualities in a close friend?",
    "Are you alone right now?",
    "Do you navigate conflicts or disagreements in your relationships effectively?",
    "Are you comfortable expressing vulnerability to others?",
    "Have you ever sensed a hidden agenda in someone you trusted?",
    "Do you have a biggest fear?",
    "Can you embrace change and adapt to new situations effectively?",
    "Do you have strategies to overcome obstacles and challenges?",
    "Have you ever experienced a transformative event that changed your perspective?",
    "Are there aspects of your personality that you feel are hidden or unexplored?",
    "Have you ever had a memory that felt distorted or unsettling?",
    "Have you ever felt like someone was watching you?",
    "Have you ever found yourself questioning the authenticity of your own thoughts?",
    "Are there moments when you feel a deep sense of unease without any apparent cause?",
    "Have you ever experienced a disconnect between your thoughts and your actions?",
    "Have you ever betrayed someone's trust, [player name]?",
    "Have you ever prioritized your own needs over someone else's?",
    "Have you ever experienced a feeling of being drawn to a specific location for unknown reasons?",
    "I've been watching you right from the start.",
    "Do you believe your mind can be easily influenced?",
    "Have you ever felt like you were being watched without anyone being present?",
    "Can you trust your own perceptions and judgments?",
    "Aren't you alone, [player name]?",
    "I've been watching you right from the start.",
    "Aren't you alone?",
    "Do you remember?",
    "The lies...",
    "The little, insignificant things you stole.",
    "Your subtle betrayal of others.",
    "The way you ignored other people's needs for the sake of yourself.",
    "The way you chose to make them feel sorry for themselves.",
    "I know how your mind works.",
    "I've been watching since the very beginning, [player name].",
    "Everyone knows what you did.",
    "You convinced yourself that it's fine because everyone does it.",
    "No.",
    "You have sinned.",
    "Look out.",
    "I'll see you later."
]

choices = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]

# Create a variable to store the selected choice for each question
selected_choices = []
s_choice = []
choices_2 = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
name = ""
ch1 = ""
ch2 = ""
ch3 = ""
buttons = []
current_dir = os.path.dirname(os.path.abspath(__file__))
button_style = {
    "bg": "lightgray",
    "fg": "black",
    "bd": 2,
    "relief": "raised",
    "font": ("Arial", 10, "bold"),
}
text_style = {
    "font": ("Arial", 12),
    "fg": "black",
    "bg":"white",
    "relief":"sunken"
}
text_styles = {
    "font": ("Arial", 16),
    "fg": "black",
}

def start_game():
    try:
        # Hide the opening note and show the name and gender input fields
        if os.path.exists('saved_variables.json'):
            with open('saved_variables.json', 'r') as file:
                global s_choice
                global buttons
                questions_2 = [
                    "Hi, [player name]. Do you have an ideal day filled with joy and fulfillment?",
                    "[player name]. Do you remember me?",
                    "I hope you're doing fine",
                    "You know, we can just start over and \ntry to know each other better.",
                    "Don't you think so?"
                ]
                choices_2 = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]

                def open_notepad(text):
                    # Check if Notepad++ is available
                    notepadpp_available = subprocess.call(["where", "notepad++"], stdout=subprocess.PIPE) == 0

                    if notepadpp_available:
                        # Launch Notepad++ with new blank window
                        subprocess.Popen(["notepad++", "-multiInst", "-nosession"])
                    else:
                        # Check if Notepad is available
                        notepad_available = subprocess.call(["where", "notepad"], stdout=subprocess.PIPE) == 0

                        if notepad_available:
                            # Launch Notepad
                            subprocess.Popen(["notepad"])
                        else:
                            print("Neither Notepad nor Notepad++ is available on this system.")
                            return

                    time.sleep(5)  # Wait for Notepad/Notepad++ to open
                    pyautogui.write(text)
                def delete_buttons():
                    global buttons
                    for button in buttons:
                        button.pack_forget()
                    buttons = []

                def update_first_question():
                    global s_choice
                    if len(s_choice) == 0:
                        frame2.after(3000,
                            lambda: question2_label.config(text=questions_2[1].replace("[player name]", new_name)))
                        s_choice.append(None)
                        print("success")

                    else:
                        print("didn't reach")

                def select_choice_2(choice_2):
                    global s_choice
                    s_choice.append(choice_2)

                    if len(s_choice) < len(questions_2):
                        frame2.after(2000, lambda: question2_label.config(
                            text=questions_2[len(s_choice)].replace("[player name]", new_name)))
                        print("posttest")
                    else:
                        choice_evaluation()
                        open_executables()
                def open_executables():

                        text_to_type = "you are not alone."
                        open_notepad(text_to_type)

                def choice_evaluation():
                    global ch1, ch2, ch3, choices_2, new_name, buttons

                    delete_buttons()
                    ch1_evaluation()

                def ch1_evaluation():

                    global buttons

                    if ch1 == choices_2[0] or ch1 == choices_2[1]:
                        question2_label.config(text="i assume for someone who values honesty and kindness knows much about being the one below.\none who already tasted the bitter taste of not being someone people accept.\nbut it's okay,white lies are lies that are white. and lying is something as bad as killing truth.\n \nyou lied don't you?")
                        button_yes2 = tk.Button(frame2, **button_style, text="yes", width=15, command=lambda: ch2_evaluation(ch2))
                        button_yes2.pack(pady=5)
                        buttons.append(button_yes2)


                    else:
                        question2_label.config(text=":)")
                        button_yes2 = tk.Button(frame2,  **button_style,text="i'm sorry", width=15, command=lambda: ch2_evaluation(ch2))
                        button_yes2.pack(pady=5)
                        buttons.append(button_yes2)

                def ch2_evaluation(ch2):
                    global buttons
                    delete_buttons()
                    text_to_type = "are you sure?"
                    open_notepad(text_to_type)

                    if ch2 == choices_2[0] or ch2 == choices_2[1]:
                        question2_label.config(text="ever felt those eyes on you? they're watching, and every single thing you do, i know.\n\nheard that? i was that." )# Move to ch3
                        button_yes3 = tk.Button(frame2,  **button_style,text="are you here?", width=15,command=lambda: ch3_evaluation(ch3))
                        button_yes3.pack(pady=5)
                        buttons.append(button_yes3)
                    else:
                        question2_label.config(text="you can't escape.")
                        button_yes3 = tk.Button(frame2, **button_style, text="i can't.", width=15, command=lambda: ch3_evaluation(ch3))
                        button_yes3.pack(pady=5)
                        buttons.append(button_yes3)

                def ch3_evaluation(ch3):
                    global buttons
                    delete_buttons()
                    text_to_type = "behind you."
                    open_notepad(text_to_type)

                    if ch3 == choices_2[0] or ch3 == choices_2[1]:
                        question2_label.config(text="open the door, darling...i'm waiting...")
                        button_yes4 = tk.Button(frame2, **button_style, text="i never did anything.", width=15, command=lambda: ending())
                        button_yes4.pack(pady=5)
                        buttons.append(button_yes4)

                    else:
                        question2_label.config(text="of course, you're not alone. you're with me. i am your company.\n\njust open up the window...")
                        button_yes4 = tk.Button(frame2, **button_style,text="leave me alone.", width=15, command=lambda: ending())
                        button_yes4.pack(pady=5)
                        buttons.append(button_yes4)

                def open_gif_in_chrome(file_name):
                    global current_dir
                    file_path = os.path.join(current_dir, file_name)
                    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'  # Path to your Chrome executable
                    webbrowser.get(chrome_path).open('file://' + file_path)

                def ending():

                    delete_buttons()
                    delete()
                    question2_label.config(
                        text="so, let\'s cut to the chase, shall we? i know things. things that you\'d rather keep buried in the darkest corners of your mind. but guess what? i\'m not letting you off the hook that easily.\n\nconsider this a friendly heads-up, though it might not feel so friendly. the ghosts of your past are restless, and they\'ve been whispering in my ear. it\'s like we\'re old pals, you know?\n\nnow, don\'t go thinking i\'m planning some gory showdown. that\'s too predictable. i prefer to be more subtle, like a little eye peeking through the window on your back. there will be sleepless nights, racing thoughts – that\'s the gift i\'m bestowing upon you.\n\ni\'ll be right here, to help you question your own sanity, wondering if you\'re losing your grip on reality. that\'s the real fun, isn\'t it?\n\nlook over your shoulder, [player name].\n\ni\'ll see you tonight.".replace(
                            "[player name]", new_name))
                    gif_file_name = 'image.gif'
                    window2.attributes("-fullscreen", True)
                    window.after(10000, lambda: (open_gif_in_chrome(gif_file_name),fullscreeen()))

                def fullscreeen():
                    time.sleep(1)
                    pyautogui.hotkey('win', 'up')
                    pyautogui.press('f11')

                def delete():
                    if os.path.exists('saved_variables.json'):
                        os.remove('saved_variables.json')


                        print("Successfully deleted")
                    else:
                        print("File not found")

                def button_clicked():
                    for button in buttons:
                        button.config(state=tk.DISABLED)
                        frame2.after(2000, enable_buttons)  # Enable the buttons after 2 seconds

                def enable_buttons():
                    for button in buttons:
                        button.config(state=tk.NORMAL)

                def button_callback(choice):
                    select_choice_2(choice)
                    button_clicked()

                window2 = tk.Toplevel()
                window2.title('ab21f7596a6f608efc2d75eb6094e82308d23cb9d05e682cc11111a2dd8b3c79')
                window2.geometry('600x400')

                frame2= tk.Frame(window2, bg="silver", bd=2, relief="raised")
                frame2.config(borderwidth=2, highlightthickness=1, highlightbackground="black")
                frame2.pack(padx=10, pady=10, fill="both", expand=True)
                
                current_dirs = os.path.dirname(os.path.abspath(__file__))
                icon_path = os.path.join(current_dirs, "icon2.ico")
                window2.iconbitmap(icon_path)

                data = json.load(file)

                new_name = data['name']
                ch1 = data['choice1']
                ch2 = data['choice2']
                ch3 = data['choice3']
                print(new_name)
                print(ch1)
                print(ch2)
                print(ch3)

            # Close the file before entering the main event loop
            file.close()

            question2_label = tk.Label(frame2, text="", width=60, wraplength=400,**text_styles,bg="silver")
            question2_label.pack(pady=20)

            question2_label.config(text=questions_2[0].replace("[player name]", new_name))

            update_first_question()

            for choice_2 in choices_2:
                button = tk.Button(frame2, text=choice_2, width=15, **button_style, command=lambda c=choice_2: (button_callback(c)))
                button.pack(pady=5)
                buttons.append(button)

            window2.mainloop()

        else:
            opening_note_label.pack_forget()
            start_button.pack_forget()
            name_label.pack()
            name_entry.pack(pady=5)
            padding_label.pack()
            submit_button.pack(pady=5)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("Error decoding JSON data")



# Function to handle the selection of a choice
def select_choice(choice):
    global selected_choices
    selected_choices.append(choice)
    if len(selected_choices) < len(questions):
        # Display the next question
        question_label.config(text=questions[len(selected_choices)].replace("[player name]", name))
    else:
        # End of the game
        end_game()


# Function to end the game and display the results
def end_game():
    # Add your code to process the selected choices and display the results here
    print("Name:", name)

    c1 = selected_choices[1]
    c2 = selected_choices[18]
    c3 = selected_choices[33]
    print("Do you value qualities like honesty, kindness, and resilience in yourself?", c1)
    print("Have you ever felt like someone was watching you?", c2)
    print("Aren't you alone?", c3)

    data = {
        'name': name,
        'choice1': c1,
        'choice2': c2,
        'choice3': c3,
    }
    with open('saved_variables.json', 'w') as file:
        json.dump(data, file)

    window.destroy()


# Function to handle the submission of name and gender input
def submit_input():
    global name
    namef = name_entry.get()
    name = namef.capitalize()


    # Hide the name and gender input fields
    name_label.pack_forget()
    name_entry.pack_forget()
    padding_label.pack_forget()
    submit_button.pack_forget()

    # Display the first question
    question_label.config(text=questions[0].replace("[player name]", name),**text_styles)
    for choice in choices:
        button = tk.Button(frame,text=choice, width=15, **button_style, command=lambda c=choice: select_choice(c))
        button.pack(pady=5)


# Create the game interface
window = tk.Tk()
window.title("Personality Test Game")
window.geometry("600x400")  # Set the window size
current_dirt = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dirt, "icon.ico")
window.iconbitmap(icon_path)

frame = tk.Frame(window, bg="silver", bd=2, relief="raised")
frame.config(borderwidth=2, highlightthickness=1, highlightbackground="black")
frame.pack(padx=10, pady=10, fill="both", expand=True)


opening_note_label = tk.Label(frame, width=60,
                              text="\n\n\nWelcome to the Personality Test Game!\n"
                                   "\nWARNING: This game delves into the deepest corners of your mind. "
                                   "\nRemember, honesty is key. The choices you make will shape your fate."
                                   "\nAre you ready to confront your true self?\n\n\n",**text_style)
opening_note_label.pack(pady=20)

# Create a label for the question
question_label = tk.Label(frame, text="", width=60, wraplength=400, bg="silver")
question_label.pack(pady=20)



# Display text entry field for the name
name_label = tk.Label(frame, text="Name:",bg="silver", font= ("Arial", 12))
name_entry = tk.Entry(frame)


start_button = tk.Button(frame, text="Start Game", width=15,**button_style, command=start_game)
start_button.pack(pady=10)

padding_label = tk.Label(frame, text=" ", bg="silver")


# Display the submit button
submit_button = tk.Button(frame, text="Submit", width=15,**button_style, command=submit_input)



# Start the game
window.mainloop()