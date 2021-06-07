import tkinter as tk
from Data.MysqlData.DispocitivosDataSql import *

class RegistarDispocitivo:
    def __init__(self):
        self.root=tk.Tk()
    def VenatanaEmergente(self):
        #Id,Nombre,No. Telefono,Direcion
        txtDispocitvo=tk.Label(self.root,text="Dispositivo").grid(padx=20,row=2 , column=2)
        txtReparacion=tk.Label(self.root,text="Reparacion").grid(padx=20,row=4 , column=2)
        txtCniente=tk.Label(self.root,text="Cliente").grid(padx=20,row=6 , column=2)
        txtPrecio=tk.Label(self.root,text="Precio").grid(padx=20,row=8 , column=2)
        txtFecha=tk.Label(self.root,text="Fecha").grid(padx=20,row=10 , column=2)

        inpNombre=tk.Entry(self.root,width=30)
        inpTelefono=tk.Entry(self.root,width=30)
        inpDirecion=tk.Entry(self.root,width=30)
        inpPrecio=tk.Entry(self.root,width=30)
        inpFecha=tk.Entry(self.root,width=30)

        inpNombre.grid(padx=20,row=3 , column=2)
        inpTelefono.grid(padx=20,row=5 , column=2)
        inpDirecion.grid(padx=20,row=7 , column=2)
        inpPrecio.grid(padx=20,row=9 , column=2)
        inpFecha.grid(padx=20,row=11 , column=2)

        btnAgreagra=tk.Button(self.root,text="Agregar",command=lambda:Regustar(self.root,inpNombre.get(),inpTelefono.get(),inpDirecion.get(),inpPrecio.get(),inpFecha.get()))
        btnAgreagra.grid(padx=1,row=12 , column=2,columnspan=1)

        btnCanselar=tk.Button(self.root,text="Cancelar",command=lambda:Canselar(self.root)).grid(padx=1,row=13 , column=2)
        self.root.geometry("225x290")
        self.root.mainloop()
def Regustar(root,Dipocitivo,Reparacion,Cliente,Precio,Fecha):
    CP=DispocitvosSql()
    if Dipocitivo !="" and Reparacion !="":
        CP.Post(Dipocitivo,Reparacion,Cliente,Precio,Fecha)
        root.destroy()
    else:
        print ("Lo siento ")
    
def Canselar(root):
    root.destroy()
