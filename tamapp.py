from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Tamapp")

frame1 = ttk.Frame(root,width=300, height=200, padding="20 20 20 20")
frame1.grid(column=0, row=0, sticky= (N, W, E, S))

frame2 = ttk.Frame(root,width=300, height=200, padding="20 20 20 20")
frame2.grid(column=0, row=1, sticky= (N, W, E, S))

frame3 = ttk.Frame(root,width=300, height=200, padding="20 20 20 20")
frame3.grid(column=0, row=2, sticky= (N, W, E, S))


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()

