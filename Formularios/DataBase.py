import sqlite3
from sqlite3.dbapi2 import Cursor
from sqlite3 import Error

def Conexion():
    try:
        conn=sqlite3.connect("Quejas.db")
        return conn
        
    except Error:
        print (Error)
    
def Post(Tupla):
    
    Conn =Conexion()
    Cur=Conn.cursor()
    Cur.execute("""INSERT INTO Quejas(Nombre,Apellido,Ubicacion, Decripcion) VALUES(?,?,?,?)""",Tupla)
    Conn.commit()
    Conn.close()

def Get():
    ListaQuejas=[]
    Conn =Conexion()
    Cur=Conn.cursor()
    Cur.execute('SELECT * FROM Quejas')
    rows = Cur.fetchall()
    for row in rows:
        ListaQuejas.append({"Nombre":row[1],"Apellido":row[2],"Direcion":row[3],"Decripcion":row[4]})
    return ListaQuejas

