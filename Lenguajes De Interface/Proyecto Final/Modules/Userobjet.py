from Data.UsariosData import *

class AhutUser:
    def Ahout(User,pasword):
        db=UsersData.TodosLosUsarios()
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