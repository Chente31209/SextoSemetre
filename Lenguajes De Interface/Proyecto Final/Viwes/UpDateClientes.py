import tkinter as tk
from tkinter.constants import S
from typing import Text
from Data.MysqlData.ClienteDataSql import *

class UpDateClietes:
    def __init__(self):
        self.root=tk.Tk()
        
    def VenatanaEmergente(self,Id,Nombre,NoTelefono,Direcion):
        txtNombre=tk.Label(self.root,text="Nombre")
        txtTelefono=tk.Label(self.root,text="Telefono")
        txtDirecion=tk.Label(self.root,text="Direcion")
        
        txtNombre.grid(padx=20,row=1 , column=2)
        txtTelefono.grid(padx=20,row=3 , column=2)
        txtDirecion.grid(padx=20,row=5 , column=2)

        inpNombre=tk.Entry(self.root,width=30)
        inpTelefono=tk.Entry(self.root,width=30)
        inpDirecion=tk.Entry(self.root,width=30)

        inpNombre.grid(padx=20,row=2 , column=2)
        inpTelefono.grid(padx=20,row=4 , column=2)
        inpDirecion.grid(padx=20,row=6 , column=2)

        txtNombre["text"]=Nombre
        txtTelefono["text"]=NoTelefono
        txtDirecion["text"]=Direcion
        
        
        btnAgreagra=tk.Button(self.root,text="Modificar",command=lambda:Regustar(self.root,Id,inpNombre.get(),inpTelefono.get(),inpDirecion.get()))
        btnAgreagra.grid(padx=1,row=7 , column=2,columnspan=1)

        btnCanselar=tk.Button(self.root,text="Cancelar",command=lambda: Canselar(self.root)).grid(padx=1,row=8 , column=2)
        self.root.geometry("225x225")
        self.root.mainloop()


def Regustar(root,Id,Nombre,NoTelefono,Direcion):
    x=str(Nombre)
    y=str(NoTelefono)
    z=str(Direcion)
    b=int(Id)
    print(b)

    CP=ClienteSql()
    if x !="" and y !="" and z !="":
        CP.Update(x,y,z,b)
        root.destroy()
    else:
        print ("Lo siento ")
    
def Canselar(root):
    root.destroy()