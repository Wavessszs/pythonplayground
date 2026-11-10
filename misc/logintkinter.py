import collections
from collections import *

input_dict= {"khevin":"123",
             "henson":"pogiako",
             "jonyl":"astigsijc"}

print(input_dict)

name = ''
password = ''

namewindow2 = ''
passwordwindow2 = ''

input = ()
input2 = ()


def listtotuple():
    global name
    global password
    global input

    list1 = list(input)
    list1.append(name)
    list1.append(password)
    input = tuple(list1)

def input_checker():

    global input

    if input in input_dict.items():
        print ("Credentials Accepted")
        input = tuple()
    else:
        input = tuple()
        print ("Please Try Again")

def submit():
    global name
    global password
    name = name_var.get()
    password = passw_var.get()

    print("The name is : " + name)
    print("The password is : " + password)

    name_var.set("")
    passw_var.set("")

from tkinter import *

window = Tk()

window.geometry("600x400")
window.title("Login Interface")
window.resizable(width=False,height=False)

name_var = StringVar()
passw_var = StringVar()

name2_var = StringVar()
passw2_var = StringVar()

name_label = Label(window,
                   text='Username',
                   font=('calibre', 10, 'bold'))
name_entry = Entry(window,
                   textvariable=name_var,
                   font=('calibre',10, 'normal'))
passw_label = Label(window,
                    text='Password',
                    font=('calibre', 10, 'bold'))
passw_entry =Entry(window,
                   textvariable=passw_var,
                   font=('calibre', 10, 'normal'),
                   show='*')
sub_btn =Button(window,
                text='Submit',
                command=lambda: [submit(),listtotuple(),input_checker()])


name_label.pack()
name_entry.pack()
passw_label.pack()
passw_entry.pack()
sub_btn.pack()



def submitwndw2():
    global namewindow2
    global passwordwindow2
    namewindow2 = name2_var.get()
    passwordwindow2 = passw2_var.get()

    name2_var.set("")
    passw2_var.set("")

def listtodict():
    global namewindow2
    global passwordwindow2
    global input_dict

    list2 = list(input2)
    list2.append(namewindow2)
    list2.append(passwordwindow2)

    x = iter(list2)
    result = dict(zip(x, x))
    print(result)

    input_dict.update(result)

    print(input_dict)

def openNewWindow():

    Window2 = Toplevel(window)


    Window2.title("Create New Account")
    Window2.geometry("600x400")


    name_label = Label(Window2,
                       text='Username',
                       font=('calibre', 10, 'bold'))
    name_entry = Entry(Window2,
                       textvariable=name2_var,
                       font=('calibre', 10, 'normal'))
    passw_label = Label(Window2,
                        text='Password',
                        font=('calibre', 10, 'bold'))
    passw_entry = Entry(Window2,
                        textvariable=passw2_var,
                        font=('calibre', 10, 'normal'))
    sub_btn = Button(Window2,
                     text='Submit',
                     command=lambda: [submitwndw2(), listtodict(), Window2.destroy()])

    name_label.pack()
    name_entry.pack()
    passw_label.pack()
    passw_entry.pack()
    sub_btn.pack()

nw_btn=Button(window,
                text='Create New Account',
                command=openNewWindow)
nw_btn.pack()

window.mainloop()