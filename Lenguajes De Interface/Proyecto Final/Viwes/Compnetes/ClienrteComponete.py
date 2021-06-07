import tkinter as tk
from Data.MysqlData.ClienteDataSql import *
from Viwes.UpDateClientes import *
class  ClienteComponete:
    def __init__(self,Frame) -> None:
        self.Frame=Frame
        self.FrameComponete= tk.Frame(self.Frame)

    def Componete(self,Id,Nombre,NoTelefono,Direcion):
        txtId=tk.Label(self.FrameComponete,text=Id)
        txtNombre=tk.Label(self.FrameComponete,text=Nombre)
        txtNoTelefono=tk.Label(self.FrameComponete,text=NoTelefono)
        txtDirecion=tk.Label(self.FrameComponete,text=Direcion)
        btnEliminar = tk.Button(self.FrameComponete,text="Eliminar", command=lambda:OnEliminar(txtId["text"],self.FrameComponete) )
        btnEditar = tk.Button(self.FrameComponete,text="Editar",command=lambda:OnUpDate(Id,Nombre,NoTelefono,Direcion))
        
        txtId.grid(padx=5,row=0 , column=0)
        txtNombre.grid(padx=5,row=0 , column=1)
        txtNoTelefono.grid(padx=5,row=0 , column=2)
        txtDirecion.grid(padx=5,row=0 , column=3)
        btnEliminar.grid(padx=5,row=0 , column=4)
        btnEditar.grid(padx=5,row=0 , column=5)
        return self.FrameComponete

def OnEliminar(txt,Comm):
    x= int(txt)
    CD= ClienteSql()
    CD.Dilite(x)
    Comm.destroy()
    pass
def OnUpDate(Id,Nombre,NoTelefono,Direcion):
    print(Id)
    UC  = UpDateClietes()
    UC.VenatanaEmergente(Id,Nombre,NoTelefono,Direcion)
    pass