import csv
ListaClientes=[]
class ClienteData:
    def TodosLosClientes(self):
        with open('Data\\Cliente.csv') as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if(row[0]!="Id"):
                    ListaClientes.append({"id":row[0],"Nombre":row[1],"Telefono":row[2],"Direccion":row[3]})
        return ListaClientes