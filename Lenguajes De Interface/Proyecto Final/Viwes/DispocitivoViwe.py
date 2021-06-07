import tkinter as tk
from Viwes.Compnetes.DIspocitivoComponete import *
from Data.MysqlData.DispocitivosDataSql import *
from Viwes.RegustarDispocitivo import *

class  DispocitivoViwe:
    def __init__(self,Frame) -> None:
        self.Frame=Frame
        self.FrameViwe= tk.Frame(self.Frame)
        
    def Viwe(self):
        co=0
        DC=DispocitvosSql()
        DatosDispocitivos=DC.Get("SELECT  * FROM dispocitivos")
        btnRegistar=tk.Button(self.FrameViwe,text="Agregar Dispositivo",command=Emergente).pack()
        btnActualizar=tk.Button(self.FrameViwe,text="Actualizar").pack()
        for c in DatosDispocitivos:
            CC=DispocitivoComponete(self.FrameViwe)
            CC.Componete(c["id"],c["dipocitivo"],c["reparacion"],c["cliente"],c["precio"],c["Fecha"]).pack()#.grid(pady=5,row=co , column=0)
            co=co+1
            
        #CC.Componete("0","Debuj","1234567890","debuj 78").pack()
        return self.FrameViwe
def Emergente():
    VR=RegistarDispocitivo()
    VR.VenatanaEmergente()