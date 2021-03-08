import  Tkinter as tk
from Modulos.Fucioes import *

def multiplos():
    n=Entrdad.get()
    Nf=float(n)
    Ni=int(Nf) 
    r=Multiplos(Ni)
    resultado["text"]=r
root = tk.Tk()
Entrdad = tk.Entry(root)
resultado = tk.Label(root)
btnMultiplos = tk.Button(root,text="Multiplos", command=multiplos)

Entrdad.pack()
btnMultiplos.pack()
resultado.pack()

root.geometry("300x300")
root.mainloop()