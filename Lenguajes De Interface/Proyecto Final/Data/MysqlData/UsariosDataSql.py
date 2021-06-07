from Data.MysqlData.ConetionDBMysql import Conetion
from Data.MysqlData.UsariosDataSql import *
List=[]
class UsariosSql:
    def __init__(self):
        self.DB=Conetion()
    def Get(self,Query):
        QueryResult = self.DB.Consultas(Query)
        
        for row in  QueryResult:
                if(row[0]!="id"):
                    List.append({"id":row[0],"Usario":row[1],"Pasword":row[2]})
        return List
