""" Product that will be used in facture """
__author__ = "Antonio Ramos"


def verify_product(name_p):  # verify name in the list of products returns 1 if exists
    verify = 0
    for p in products_list:
        if p == name_p:
            verify = 1

    return verify


def read_info_products():  # read all products from file
    f = open(path_products, 'r')
    line = f.read().split(";")
    for p in line:
        products_list.append(p)
    f.close()
    return products_list

def clean_trash():  # after remove or update one product we got to clean the file and write the products
    f = open(path_products, 'w')
    f.write("")
    f.close()


class Products:
    def __init__(self):
        self.products_list = []

    """ list all names in database """
    def list_products(self):
        self.products_list = read_info_products()
        if len(products_list) == 0:
            print("sem produtos na base de dados")
        for product in products_list:
            print("produto " + str(product))

    def get_list(self):
        return self.products_list

    """when the user wants to add a product to our list"""
    def add(self,name_product):
        self.products_list.append(name_product)
        write_info_products(name_product)
        return 1


    def remove(self, name_product):
        if name_product not in self.products_list:
            error_message(name_product)
            return 0
        else:
            clean_trash()
            self.products_list.remove(name_product)
            line = ""
            for i in self.products_list:
                line += i + ";"

            print(line)
            print(line[:-1])
            return 1
