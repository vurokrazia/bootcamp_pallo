import csv

class Writer:
    def __init__(self, file_name, type = 'w'):
        self.__data = []
        self.__file = open(file_name, type)
        self.__writer = csv.writer(self.__file)
    
    def insert(self,data): 
        self.__data.append(data) # [1, 2]
        self.__writer.writerow(data) # [1], [2]
    
    def close(self):
        self.__file.close()