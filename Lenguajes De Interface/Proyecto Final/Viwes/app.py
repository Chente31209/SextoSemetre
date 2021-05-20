import tkinter as tk
from Viwes.Compnetes import HeaderComponet
from Viwes.Compnetes.HeaderComponet import *
from Viwes.ClienteViwe import *
class app:
    def __init__(self):
        self.root=tk.Tk()
        self.FrameHead=tk.Frame(self.root)
        self.FrameBody=tk.Frame(self.root)
        
    def App(self):
        CV=ClienteViwe(self.FrameBody)
        HC=HaderApp(self.FrameHead,CV)
        HC.AppInit().pack()
        self.FrameHead.config(bg="lightblue")
        self.FrameHead.config(bd=25)
        self.FrameBody.config(bg="blue")
        self.FrameBody.config(bd=25)
        self.FrameHead.pack()
        self.FrameBody.pack()
        #head
        #/hesd
        #body
        #CV.Viwe()
        #/body
        self.root.geometry("700x600")
        self.root.mainloop()
