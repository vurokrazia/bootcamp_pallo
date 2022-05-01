class Company:
    def __init__(self, name):
        self.__name = name
        self.__spartans = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    
    def get_spartans(self):
        return self.__spartans

    def add_spartan(self, spartan):
        self.__spartans.append(spartan)

    def find_spartan_by_name(self, name):
        for spartan in self.__spartans:
            if(spartan.get_name() == name):
                return spartan
        return False
