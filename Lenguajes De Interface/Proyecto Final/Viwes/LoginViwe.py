import tkinter as tk
from Controles.LoginControler import *
from Viwes.index import *
from Modules.Userobjet import *
from Viwes.app import *

class Login:
    def __init__(self,root):
        self.root=root
    def Viwe(self):
        frame = tk.Frame(self.root) 
        txtUsuario = tk.Label(frame , text="Usuario")
        iptUsuario = tk.Entry(frame)
        btnEtar= tk.Button(frame,text="Entrar", width=10,height=1, command= lambda: onBtnEntar(iptPasword,iptUsuario,frame))
        txtPasword = tk.Label(frame , text="Password")
        iptPasword = tk.Entry(frame, show="*")
        txtUsuario.grid(padx=5,row=1 , column=1)
        iptUsuario.grid(padx=5,row=1 , column=2)
        txtPasword.grid(padx=5,row=2 , column=1)
        iptPasword.grid(padx=5,row=2 , column=2)
        btnEtar.grid(padx=5, row=3, column=1)
        return frame
def onBtnEntar(iptPasword,iptUsuario,frame):
    varPasword=iptPasword.get()
    varUario=iptUsuario.get()
    varAhut= AhutUser.Ahout(varUario,varPasword)
    if(varAhut):
        frame.destroy()
        App=app()
        App.App()

