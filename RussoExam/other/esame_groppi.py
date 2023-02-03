class ExamException(Exception):
    pass

class CSVFile():
    def __init__(self,name):
        self.name=name # non facciamo controlli sul nome perché si fanno nel get_data
                    
class CSVTimeSeriesFile(CSVFile):
    
    def get_data(self):
        try: # test validità del file
            file=open(self.name, 'r')
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
            if len(lista)>2 and lista[-1][0]<=lista[-2][0]: # verifica validità ultimo dato
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
    line=iter(lista)
    temp_data=[line]
    ris=[]
    if line[0]<0:
        line=next(lista)
        while line[0]<0:
            if int(temp_data[0][0]/86400)==int(lista[line][0]/86400):
                temp_data.append(lista[line])
            else:
                if len(temp_data)==1:
                    ris.append(None)
                else:
                    num=diff_max_min_lista(temp_data)
                    ris.append(num)
                temp_data=[lista[line]]
                
            temp_data.append(line)
    for line in range(1,len(lista)):
        if int(temp_data[0][0]/86400)==int(lista[line][0]/86400):
        # controlliamo se i dati presi prima sono della stessa giornata di quelli in esame
            temp_data.append(lista[line])
        else:
            if len(temp_data)==1:
                ris.append(None)
            else:
                num=diff_max_min_lista(temp_data)
                ris.append(num)
            temp_data=[lista[line]]
            # alla fine modifichiamo la temp_data e ci mettiamo solo la lista[line]
    # alla fine del ciclo calcolo l'ultima giornata
    if len(temp_data)==1:
        ris.append(None)
    else:
        num=diff_max_min_lista(temp_data) # si calcola un ultima volta il maxmin sull'ultima giornata
        ris.append(num)
    return ris

def diff_max_min_lista(lista):
    massimo=lista[0][0]
    minimo=lista[0][0]
    for i in lista:
        if i[1]<minimo:
            minimo=i[1]
        if i[1]>massimo:
            massimo=1[1]
    return(massimo-minimo)