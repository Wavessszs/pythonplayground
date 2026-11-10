import tkinter
from tkinter import *
import os
from collections import Counter

shopcart_dict={}

button_counter = Counter()

def add_to_dict(key, value):
    # If the key already exists, increment the value
    if key in shopcart_dict:
        shopcart_dict[key] += value
    # Otherwise, add a new key-value pair
    else:
        shopcart_dict[key] = value
    # Increment the button counter
    button_counter[key] += 1
    # Print the dictionary and button counts
    print(shopcart_dict)
    print(button_counter)

def receipt():

    receiptwindow = Toplevel(window)
    receiptwindow.title("Checkout")
    receiptwindow.geometry("400x400")

    global button_counter
    global shopcart_dict
    for i, key in enumerate(shopcart_dict.keys()):
        # Add the key label to the window
        key_label = Label(receiptwindow, text=f"{button_counter[key]} x {key}")
        key_label.grid(row=i, column=0, padx=10, pady=5)

        # Add the value label to the window
        value_label = Label(receiptwindow, text=shopcart_dict[key])
        value_label.grid(row=i, column=1, padx=10, pady=5)

    values_list = list(shopcart_dict.values())
    values_sum = sum(values_list)
    total = Label(receiptwindow,
                  text=f"Total Value: {values_sum}"
                  )
    label = Label(receiptwindow, text="Finalize your order?")
    total.grid(row=i + 1, column=1)
    label.grid(row=i + 2, column=0)

    confirm = Button(receiptwindow,
                    text="YES",
                    command=lambda: [receiptwindow.destroy(),accept_items()]
                    )
    deny = Button(receiptwindow,
                  text="NO",
                  command=lambda: [receiptwindow.destroy(),clear_list(),deny_print()]
                  )

    confirm.grid(row= i + 3, column=0)
    deny.grid(row= i + 3, column=1)

def accept_items():
    global button_counter
    global shopcart_dict

    certwindow= Toplevel(window)
    certwindow.title("Checkout")
    certwindow.geometry("400x250")

    values_list = list(shopcart_dict.values())
    amount = sum(values_list)

    greet = Label(certwindow,
                  text="You have successfully ordered :")
    greet.pack()

    for i, key in enumerate(shopcart_dict.keys()):
        if button_counter[key] > 1:
            order = "orders"
        else:
            order= "order"

        output = Label(certwindow,
                      text=f"{button_counter[key]} {order} of {key} worth {shopcart_dict[key]}")
        output.pack()
    lbl = Label(certwindow,
                text=f"Totalling a value of {amount} pesos.")

    label = Label(certwindow,
                  text="Thank you for purchasing!\nEnjoy your meal!")

    btn = Button (certwindow,
                  text= "Print receipt",
                  command=lambda:[clear_list(),certwindow.destroy()]
                  )

    lbl.pack()
    label.pack()
    btn.pack()


def clear_list():
    global shopcart_dict
    global button_counter

    for key in shopcart_dict:
        button_counter[key] = 0


    shopcart_dict.clear()

    if bool(shopcart_dict):
        print("The dictionary is not empty.")
    else:
        print("The dictionary is now empty.")


def deny_print():
    cert2window = Toplevel(window)
    cert2window.title("Withdraw")
    cert2window.geometry("200x200")

    label = Label(cert2window,
                  text="All orders are disregarded\nPlease care to browse more!")
    label.pack()


window = Tk()
window.title("Welcome, feel free to browse any of the items!")
window.geometry("720x800")

dir_path = os.path.dirname(os.path.realpath(__file__))
resource_path = os.path.join(dir_path, "resources")

iconname = "windowicon.ico"
burgername = "burger.png"
friesname = "fries.png"
sundaename = "sundae.png"
chipsname = "chips.png"
milkteaname = "milktea.png"
chicken_nuggetsname = "nuggets.png"
fried_chickenname = "fried_chicken.png"
apple_piename = "apple_pie.png"
pancakename = "pancake.png"


window.iconbitmap(resource_path, iconname)


burgerimage= tkinter.PhotoImage(file=os.path.join(resource_path,burgername))
friesimage= tkinter.PhotoImage(file=os.path.join(resource_path,friesname))
sundaeimage= tkinter.PhotoImage(file=os.path.join(resource_path,sundaename))
chipsimage= tkinter.PhotoImage(file=os.path.join(resource_path,chipsname))
milkteaimage= tkinter.PhotoImage(file=os.path.join(resource_path,milkteaname))
nuggetsimage= tkinter.PhotoImage(file=os.path.join(resource_path,chicken_nuggetsname))
fried_chickenimage= tkinter.PhotoImage(file=os.path.join(resource_path,fried_chickenname))
apple_pieimage= tkinter.PhotoImage(file=os.path.join(resource_path,apple_piename))
pancakeimage= tkinter.PhotoImage(file=os.path.join(resource_path,pancakename))


burger = Button (window,
                 text="Beefy Korean Style Burger\n59",
                 compound="top",
                 image=burgerimage,
                 command=lambda: add_to_dict("Beefy Korean Style Burger", 59)
                 )
fries = Button (window,
                text="Italian Butter Grazed Potato Fries\n39",
                compound="top",
                image=friesimage,
                command=lambda: add_to_dict("Italian Butter Grazed Potato Fries", 39)
                )
sundae = Button (window,
                text="Chocolate Willow Autumn Sundae\n20",
                compound="top",
                image=sundaeimage,
                command=lambda: add_to_dict("Chocolate Willow Autumn Sundae", 20)
                )
chips = Button (window,
                 text="Cheesy Truffle Chips with Parmesan and Chives\n25",
                 compound="top",
                 image=chipsimage,
                 command=lambda: add_to_dict("Cheesy Truffle Chips with Parmesan and Chives", 25)
                 )
milktea = Button (window,
                text="Red Velvet Earl Grey Tea Latte\n60",
                compound="top",
                image=milkteaimage,
                command=lambda: add_to_dict("Red Velvet Earl Grey Tea Latte", 60)
                )
nuggets = Button (window,
                text="Spicy Buffalo Style Chicken Bites\n30",
                compound="top",
                image=nuggetsimage,
                command=lambda: add_to_dict("Spicy Buffalo Style Chicken Bites", 30)
                )
fried_chicken = Button (window,
                 text="Southern-style Buttermilk Chicken\n89",
                 compound="top",
                 image=fried_chickenimage,
                 command=lambda: add_to_dict("Southern-style Buttermilk Chicken", 89)
                 )
apple_pie = Button (window,
                text="Warm Cinnamon Apple Tart\n29",
                compound="top",
                image=apple_pieimage,
                command=lambda: add_to_dict("Warm Cinnamon Apple Tart", 29)
                )
pancake = Button (window,
                text="Fluffy Buttermilk Pancakes with Maple Syrup\n29",
                compound="top",
                image=pancakeimage,
                command=lambda: add_to_dict("Fluffy Buttermilk Pancakes with Maple Syrup", 29)
                )


submit = Button (window,
                text="submit",
                command=receipt)

burger.grid(row=0,column =0, sticky="NSEW")
fries.grid(row=0,column =1,sticky="NSEW")
sundae.grid(row=0,column =2,sticky="NSEW")
chips.grid(row=1,column =0, sticky="NSEW")
milktea.grid(row=1,column =1,sticky="NSEW")
nuggets.grid(row=1,column =2,sticky="NSEW")
fried_chicken.grid(row=2,column =0, sticky="NSEW")
apple_pie.grid(row=2,column =1,sticky="NSEW")
pancake.grid(row=2,column =2,sticky="NSEW")

submit.grid(row=5,column=1)


window.mainloop()