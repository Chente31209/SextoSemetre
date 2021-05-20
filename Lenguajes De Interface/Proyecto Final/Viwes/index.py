import tkinter as tk
from Controles.IndexControler import *
from Viwes.LoginViwe import *
from Viwes.Compnetes.HeaderComponet import *

class index:
    def __init__(self):
        self.app=tk.Tk()

    def ViweMain(self):
        #head
        frameHead = tk.Frame(self.app, width=700, height=50)
        frameHead.pack()
        frameHead.config(bg="lightblue")
        frameHead.config(bd=25)
        #/head
        #body
        frameBody = tk.Frame(self.app ,width=700, height=700)
        frameBody.pack()
        frameBody.config(bg="blue")
        frameBody.config(bd=25)
        ViweLogin = Login(frameBody)
        Ha=Hader(frameHead,ViweLogin)
        Ha.Init().grid(row=0 , column=0)
        #/body
        self.app.geometry("700x600")
        self.app.mainloop()
    def onClose(self):
        self.app.destroy()
