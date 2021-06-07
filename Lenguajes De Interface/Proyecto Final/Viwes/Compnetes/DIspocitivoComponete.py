import tkinter as tk
from Viwes.UpDateDispocitivo import *
from Data.MysqlData.DispocitivosDataSql import *

class  DispocitivoComponete:
    def __init__(self,Frame) -> None:
        self.Frame=Frame
        self.FrameComponete= tk.Frame(self.Frame)


    def Componete(self,Id,Dipocitivo,Reparacion,Cliente,Precio,Fecha):
        txtId=tk.Label(self.FrameComponete,text=Id)
        txtDipocitivo=tk.Label(self.FrameComponete,text=Dipocitivo)
        txtReparacion=tk.Label(self.FrameComponete,text=Reparacion)
        txtCliente=tk.Label(self.FrameComponete,text=Cliente)
        txtPrecio=tk.Label(self.FrameComponete,text=Precio)
        txtFecha=tk.Label(self.FrameComponete,text=Fecha)
        btnEliminar = tk.Button(self.FrameComponete,text="Eliminar",command=lambda:Elininar(self.FrameComponete,Id))
        btnEditar = tk.Button(self.FrameComponete,text="Editar", command=lambda:Editar(Id,Dipocitivo,Reparacion,Cliente,Precio,Fecha))

        txtId.grid(padx=5,row=0 , column=0)
        txtDipocitivo.grid(padx=5,row=0 , column=1)
        txtReparacion.grid(padx=5,row=0 , column=2)
        txtCliente.grid(padx=5,row=0 , column=3)
        txtPrecio.grid(padx=5,row=0 , column=4)
        txtFecha.grid(padx=5,row=0 , column=4)
        btnEliminar.grid(padx=5,row=0 , column=6)
        btnEditar.grid(padx=5,row=0 , column=7)
        return self.FrameComponete
def Editar(Id,Dipocitivo,Reparacion,Cliente,Precio,Fecha):
    UD=UpDateDispocitivo()
    UD.VenatanaEmergente(Id,Dipocitivo,Reparacion,Cliente,Precio,Fecha)
    pass
def Elininar(root,Id):
    DS= DispocitvosSql()
    DS.Delite(Id)
    root.destroy()
    pass 