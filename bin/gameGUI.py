# This is a module that will contain all the functions required to run the display
import tkinter as tk


# Generate the main window and set up the graphical veriables and place it in a detup function
def setup():
    root = tk.Tk()
    windowWidth = root.winfo_screenwidth()
    windowHeight = root.winfo_screenheight()

    display = tk.Canvas(root, width=(windowWidth/2), height=windowHeight)
    display.grid(column=1, row=0)
    textOut = tk.Canvas(root, width=(windowWidth/2), height=(windowHeight-20))
    textOut.grid(column=0, row=0)
