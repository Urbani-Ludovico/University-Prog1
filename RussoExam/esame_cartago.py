
class ExamException(Exception):
    pass 


class CSVFile():

    def __init__(self, name=None):
        self.file_name = name

    def get_data(self):
        if not isinstance(self.file_name, str):
            raise ExamException("Il nome del file deve essere una stringa.")
        
        # Controllo eisistenza e leggibilità del file
        try:
            file_content = open(self.file_name)

        # Ottengo le liste dei campi delle singole righe  
            processed_data = [line.strip().split(",") for line in file_content.read().split("\n")]
            file_content.close()
        except Exception as e:
            raise ExamException("Errore! {}".format(e))
        
        return processed_data


class CSVTimeSeriesFile(CSVFile):
    
    def __init__(self, name=None):
        super().__init__(name)

    def get_data(self):
        try:
            file_content = super().get_data()
        except Exception as e:
            raise ExamException("Errore nell'apertura del file! {}".format(e))

        processed_data = []
        prev_epoch = 0

        for line_number, line in enumerate(file_content):
            if len(line) < 2:
                continue
            
            epoch, temperature = line[:2]
            # Controllo per eventuali errori di conversione dei dati
            # In caso non sia possibile, continuo
            try:
                curr_epoch = int(float(epoch))
                temperature = float(temperature)
            except:
               continue
            
            # Controllo se la serie è temporalmente ordinata
            if not prev_epoch < curr_epoch and not line_number == 0:
                raise ExamException("Errore! La serie temporale non è ordinata {} {}".format(prev_epoch, curr_epoch))
             
            prev_epoch = curr_epoch
            processed_data.append([curr_epoch, temperature])

        return processed_data


def utc_day(epoch):
    return epoch - (epoch % 86400)

def compute_daily_max_difference(data):
    
    # Controllo se i dati hanno la forma di una lista
    if not isinstance(data, (list, tuple)):
        raise ExamException("Errore! L'input deve essere una lista")
    
    if len(data) == 0:
        return []
    
    if len(data) == 1:
        return [None]

    current_day = utc_day(data[0][0])
    current_day_temperatures = [data[0][1]]
    processed_data = []

    for element in data[1:]:
        epoch, temperature = element
        #print(current_day_temperatures)
        # Se il giorno non cambia
        if not utc_day(epoch) == current_day:
            if len(current_day_temperatures) == 1:
                processed_data.append(None)
            else:
                processed_data.append(max(current_day_temperatures) - min(current_day_temperatures))
            
            current_day = utc_day(epoch)
            current_day_temperatures = [temperature]
        
        else:
            current_day_temperatures.append(temperature)     

    # Processo gli ultimi elementi della lista
    if current_day_temperatures != []:
        if len(current_day_temperatures) == 1:
            processed_data.append(None)
        else:
            processed_data.append(max(current_day_temperatures) - min(current_day_temperatures))

    return processed_data