class User:
    def __init__(self, name, lastname):
        self.name =name
        self.lastname = lastname

    def nombreCompleto(self):
        return '({} {})' .format(self.name , self.lastname)
