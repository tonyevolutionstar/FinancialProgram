""" Product that will be used in facture """
__author__ = "Antonio Ramos"

products_list = []
path_products = 'dados/produtos/produtos.txt'


def error_message(name_p):
    print('O nome ' + name_p + ' nao esta na base de dados\n')
    print('Disponiveis: ')
    for i in range(len(products_list)):
        if products_list[i] is not None:
            print(products_list[i])


def verify_product(name_p):  # verify name in the list of products returns 1 if exists
    verify = 0
    for p in products_list:
        if p == name_p:
            verify = 1

    return verify


def write_info_products(name_p):
    f = open(path_products, 'a')
    f.write(";" + name_p)
    f.close()


def read_info_products():  # read all products from file
    f = open(path_products, 'r')
    line = f.read().split(";")
    for p in line:
        products_list.append(p)
    f.close()
    return products_list

def clean_trash():  # after remove or update one product we got to clean the file and write the products
    f = open(path_products, 'w')
    f.write()
    f.close()


class Products:
    def __init__(self):
        self.products_list = read_info_products()

    """ list all names in database """

    @staticmethod
    def list_products():
        for product in products_list:
            print("product " + str(product))

    def get_list(self):
        return self.products_list

    """when the user wants to add a product to our list"""
    @staticmethod
    def add(name_product):
        products_list.append(name_product)
        write_info_products(name_product)
        return 1

    @staticmethod
    def update(name_product):
        verify = verify_product(name_product)
        if verify == 0:
            error_message(name_product)
            return 0
        else:
            pos = products_list.index(name_product)
            products_list.pop(pos)
            upd_product = input("Qual é a nova designaçao? ")
            products_list.insert(pos, upd_product)
            clean_trash()
            for p in products_list:
                write_info_products(p)
            return 1

    def remove(self, name_product):
        if name_product not in self.products_list:
            error_message(name_product)
            return 0
        else:
            clean_trash()
            self.products_list.remove(name_product)
            for i in self.products_list:
                write_info_products(i)
            return 1
