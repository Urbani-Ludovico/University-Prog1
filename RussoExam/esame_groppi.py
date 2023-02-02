class ExamException(Exception):
    pass

class CSVFile():
    def __init__(self,name):
        self.name=name # non facciamo controlli sul nome perché si fanno nel get_data
                    
class CSVTimeSeriesFile(CSVFile):
    
    def get_data(self):
        try:
            file=open(self.name)
            for linea in file:
                pass
            file.close()
        except:
            raise ExamException('nome file non valido')
        myfile=open(self.name, 'r')
        lista=[]
        for line in myfile:
            element=line.split(',')
            try:
                # creazione lista di dati e sanitizzazione di questi
                # se uno dei dati non è dei casi previsti esce dal tray e la riga non viene aggiunta
                element[1]=element[1].strip()
                element[0]=element[0].strip()
                element[0]=int(float(element[0]))
                element[1]=float(element[1])
                lista.append([element[0], element[1]])
            except:
                pass
            # nel momento in cui un timestamp è fuori norma il get_data viene fermato
            if len(lista)>2 and lista[-1][0]<=lista[-2][0]:
                myfile.close()
                raise ExamException('timestamp fuori ordine')
            elif len(lista)==2 and lista[1][0]<=lista[0][0]:
                myfile.close()
                raise ExamException('timestamp fuori ordine')
        myfile.close()
        return lista

def compute_daily_max_difference(lista):
    if not isinstance(lista, list):
        raise ExamException('{} non è una lista'.format(lista))
    if len(lista) == 0:
        return []
    temp_data=[lista[0]]
    ris=[]
    for line in range(1,len(lista)):
        if int(temp_data[0][0]/86400)==int(lista[line][0]/86400):
        # controlliamo se i dati presi prima sono della stessa giornata di quelli in esame
            temp_data.append(lista[line])
        else:
            if len(temp_data)==1:
                ris.append(None)
            else:
                massimo=temp_data[0][1] # assumiamo il primo valore come massimo e minimo
                minimo=temp_data[0][1]
                for dato in temp_data:
                    if dato[1]>massimo:
                        massimo=dato[1]
                    if dato[1]<minimo:
                        minimo=dato[1]
                ris.append(massimo-minimo)
            temp_data=[lista[line]]
            # alla fine modifichiamo la temp_data e ci mettiamo solo la lista[line]
    # alla fine del ciclo calcolo l'ultima giornata
    if len(temp_data)==1:
        ris.append(None)
    else:
        massimo=temp_data[0][1] # assumiamo il primo valore come massimo e minimo
        minimo=temp_data[0][1]
        for dato in temp_data:
            if dato[1]>massimo:
                massimo=dato[1]
            if dato[1]<minimo:
                minimo=dato[1]
        ris.append(massimo-minimo)
    return ris
        
    # controllo che sia una lista
    # è dato per assunto che la lista 
    # ciclando su tutte le righe della lista data
    # prendo il primo giorno di una giornata e creo una lista con tutte le rilevazioni di una giornata
# my_file=CSVTimeSeriesFile('data.txt')
# lista=my_file.get_data()
# print('ecco la lista {}  fine lista'.format(lista))
# ris=compute_daily_max_difference(lista)
# print(ris)
