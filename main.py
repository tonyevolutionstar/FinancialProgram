__author__ = "Antonio Ramos"

import sys
import os

from products import Products
from fatura import Fatura  # id, desc, date, forn, iva, qtd, precolitro
from buy import Buy  # qtd, date
from sell import Sell  # qtd, date
from client import Client  # name, nif, email, phone
from provider import Provider  # name, nif, email, phone
from file import Database  # type, info

list_providers = []
list_sells = []
list_buys = []
list_clients = []
list_faturas = []

product = Products()


def custo_fifo(buy, sell):
    pass


def verify_buy(buy, fatura, provider):
    pass


def verify_sell(sell):
    pass


def add_provider(name, nif, email, phone):
    provider = Provider(name, nif, email, phone)


def add_info_into_file(tp, mem):
    return Database(tp, mem)


# principal menu, input opcao output submenu
def menu():
    print("--------------------------------------")
    print("-------- Financial program -----------")
    print("-------- Menu ------------------------")
    print("\t\t0 - Sair")
    print("\t\t1 - Clientes")
    print("\t\t2 - Fornecedores")
    print("\t\t3 - Compras")
    print("\t\t4 - Vendas")
    print("\t\t5 - Produtos")
    print("\t\t6 - Fazer Custo Fifo")
    print("-------- Adicionar Opcao ------------\n")
    return int(input())


def sub_menu():
    print("--------------------------------------")
    print("\t\t0 - Voltar")
    print("\t\t1 - Adicionar")
    print("\t\t2 - Alterar")
    print("\t\t3 - Remover")
    print("\t\t4 - Listar")
    print("-------- Adicionar Opcao ------------\n")
    return int(input())


# este menu é para as vendas e compras de produtos com faturas
def sub_menu_2():
    pass


def confirm_menu(selection, tipo):
    print("----------------------")
    print("Escolheste " + str(selection) + " para " + tipo)
    print("\nDesejas:")
    print("0 - Cancelar")
    print("1 - Confirmar")
    print("---- Adicionar Opcao -----\n")

    return int(input())


def info():
    nome = input("Adicione o nome")
    nif = int(input("Adicione o nif"))
    email = input("Adicione o mail")
    tel = int(input("Adicione o telefone"))

    return nome, nif, email, tel


def add_info_client():
    print("Estrutura Cliente nome, nif, email, telefone")

    nome, nif, email, tel = info()
    client = Client(nome, nif, email, tel)
    op_client = confirm_menu(client.__dict__, "clientes")

    if op_client == 1:
        add_info_into_file("clientes", client.__dict__)

    return op_client


def list_info_client():
    path = 'dados/clientes/'
    files = os.listdir(path)

    for file in files:
        f = open(os.path.join(path, file), 'r')
        print(f.read())
        # do what you want
        f.close()


def add_info_fornecedor():
    print("Estrutura Fornecedor nome, nif, email, telefone")
    nome, nif, email, tel = info()

    forn = Provider(nome, nif, email, tel)
    op_fornecedor = confirm_menu(forn.__dict__, "fornecedores")

    if op_fornecedor == 1:
        add_info_into_file("fornecedores", forn.__dict__)

    return op_fornecedor


def list_info_fornecedor():
    your_path = 'dados/fornecedores/'
    files = os.listdir(your_path)

    for file in files:
        f = open(os.path.join(your_path, file), 'r')
        print(f.read())
        # do what you want
        f.close()



def add_info_buys():
    pass


def add_info_sells():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # fatura = Fatura(1,'Negocio','2021-08-03','Galp',6,1000,1.5487)

    # tests write file
    # test_file("compras",2000)

    princ = 0  # 0 -> menu, 1 -> sub menu
    cancel = 0

    while princ == 0:
        op = menu()
        if op == 0:
            sys.exit(1)
        elif op == 1:  # clientes
            sub_op = sub_menu()
            if sub_op == 0:
                princ = 0
            elif sub_op == 1:  # add name, nif, email, phone
                while cancel == 0:
                    cancel = add_info_client()
            elif sub_op == 4:  # list
                list_info_client()
                sub_op = sub_menu()
        elif op == 2:  # providers
            sub_op = sub_menu()
            if sub_op == 0:
                princ = 0
            elif sub_op == 1:  # add name, nif, email, phone
                while cancel == 0:
                    cancel = add_info_fornecedor()
            elif sub_op == 4:  # list
                list_info_fornecedor()
                sub_op = sub_menu()
        elif op == 5:  # product
            sub_op = sub_menu()
            if sub_op == 0:
                princ = 0
            elif sub_op == 1:  # add name, nif, email, phone
                while cancel == 0:
                    name_p = input('Qual é o produto a adicionar?')
                    cancel = confirm_menu(name_p, "product")
                    product = Products()
                    product.add(name_p)

            elif sub_op == 2:
                name_p = input("Qual é o produto que quer alterar? ")
                product.update(name_p)
            elif sub_op == 3:

                name_p = str(input("Qual é o produto a eliminar?")).strip()
                product.remove(name_p)
            elif sub_op == 4:
                product.list_products()
