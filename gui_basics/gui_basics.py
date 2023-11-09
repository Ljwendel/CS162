'''Let's make a basic GUI at least show up on the screen.'''

import tkinter as tk
# import motor_build


def update_label_text():
    my_label.set()


root = tk.Tk()
root.geometry("300x200")
root.title("My GUI")


my_label_string_var = tk.StringVar(root, "hello?")
my_label = tk.Label(root, textvariable=my_label_string_var)
my_label.pack()
# my_motor = motor_build.Motor()

label_button = tk.Button(root, text='update label', command=update_label_text)
label_button.pack()

# my_label = tk.Label(root, text=f"Hello?")
# my_label.pack()

# my_label2 = tk.Label(root, text="Label?")
# my_label2.pack()


# print(f"my_label: {my_label}")
root.mainloop()
