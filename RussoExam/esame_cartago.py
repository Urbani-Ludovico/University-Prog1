
class ExamException(Exception):
    pass 

class CSVFile():

    def __init__(self, file_name=None):
        self.file_name = file_name

    def get_data(self):
        if not isinstance(self.file_name, str): ### ADD not ### moved from __init__
            raise ExamException("Il nome del file deve essere una stringa.")
        
        # processed_data = []
        try:
            file_content = open(self.file_name)
        except Exception as e:
            raise ExamException("Errore! {}".format(e))

        processed_data = [item.split(",") for item in file_content.read().split("\n")]
        # for line in file_content: ### REMOVED enumerate
        #     file_line = line.strip().replace("\n","").split(",")
        #     processed_data.append(file_line)
        
        file_content.close() ### ADD
        
        return processed_data ### ADD


class CSVTimeSeriesFile(CSVFile):
    
    def __init__(self, fileName=None):
        super().__init__(fileName) ## CHANGED to super

    def get_data(self):
        try:
            file_content = super().get_data()  ## CHANGED to super
        except Exception as e:
            raise ExamException("Errore nell'apertura del file! {}".format(e))

        processed_data = []
        prev_epoch = 0

        for line_number, line in enumerate(file_content):
            if len(line) < 2:
                continue
            
            epoch, temperature = line[:2]
            if not isinstance(epoch, (int,float)) or not isinstance(temperature, (int,float)):
                continue
            
            if not epoch - prev_epoch > 0 or not line_number == 0:
                raise ExamException("Errore! La serie temporale non è ordinata")
             
            prev_epoch = epoch
            processed_data.append([int(float(epoch)), float(temperature)])
            
        return processed_data ### ADD


def day(epoch):
    return epoch - (epoch % 86400)


def compute_daily_max_difference(data):
    if not isinstance(data, list):
        raise ExamException("Errore! L'input deve essere una lista")
    
    if len(data) < 2:
        return [None]

    current_day = data[0][0]
    current_day_temperatures = [data[0][1]]
    processed_data = []

    for element in data[1:]:
        epoch, temperature = element[:2]
        if not isinstance(epoch, int) or not isinstance(temperature, float):
            continue

        if day(epoch) == current_day:
            current_day.append(temperature)
        
        else:
            current_day = day(epoch)
            if len(current_day_temperatures) == 1:
                processed_data.append(None)
            else:
                processed_data.append(max(current_day_temperatures) - min(current_day_temperatures))
                current_day_temperatures = []
        
        return processed_data