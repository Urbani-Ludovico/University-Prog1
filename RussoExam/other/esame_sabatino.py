import os

def check_existance(file): # funzione che controlla se il file esiste
    if os.path.exists(file):
        return True # se esiste ritorno vero
    else:
        return False # altrimenti falso

class ExamException(Exception): # classe ExamException che estende Exception
    pass

def clean_line(line): # funzione che controlla se la riga è 'pulita', la userò dopo per stabilire cosa aggiungere alla lista da ritornare
    try: # controllo se posso castare a numerici i valori
        line[0] = int(float(line[0])) # l'epoch deve essere un intero
        line[1] = float(line[1]) # la temperatura invece un float
        return True # se entrambi i cast sono andati a buon fine ritorno vero
    except Exception: # se invece incorro in un'eccezione
        return False # ritorno falso, ignorerò questa riga

class CSVTimeSeriesFile: # definisco la classe che ritornerà la lista time_series con i valori estratti dal CSV
    def __init__(self, name=None): # l'unico parametro è il nome del file
        self.name = name 

    def get_data(self): # funzione che estrae i dati e ritorna una lista
        if not isinstance(self.name, str): # se il nome non è una stringa
            raise ExamException('Errore! nome del file non valido') # alzo un'eccezione
        
        if not check_existance(self.name): # se il file non esiste
            raise ExamException('Errore! file non trovato') # alzo un'eccezione

        try: # provo ad aprire il file
            file = open(self.name, 'r')
            file.readline() # leggo la prima riga
        except Exception as e:
            raise ExamException('Errore! file non leggibile: ', e) # se non riesco alzo un'eccezione
            
        data = [] # lista in cui salverò i dati

        prev_epoch = None # variabile in cui salverò l'epoch precedente, alla prima iterazione non c'è un precedente e quindi è None

        for line in file: # leggo linea per linea il file
            elements = line.split(',') # divido gli elementi in base alla virgola
            elements[-1] = elements[-1].strip() # faccio lo strip dal campo -1
            if clean_line(elements): # se la linea è 'pulita', allora posso aggiungere gli elementi
                current_epoch = elements[0] # l'epoch corrente è quello di posto 0, lo userò per controllare che la lista sia in ordine
                if prev_epoch != None and current_epoch <= prev_epoch: # se il precedente non è None e gli epoch non sono ordinati
                    raise ExamException('Errore! lista non ordinata') # alzo l'eccezione
                else: # altrimenti, se gli epoch sono in ordine cronologico
                    prev_epoch = current_epoch # switcho il precedente con il corrente per proseguire col controllo alla prossima iterazione
                    elements = elements[0 : 2] # salvo solo i primi due elementi, così da risolvere il problema dei campi aggiuntivi
                    data.append(elements) # aggiungo gli elementi alla lista data
            else: # altrimenti, se la mia linea non era 'pulita'
                continue # vado avanti con l'esecuzione senza salvare quei dati

        file.close() 
        return data # ritorno la lista finale

def convert_day(epoch): # funzione che ritorna solo il giorno rappresentato da un epoch
    return epoch - (epoch%86400)

def compute_daily_max_difference(time_series):
    final_list = [] # lista finale in cui salverò le escursioni termiche
    counter = 0 # contatore per le righe della time_series
    while counter < len(time_series): # itero finché non arrivo alla fine della lista 
        tmp_list = [] # lista temporanea per le temperature di un singolo giorno
        current_day = convert_day(time_series[counter][0]) # converto l'epoch di inizio al solo giorno 
        tmp_list.append(time_series[counter][1]) # aggiungo la temperatura associata 
        for i in range(counter + 1, len(time_series)): # itero sui successivi
            day = convert_day(time_series[i][0]) # converto ogni epoch a giorno
            if day == current_day: # controllo se il giorno è lo stesso
                tmp_list.append(time_series[i][1]) # aggiungo la temperatura associata alla lista temporanea
            else: # se non sto più lavorando sullo stesso giorno
                break # esco dal for interno
        counter += len(tmp_list) + 1 # salto le righe che appartenevano allo stesso giorno e ricomincio dalla successiva
        if len(tmp_list) > 1: # se avevo più di una misurazione per un dato giorno
            final_list.append(max(tmp_list)-min(tmp_list)) # aggiungo la differenza massima
        else: 
            final_list.append(None) # altrimenti aggiungo None
    return final_list # ritorno la lista delle escursioni termiche giornaliere               

# my_file = CSVTimeSeriesFile(name='data.csv')
# time_series = my_file.get_data()
# print('lista dei dati:\n', time_series)

# diff_list = compute_daily_max_difference(time_series)
# print('lista delle escursioni termiche giornaliere:\n', diff_list)