import csv
from typing import List

# Creo una classe CSVFile per rappresentare un file CSV
class CSVFile:
    # Il metodo __init__ inizializza un'istanza di CSVFile con un nome del file
    def __init__(self, name):
        self.name = name

    # Metodo per leggere il file CSV
    def read_csv(self):
        try:
            # Apro il file
            with open(self.name) as csvfile:
                # Leggo il contenuto del file usando il lettore del modulo csv
                reader = csv.reader(csvfile)
                # Prendo ogni riga nel file e la memorizzo nell'elenco dei dati
                data = [row for row in reader]
            # Resturno l'elenco dei dati: data
            return data
        # Se il file non esisto, stampo l'errore a schermo
        except FileNotFoundError:
            print(f"File '{self.name}' non esiste")
        # Per qualsiasi altro tipo di errore, stampa un messaggio di errore personalizzato con i dettagli dell'errore
        except Exception as e:
            print(f"Si è verificato un errore durante la lettura del file '{self.name}': {e}")
        return []

# Creo una classe CSVTimeSeriesFile che eredita da CSVFile
class CSVTimeSeriesFile(CSVFile):
    # Metodo per ottenere i dati dal file CSV
    def get_data(self):
        data = self.read_csv()
        if data:
            time_series = []
            for row in data[1:]: # ignoriamo la prima riga che rappresenta le intestazioni
                epoch = int(row[0])
                temperature = float(row[1])
                time_series.append([epoch, temperature])
            return time_series
        return []

# Funzione per calcolare la differenza massima giornaliera
def compute_daily_max_difference(time_series: List[List[int]]) -> List[float]:
    daily_max_differences = []
    day = {}
    for timestamp, temperature in time_series:
        date = timestamp // 86400 # un giorno ha 86400 secondi
        if date not in day:
            day[date] = (temperature, temperature)
        else:
            day[date] = (min(day[date][0], temperature), max(day[date][1], temperature))
    for (min_temp, max_temp) in day.values():
        daily_max_differences.append(max_temp - min_temp)
    return daily_max_differences

# Creo un'istanza di CSVTimeSeriesFile
time_series_file = CSVTimeSeriesFile(name='data.csv')

# Ottengo i dati dal file
time_series = time_series_file.get_data()
print(time_series)