def strAint(Numero):
    NFloat=float(Numero)
    NInt=int(NFloat)
    return NInt
    
def ComparcionMayor (A,B):
    if(A<B):
        return A+""
    if(A>B):
        return B+""
    else:
        return A+""

def ComparcionMenor (A,B):
    if(A>B):
        return A+""
    if(A<B):
        return B+""
    else:
        return A+""

def Multiplos(n):
    
    cont=1
    strResultado =" "
    for i in range(0,n):
        if(cont==3):
            IS=i
            I=str(IS+1)
            strResultado= strResultado + I + "-"
            cont=1
        else:
            cont=cont+1
    return strResultado 


