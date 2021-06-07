import tkinter as tk
from DataBase import *
from Quejas import *
def Admin():
    root=tk.Tk()
    body1=tk.Frame(root)
    body1.pack()
    
    root.title("Quejas")
    Quejas=Get()
    for Queja in Quejas:
        Revisar(body1,Queja["Nombre"],Queja["Apellido"],Queja["Direcion"],Queja["Decripcion"]).pack()
    root.config(background = "Red")
    root.geometry("500x500")
    root.mainloop()
    pass

def OnClick(inpNombre,inpApellidos,inpDirecion,inpDescriocion):
    Nombre=inpNombre.get()
    Apellido=inpApellidos.get()
    Direcion=inpDirecion.get()
    Decricion=inpDescriocion.get()
    if Nombre!="" and Apellido!="" and Direcion!="" and Decricion!="":
        Post((Nombre,Apellido,Direcion,Decricion))
    Admin()
    pass

def app():
    root=tk.Tk()
    body=tk.Frame()
    body.pack()
    root.title("Quejas")
    Formulario(body).pack()
    root.config(background = "Red")
    root.geometry("500x500")
    root.mainloop()

def Formulario(Body):
    FQueja=tk.Frame(Body)
    txtNombre=tk.Label(FQueja,text="Nombre").pack()
    inpNombre=tk.Entry(FQueja)
    inpNombre.pack()
    txtApellido=tk.Label(FQueja,text="Apellido").pack()
    inpApellidos=tk.Entry(FQueja)
    inpApellidos.pack()
    txtDirecion=tk.Label(FQueja,text="Direcion").pack()
    inpDirecion=tk.Entry(FQueja)
    inpDirecion.pack()
    txtUbicacion=tk.Label(FQueja,text="Decripcion").pack()
    inpDescriocion=tk.Entry(FQueja)
    inpDescriocion.pack()
    btnEnviar= tk.Button(FQueja,text="Enviar",command=lambda:OnClick(inpNombre,inpApellidos,inpDirecion,inpDescriocion)).pack()
    return FQueja
    

if __name__=="__main__":
    app()