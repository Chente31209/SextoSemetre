import tkinter as tk
from tkinter.constants import E
from Viwes.Compnetes.HeaderComponet import *
class Hader:
    def __init__(self,Frame,ViweLogin):
        self.Frame =Frame
        self.ViweLogin = ViweLogin
    def Init(self):
        FrameHeader=tk.Frame(self.Frame)
        txtNombre = tk.Label(FrameHeader,text="control de versiones")
        txtNombre.grid( row=0 , column=0)
        btnLogin= tk.Button(FrameHeader,text="Login",command= lambda: onBtnLogin(self.ViweLogin,btnLogin) )
        btnLogin.grid(padx=500,row=0 , column=2)
        return FrameHeader
def onBtnLogin(viweLogin,btnLogin):
    viweLogin.Viwe().pack() 
    btnLogin['state'] = tk.DISABLED


class HaderApp:
    def __init__(self,Frame,Cliente,Dispocitivo):
        self.Frame=Frame
        self.Cliente = Cliente
        self.Dispocitivo=Dispocitivo
    def AppInit(self):
        SingletonCliente =self.Cliente.Viwe()
        SingletonDispocitivo = self.Dispocitivo.Viwe()
        FrameHeader=tk.Frame(self.Frame)
        txtNombre = tk.Label(FrameHeader,text="control de versiones")
        txtNombre.grid( row=0 , column=0)
        btnInicio= tk.Button(FrameHeader,text="Inicio",command= lambda: BtnInicio(SingletonCliente,SingletonDispocitivo) )
        btnInicio.grid(padx=5,row=0 , column=1)
        btnCliente= tk.Button(FrameHeader,text="Cliente",command= lambda: BtnClientes(SingletonCliente,SingletonDispocitivo) )
        btnCliente.grid(padx=5,row=0 , column=2)
        btnProducto= tk.Button(FrameHeader,text="Dispositivo",command= lambda: BtnDispocitivos(SingletonCliente,SingletonDispocitivo) )
        btnProducto.grid(padx=5,row=0 , column=3)
        return FrameHeader
def BtnClientes(Cliente,Dispocitivo):
    try:
        Cliente.pack()
        Dispocitivo.pack_forget()
    except NameError:
        print("Error detecado"+NameError)

def BtnDispocitivos(Cliente,Dispocitivo):
    Cliente.pack_forget()
    Dispocitivo.pack()
def BtnInicio(Cliente,Dispocitivo):
    Cliente.pack_forget()
    Dispocitivo.pack_forget()

