'''Let's make a basic GUI at least show up on the screen.'''

import tkinter as tk

import motor_class

root = tk.Tk()
root.geometry("300x200")
root.title("My GUI")


my_label = tk.Label(root, text="Hello?")
my_label.pack()

my_label2 = tk.Label(root, text="Label?")
my_label2.pack()

my_motor = motor_class.Motor()
print(f"my_motor: {my_motor}")
root.mainloop()
