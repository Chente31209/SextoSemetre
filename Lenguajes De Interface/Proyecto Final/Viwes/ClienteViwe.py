import tkinter as tk
from Viwes.Compnetes.ClienrteComponete import *
from Data.MysqlData.ClienteDataSql import *
from Viwes.RegustarClientes import *

class  ClienteViwe:
    def __init__(self,Frame) -> None:
        self.Frame=Frame
        self.FrameViwe= tk.Frame(self.Frame)
        
    def Viwe(self):
        btnRegistar=tk.Button(self.FrameViwe,text="Agregar Cliente",command=Emergente).pack()
        Car=Cargar(self.FrameViwe)
        Car.pack()
        btnActualizar=tk.Button(self.FrameViwe,text="Actualizar",command=lambda: Actualisar(self.FrameViwe)).pack()
        
        return self.FrameViwe

def Emergente():
    VR=RegistarClietes()
    VR.VenatanaEmergente()

def Cargar(FrameViwe):
    tabla=tk.Frame(FrameViwe)
    DC=ClienteSql()
    DatosClientes=DC.Get("SELECT  * FROM clientes")
    co=0
    for c in DatosClientes:
        CC=ClienteComponete(tabla)
        CC.Componete(c["id"],c["Nombre"],c["Telefono"],c["Direccion"]).pack()#.grid(pady=5,row=co , column=0)
        co=co+1
    return tabla
    pass

def all_children (wid) :
    _list = wid.winfo_children()
    #print(_list)
    """
    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
"""
    return _list

def Actualisar(FrameViwe):
    
    cunt=0
    list=all_children(FrameViwe)
    for i in list:
        cunt=cunt+1
    
    if cunt == 3:
        Lista=list[1]
        Tabla = all_children(Lista)
        for i in Tabla:
            print(i)
        ListaTabla=all_children(Tabla[0])
        for i in ListaTabla:
            print(i["text"])
        
    pass 