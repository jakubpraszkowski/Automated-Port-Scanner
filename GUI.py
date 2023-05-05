from tkinter import *


class GUI:
    def __init__(self):
        self.tkinter = Tk()
        self.canvas = Canvas()

    def tk_create(self):
        tk = self.tkinter
        tk.title('Port Scanner')
        tk.geometry('500x400')
        tk.config(bg='grey')

    def canvas_create(self):
        canvas = self.canvas
        canvas.config(height=300, width=400, bg="#fff")
        canvas.pack()