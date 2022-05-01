from writer import Writer
class RegisterSpartans:
    def __init__(self,company, filename = None) -> None:
        self.__company = company
        self.__spartans = company.get_spartans()
        self.__database = Writer((filename or company.get_name())+'.csv','a')

    def create_headers(self):
        self.__database.insert(['Spartan Name','Company Name'])

    def save(self):
        for spartan in self.__spartans:
            self.__database.insert([
                self.__company.get_name(),
                spartan.get_name(),
            ])
        self.__database.close()

