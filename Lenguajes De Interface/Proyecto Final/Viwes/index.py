import tkinter as tk
from Controles.IndexControler import *
from Viwes.LoginViwe import *
class index:
    def ViweMain(self):
        controles = FutionEventIndex()
        app = tk.Tk()
        
        #head
        frameHead = tk.Frame(app, width=700, height=50)
        frameHead.pack()
        frameHead.config(bg="lightblue")
        frameHead.config(bd=25)
        txtNombre = tk.Label(frameHead,text="Comtrol de Verciones")
        txtNombre.grid( row=0 , column=0)
        btnLogin= tk.Button(frameHead,text="Login",command= lambda: index().onBtnLogin(ViweLogin,btnLogin) )
        btnLogin.grid(padx=500,row=0 , column=2)
        #/head
        #body
        frameBody = tk.Frame(app ,width=700, height=700)
        frameBody.pack()
        frameBody.config(bg="blue")
        frameBody.config(bd=25)
        ViweLogin = Login(frameBody)
        
        #/body
        app.geometry("700x600")
        app.mainloop()
        
    def onBtnLogin(self,viweLogin,btnLogin):
        viweLogin.Viwe().pack() 
        btnLogin['state'] = tk.DISABLED
