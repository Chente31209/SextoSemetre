import Tkinter as tk 
from Modulos.Fucioes import *

def btnComprar():
    X = txtNuemro1.get()
    Y = txtNuemro2.get()
    
    RM1["text"]=ComparcionMenor(X,Y)
    RM2["text"]= ComparcionMayor(X,Y)
    
    print("El Menor es " + ComparcionMenor(X,Y))
    print("El Mayor es " + ComparcionMayor(X,Y))
    
root = tk.Tk()
LibNuero1= tk.Label(root, text="Nuemero 1")
txtNuemro1 = tk.Entry(root)
LibNuero2= tk.Label(root, text="Nuemero 2")
txtNuemro2 = tk.Entry(root)
btnComparar= tk.Button(root,text="Comprar", command=btnComprar)
btnSalir= tk.Button(root,text="Salir", command = quit)
LibNuero1M = tk.Label(root, text="Numero Mayor")
LibNuero2M = tk.Label(root, text="Numero Menor")

RM1= tk.Label(root, text="Numero Mayor")
RM2= tk.Label(root, text="Numero Menor")

LibNuero1.grid(row=1 , column=1)
LibNuero2.grid(row=2 , column=1)
txtNuemro1.grid(row=1 , column=2)
txtNuemro2.grid(row=2 , column=2)
btnComparar.grid(row=3 , column=2)
btnSalir.grid(row=8 , column=6)
LibNuero1M.grid(row=4 , column=1)
LibNuero2M.grid(row=5 , column=1)
RM1.grid(row=4 , column=2)
RM2.grid(row=5 , column=2)

root.geometry("300x300")
root.mainloop()