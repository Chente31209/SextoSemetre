from Data.MysqlData.UsariosDataSql import *

class AhutUser:
    def Ahout(User,pasword):
        db=UsariosSql().Get("SELECT * FROM usarios")
        for users in db:
            if(users["Usario"]==User):
                if(users["Pasword"]==pasword):
                    result= True
                    break
                else:
                    result=False
            else:
                result = False
        return result