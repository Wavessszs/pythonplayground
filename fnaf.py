import tkinter as tk
import random
import time
import threading
import numpy as np

weights = [0.75, 0.25]
position = ""
boolean = ""
seconds = 4
seconds2 = 2


def minustimesum():
    minustime()
    minustime2()


def minustime():
    global seconds
    print("seonds 1 working")
    time.sleep(10)
    if seconds != .5:
        seconds = seconds - .5
        print(seconds)
        minustime()
    else:
        seconds = .5


def minustime2():
    global seconds2
    print("seodncs 2 wokring")
    time.sleep(10)
    if seconds2 != .5:
        seconds2 = seconds2 - .5
        print(seconds2)
        minustime2()
    else:
        seconds2 = .5


def not_moving():
    print("Not moving.")
    time.sleep(seconds)


def start():
    global position, boolean
    position = "start"
    available_moveset = [top_left, top_right, center]
    print("Now at start.")
    boolean = ""
    time.sleep(seconds)
    while True:
        move_chance = random.random()
        if move_chance <= 0.6:
            direction = random.choice(available_moveset)
            direction()
            break
        else:
            not_moving()


def top_left():
    global position
    position = "top_left"
    available_moveset = [start, left]
    print("Now at top_left.")
    time.sleep(seconds)
    while True:
        move_chance = random.random()
        if move_chance <= 0.6:
            direction = random.choice(available_moveset)
            direction()
            break
        else:
            not_moving()


def top_right():
    global position
    position = "top_right"
    available_moveset = [start, right]
    print("Now at top_right.")
    time.sleep(seconds)
    while True:
        move_chance = random.random()
        if move_chance <= 0.6:
            direction = random.choice(available_moveset)
            direction()
            break
        else:
            not_moving()


def center():
    global position
    position = "center"
    available_moveset = [right, start, left]
    print("Now at center.")
    time.sleep(seconds)
    while True:
        move_chance = random.random()
        if move_chance <= 0.6:
            direction = random.choice(available_moveset)
            direction()
            break
        else:
            not_moving()


def right():
    global position
    position = "right"
    available_moveset = [top_right, center, bottom_right]
    print("Now at right.")
    time.sleep(seconds)
    while True:
        move_chance = random.random()
        if move_chance <= 0.6:
            direction = random.choice(available_moveset)
            direction()
            break
        else:
            not_moving()


def left():
    global position
    position = "left"
    available_moveset = [top_left, center, bottom_left]
    print("Now at left.")
    time.sleep(seconds)
    while True:
        move_chance = random.random()
        if move_chance <= 0.6:
            direction = random.choice(available_moveset)
            direction()
            break
        else:
            not_moving()


def bottom_left():
    global position, boolean, weights
    position = "bottom_left"
    print(position)
    available_moveset = [origin, left]
    print("Now at bottom_left.")
    time.sleep(seconds2)
    if boolean == "1":
        start()
        return
    time.sleep(seconds2)

    while True:
        move_chance = random.random()
        if move_chance <= 0.6:
            direction = np.random.choice(available_moveset, p=weights)
            direction()
            break
        else:
            not_moving()


def bottom_right():
    global position, boolean, weights
    position = "bottom_right"
    available_moveset = [origin, right]
    print("Now at bottom_right.")
    time.sleep(seconds2)
    if boolean == "1":
        start()
        return
    time.sleep(seconds2)
    while True:
        move_chance = random.random()
        if move_chance <= 0.6:
            direction = np.random.choice(available_moveset, p=weights)
            direction()
            break
        else:
            not_moving()


def on_key_press(event):
    global position, boolean
    key = event.keysym
    if position in ["bottom_left", "bottom_right"] and key == "q" or key == "w":
        boolean = "1"


def origin():
    print("Game over.")


def update_label(row, col, new_text):
    labels[row][col].config(text=new_text)


# Function to update labels
def update_labels():
    for i in range(3):
        for j in range(3):
            label_name = initial_label_names[i * 3 + j]
            if label_name in label_texts:
                update_label(i, j, label_texts[label_name])
            else:
                update_label(i, j, label_name)


# Call the function to initially set the label names


# Function to check and update label
def check_and_update_label(input_label):
    if input_label in initial_label_names:
        # Revert previous label to its initial state
        for label_name in label_texts:
            update_label_name = initial_label_names.index(label_name)
            row = update_label_name // 3
            col = update_label_name % 3
            update_label(row, col, label_name)
        # Update the current label
        index = initial_label_names.index(input_label)
        row = index // 3
        col = index % 3
        update_label(row, col, "is here")
        label_texts[input_label] = "is here"
    else:
        print("Invalid label name!")


def update_position():
    global position
    check_and_update_label(position)
    window.after(1000, update_position)


def start_in_background():
    thread1 = threading.Thread(target=bottom_right)
    thread2 = threading.Thread(target=minustimesum)
    thread1.daemon = True
    thread2.daemon = True
    thread1.start()
    thread2.start()


# Create a Tkinter window
window = tk.Tk()

window.title("Grid Display")
window.geometry("470x500")

# Create a 3x3 grid of labels
labels = [[tk.Label(window, width=20, height=10, relief="solid") for _ in range(3)] for _ in range(3)]

# Place the labels in the grid
for i in range(3):
    for j in range(3):
        labels[i][j].grid(row=i, column=j, padx=5, pady=5)

# List of initial label names
initial_label_names = [
    "top_left", "start", "top_right",
    "left", "center", "right",
    "bottom_left", "bottom", "bottom_right"
]

# Dictionary to store the current label texts
label_texts = {}

update_labels()
update_position()
window.bind("<Key>", on_key_press)
window.focus_set()
start_in_background()
window.mainloop()
