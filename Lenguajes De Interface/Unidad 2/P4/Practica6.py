import tkinter as tk 
from Modulos.Fucioes import *
def btnAcion():
    Plabra = ""
    PlabraD = ""
    Valortxt1=txtNumeroMayor.get()
    Valortxt2=txtNumeroMenor.get()

    Nmin=strAint(Valortxt1)
    Nmax=strAint(Valortxt2)
    dcremeto =Nmax
    for i in range(Nmin,Nmax+1):
        Plabra = Plabra + " "+ str(i)
        PlabraD = PlabraD  +" "+ str(dcremeto)
        dcremeto = dcremeto-1
    RsultadoN["text"]=Plabra
    RsultadoI["text"]=PlabraD

root = tk.Tk()
txtNumeroMayor = tk.Entry(root)
txtNumeroMenor = tk.Entry(root)
btnSusecion =tk.Button(root, text="Secuencia", command= btnAcion)
RsultadoN=tk.Label(root)
RsultadoI=tk.Label(root)
txtNumeroMayor.pack()
txtNumeroMenor.pack()
btnSusecion.pack()
RsultadoN.pack()
RsultadoI.pack()
root.geometry("300x300")
root.mainloop()