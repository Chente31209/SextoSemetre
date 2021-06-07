import tkinter as tk
def Revisar(Frame,No,Ap,De,Ub):
    Queja=tk.Frame(Frame)
    Nombre=tk.Label(Queja,text=No).pack()
    Apellido=tk.Label(Queja,text=Ap).pack()
    Dercipcion=tk.Label(Queja,text=De).pack()
    Ubicacion=tk.Label(Queja,text=Ub).pack()
    Linea=tk.Label(Queja,text="_________________________________________").pack()
    return Queja
    