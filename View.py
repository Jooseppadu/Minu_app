# Python program demonstrating
# ScrolledText widget in tkinter

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Creating tkinter main window
win = tk.Tk()
win.title("Programm")
win.geometry('600x500')


# Title Label
ttk.Label(win,
		text = "Tasks and Students",
		font = ("Times New Roman", 15),
		background = 'green',
		foreground = "white").grid(column = 0,
									row = 0)

# Creating scrolled text
# area widget
text_area = scrolledtext.ScrolledText(win,
									wrap = tk.WORD,
									width = 20,
									height = 20,
									font = ("Times New Roman",
											11))

text_area.grid(row=0, column=0, pady=40, padx=2)



text_area = scrolledtext.ScrolledText(win,
									wrap = tk.WORD,
									width = 20,
									height = 20,
									font = ("Times New Roman",
											11))

text_area.grid(row=0, column=1, pady=40, padx=2)

text_area = scrolledtext.ScrolledText(win,
									wrap = tk.WORD,
									width = 20,
									height = 20,
									font = ("Times New Roman",
											11))

text_area.grid(row=0, column=2, pady=40, padx=2)




# Placing cursor in the text area
text_area.focus()
button = tk.Button(win, text="ÕPILASED")
button.grid(column=0, row=2, pady=2, padx=2)

button = tk.Button(win, text="ÜLESANDED")
button.grid(column=0, row=3, pady=2, padx=2)

button = tk.Button(win, text="SEGA")
button.grid(column=2, row=2, pady=2, padx=2)

button = tk.Button(win, text="SALVESTA")
button.grid(column=2, row=3, pady=2, padx=2)

win.mainloop()

