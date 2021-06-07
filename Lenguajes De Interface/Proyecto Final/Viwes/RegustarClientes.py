import tkinter as tk
from Data.MysqlData.ClienteDataSql import *

class RegistarClietes:
    def __init__(self):
        self.root=tk.Tk()
        
    def VenatanaEmergente(self):
        txtNombre=tk.Label(self.root,text="Nombre").grid(padx=20,row=1 , column=2)
        txtTelefono=tk.Label(self.root,text="Telefono").grid(padx=20,row=3 , column=2)
        txtDirecion=tk.Label(self.root,text="Direccion").grid(padx=20,row=5 , column=2)

        
        inpNombre=tk.Entry(self.root,width=30)
        inpTelefono=tk.Entry(self.root,width=30)
        inpDirecion=tk.Entry(self.root,width=30)

        inpNombre.grid(padx=20,row=2 , column=2)
        inpTelefono.grid(padx=20,row=4 , column=2)
        inpDirecion.grid(padx=20,row=6 , column=2)

        btnAgreagra=tk.Button(self.root,text="Agregar",command=lambda:Regustar(inpNombre.get(),inpTelefono.get(),inpDirecion.get(),self.root)).grid(padx=1,row=7 , column=2,columnspan=1)
        btnCanselar=tk.Button(self.root,text="Cancelar",command=lambda: Canselar(self.root)).grid(padx=1,row=8 , column=2)
        self.root.geometry("225x225")
        self.root.mainloop()


def Regustar(Nombre,Telefono,Direcion,root):
    x=str(Nombre)
    y=str(Telefono)
    z=str(Direcion)

    CP=ClienteSql()
    if x !="" and y !="" and z !="":
        CP.Post(x,y,z)
        root.destroy()
    else:
        print ("Lo siento ")
    
def Canselar(root):
    root.destroy()