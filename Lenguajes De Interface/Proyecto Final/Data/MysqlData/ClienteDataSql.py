from Data.MysqlData.UsariosDataSql import *
List=[]
class ClienteSql:
    def __init__(self):
        self.DB=Conetion()
    def Get(self,Query):
        QueryResult = self.DB.Consultas(Query)
        
        for row in  QueryResult:
                if(row[0]!="id"):
                    List.append({"id":row[0],"Nombre":row[1],"Telefono":row[2],"Direccion":row[3]})
        return List
    def Post(self,Nombre,NoTelefono,Direcion):
        self.DB.Modificar(" INSERT  INTO  clientes(Nombre,NoTelefono,Direcion) VALUES('{0}','{1}','{2}')".format(Nombre,NoTelefono,Direcion))
    
    def Update(self,Nombre,NoTelefono,Direcion,Id):
        #print("update clientes set Nombre = '{0}', NoTelefono='{1}',Direcion='{2}' WHERE id= {3};".format(Nombre,NoTelefono,Direcion,Id))
        self.DB.Modificar("update clientes set Nombre = '{0}', NoTelefono='{1}',Direcion='{2}' WHERE id= {3};".format(Nombre,NoTelefono,Direcion,Id))
        pass
    
    def Dilite(self, txt):
        #print("DELETE FROM clientes WHERE id = {0};".format(txt))
        self.DB.Modificar("DELETE FROM clientes WHERE id = {0};".format(txt))
        pass


