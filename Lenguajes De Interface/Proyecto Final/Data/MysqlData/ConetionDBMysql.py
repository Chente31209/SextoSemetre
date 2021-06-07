import pymysql 

class Conetion:
    def __init__(self) -> None:
        self.host="localhost"
        self.port=3306
        self.user="root"
        self.passwd="osoosa123"
        self.db="control_de_verciones"
        self.conn = pymysql.connect(
                                host=self.host, port=self.port, user=self.user,
                                passwd=self.passwd, db= self.db)
        self.cursor = self.conn.cursor()

    def Consultas(self,Query):
        self.cursor.execute(Query)
        result = self.cursor.fetchall()
        self.conn.close()
        return result
        
    def Modificar(self,Query):
        self.cursor.execute(Query)
        self.conn.commit()
        self.conn.close()

#P= Conetion().Modificar("INSERT INTO clientes VALUES("")")#Consultas("SELECT * FROM usarios")
#print(P)