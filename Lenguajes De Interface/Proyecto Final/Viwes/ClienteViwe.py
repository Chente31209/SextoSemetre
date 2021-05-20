import tkinter as tk
from Viwes.Compnetes.ClienrteComponete import *
from Data.ClientesData import *


class  ClienteViwe:
    def __init__(self,Frame) -> None:
        self.Frame=Frame
        self.FrameViwe= tk.Frame(self.Frame)
        


    def Viwe(self):
        co=0
        DC=ClienteData()
        DatosClientes=DC.TodosLosClientes()
        
        for c in DatosClientes:
            CC=ClienteComponete(self.FrameViwe)
            CC.Componete(c["id"],c["Nombre"],c["Telefono"],c["Direccion"]).pack()#.grid(pady=5,row=co , column=0)
            co=co+1
            
        #CC.Componete("0","Debuj","1234567890","debuj 78").pack()
        
        return self.FrameViwe
