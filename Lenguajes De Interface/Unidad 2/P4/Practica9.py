from Tkinter import *
import random as rm
def graficar ():
    for i in range(0,9):
        X1= rm.randint(50,200)
        Y1= rm.randint(50,200)
        X2= rm.randint(50,200)
        Y2= rm.randint(50,200)
        figura.create_line(X1, Y1, X2, Y2,width=1,fill='blue')
def limpiar():
    figura

ventana = Tk()
btnGraficar= Button(ventana, text= "Graficar", command = graficar)
btnLimpia= Button(ventana, text= "limpiar", command = limpiar)
btnGraficar.pack()
figura = Canvas(ventana, width=300,height=250)

figura.pack()
btnLimpia.pack()

figura.mainloop()