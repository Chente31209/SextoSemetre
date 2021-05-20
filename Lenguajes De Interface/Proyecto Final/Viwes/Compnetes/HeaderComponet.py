import tkinter as tk
from tkinter.constants import E
from Viwes.Compnetes.HeaderComponet import *
class Hader:
    def __init__(self,Frame,ViweLogin):
        self.Frame =Frame
        self.ViweLogin = ViweLogin
    def Init(self):
        FrameHeader=tk.Frame(self.Frame)
        txtNombre = tk.Label(FrameHeader,text="Comtrol de Verciones")
        txtNombre.grid( row=0 , column=0)
        btnLogin= tk.Button(FrameHeader,text="Login",command= lambda: onBtnLogin(self.ViweLogin,btnLogin) )
        btnLogin.grid(padx=500,row=0 , column=2)
        return FrameHeader
def onBtnLogin(viweLogin,btnLogin):
    viweLogin.Viwe().pack() 
    btnLogin['state'] = tk.DISABLED


class HaderApp:
    def __init__(self,Frame,Cliente):
        self.Frame=Frame
        self.Cliente = Cliente
    def AppInit(self):
        SingletonCliente =self.Cliente.Viwe()
        FrameHeader=tk.Frame(self.Frame)
        txtNombre = tk.Label(FrameHeader,text="Comtrol de Verciones")
        txtNombre.grid( row=0 , column=0)
        btnInicio= tk.Button(FrameHeader,text="Inicio",command= lambda: BtnInicio(SingletonCliente) )
        btnInicio.grid(padx=5,row=0 , column=1)
        btnCliente= tk.Button(FrameHeader,text="Cliente",command= lambda: BtnClientes(SingletonCliente) )
        btnCliente.grid(padx=5,row=0 , column=2)
        btnProducto= tk.Button(FrameHeader,text="Producto",command= lambda: BtnInicio(SingletonCliente) )
        btnProducto.grid(padx=5,row=0 , column=3)
        return FrameHeader
def BtnClientes(Cliente):
    try:
        Cliente.pack()
    except NameError:
        print("Error detecado"+NameError)

def BtnDispocitivos(Cliente):
    Cliente.pack_forget()

def BtnInicio(Cliente):
    Cliente.pack_forget()

