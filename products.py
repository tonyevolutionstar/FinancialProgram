""" Product that will be used in facture """
__author__ = "Antonio Ramos"

name = []

def error_message():
    print('O nome atual nao esta na base de dados\n')
    print('Disponiveis: ')
    list()


class Products:
    def __init__(self):
        self.name = name

    """ list all names in database """
    def list(self):
        for i in range(len(self.name)):
            if self.name[i] is not None:
                print(self.name[i])

    def get_list(self):
        return self.name

    """when the user wants to add a product to our list"""
    def add(self, name):

        self.name.append(name)
        return 1

    def update(self, name):
        if name not in self.name:
            error_message()
            return 0
        else:
            pos = self.name.index(name)
            self.name.pop(pos)
            self.name.insert(pos, name)
            return 1

    def remove(self, name):
        if name not in self.name:
            error_message()
            return 0
        else:
            self.name.remove(name)
            return 1
