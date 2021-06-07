import csv

ListaUsarios=[]
class UsersData:
    def TodosLosUsarios():
        with open('Data\\Usarios.csv') as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if(row[0]!="id"):
                    ListaUsarios.append({"id":row[0],"Usario":row[1],"Pasword":row[2]})
        return ListaUsarios