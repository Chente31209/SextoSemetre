import Tkinter as tk 
from Modulos.Fucioes import *


def btnfuncon():
    sumaPar=0
    SumaImpar=0
    MultiPar=1
    MualtiImpar=1
    n=RntryN.get()
    if(n==""):
        print "esta vacio"
    else:
        N= strAint(n)
        for i in range(1,N+1):
            r=i%2
            if(r==0):    
                txtPares["text"]=txtPares["text"] + " " +str(i)
                sumaPar = sumaPar + i
                MultiPar= MultiPar * i
            else:
                txtImpares["text"]=txtImpares["text"] + " " +str(i)
                SumaImpar = SumaImpar + i
                MualtiImpar=MualtiImpar * i
        txtMultiplicacion["text"]="suam de pares = "+str(sumaPar)+" suma impares ="+str(SumaImpar)
        txtSuama["text"]= "Multiplicacion pares ="+str(MultiPar)+" Multiplicacion pares ="+str(MualtiImpar)




root = tk.Tk()
root.geometry("300x300")
#
RntryN = tk.Entry(root)
txtPares= tk.Label(root)
txtImpares = tk.Label(root)
txtSuama= tk.Label(root)
txtMultiplicacion = tk.Label(root)
btnFuncon = tk.Button(root, text = "Calular" ,command=btnfuncon)

RntryN.pack()
btnFuncon.pack()
txtPares.pack()
txtImpares.pack()
txtSuama.pack()
txtMultiplicacion.pack()


root.mainloop()
