from tkinter import *

root = Tk()
root.title("label-test") # set window title
root.geometry("200x300") # set window size note : x is not *
root.resizable(width=True, height=False) # set whether the window can be lengthened / wide, False immutable, True variable, default is True