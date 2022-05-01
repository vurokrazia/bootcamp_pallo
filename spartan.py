class Spartan:

    def __init__(self,  name, last_name ='', casco ='',   equipamiento ='',  voz ='',  sexo ='', antebrazo ='',   rodilleras ='',    stikers ='',    banderas='',   color_visor=''):
        self.__name = name
        self.__last_name = last_name
        self.__casco = casco
        self.__equipamiento = equipamiento
        self.__voz = voz
        self.__sexo = sexo
        self.__antebrazo = antebrazo
        self.__rodilleras = rodilleras
        self.__stikers = stikers
        self.__banderas = banderas
        self.__color_visor = color_visor
    
    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_antebrazo(self):
        return self.__antebrazo

    def get_full_name(self):
        return self.__name + " " + self.__last_name
