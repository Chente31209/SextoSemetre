import Tkinter as tk 
from Modulos.Fucioes import *


def Calcularbtn():
    PrimerNumero= N1.get()
    SegundoNumero= N2.get()
    VarN1= strAint(PrimerNumero)
    VarN2= strAint(SegundoNumero)
    varAnd= VarN1 and VarN2
    varOr= VarN1 or VarN2
    varXor= VarN1 ^ VarN2
    txtNuemtos["text"]= PrimerNumero +" " + SegundoNumero
    txtAnd["text"]= str(varAnd)  
    txtOr["text"] = str(varOr )
    txtXor["text"] = str(varXor)




root = tk.Tk()
root.geometry("300x300")
#
N1 = tk.Entry(root)
N2 = tk.Entry(root)
txtNuemtos= tk.Label(root)
txtAnd = tk.Label(root)
txtOr= tk.Label(root)
txtXor = tk.Label(root)
btnFuncon = tk.Button(root, text = "Calular" ,command =Calcularbtn)

N1.pack()
N2.pack()
btnFuncon.pack()
txtNuemtos.pack()
txtAnd.pack()
txtOr.pack()
txtXor.pack()


root.mainloop()
