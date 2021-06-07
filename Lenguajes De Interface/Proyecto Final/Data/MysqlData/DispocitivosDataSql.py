from Data.MysqlData.UsariosDataSql import *
List=[]
class DispocitvosSql:
    def __init__(self):
        self.DB=Conetion()
    def Get(self,Query):
        QueryResult = self.DB.Consultas(Query)
        
        for row in  QueryResult:
                if(row[0]!="id"):
                    List.append({"id":row[0],"dipocitivo":row[1],"reparacion":row[2],
                    "cliente":row[3],"precio":row[4],"Fecha":row[5]})
        return List

    def Post(self,Dipocitivo,Reparacion,Cliente,Precio,Fecha):
        self.DB.Modificar("INSERT INTO dispocitivos(dipocitivo,reparacion,id_cliente,precio,fecha) VALUES('{0}','{1}',{2},'{3}','{4}')".format(Dipocitivo,Reparacion,Cliente,Precio,Fecha))
        pass
    def UpDate(self,Id,Dipocitivo,Reparacion,Cliente,Precio,Fecha):
        self.DB.Modificar("UPDATE  dispocitivos SET dipocitivo='{1}',reparacion='{2}',id_cliente={3},precio='{4}',fecha='{5}' WHERE id = {0};".format(Id,Dipocitivo,Reparacion,Cliente,Precio,Fecha))
        pass
    def Delite(self,ID):
        self.DB.Modificar("DELETE  FROM dispocitivos WHERE id={0};".format(ID))
        pass

