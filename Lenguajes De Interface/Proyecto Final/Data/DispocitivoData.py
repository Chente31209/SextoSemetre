import csv
ListaUsarios=[]
class DispocitivoData:
    def TodosLosDispocitivo(self):
        with open('Data\\Dipocitivo.csv') as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if(row[0]!="id"):
                    #id,dipocitivo,reparacion,cliente,precio,fecha
                    ListaUsarios.append({"id":row[0],"dipocitivo":row[1],"reparacion":row[2],
                    "cliente":row[3],"precio":row[4],"Fecha":row[5]})
        return ListaUsarios
d= DispocitivoData()
print(d.TodosLosDispocitivo())