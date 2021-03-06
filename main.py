__author__ = "Antonio Ramos"

import sys
import os
import datetime

from client import Client  # name, nif, email, phone
from provider import Provider  # name, nif, email, phone
from file import Database  # type, info

list_providers = []
list_sells = []
list_buys = []
list_clients = []
list_faturas = []

# paths files
path_clientes = 'dados/clientes/clientes.txt'
path_providers = 'dados/fornecedores/fornecedores.txt'# doesnt exist yet
path_buyers = 'dados/compras/'  # doesnt exist yet
path_products = 'dados/produtos/produtos.txt'


def custo_fifo(buy, sell):
    pass

def verify_buy(buy, fatura, provider):
    pass

def verify_sell(sell):
    pass

def add_provider(name, nif, email, phone):
    Provider(name, nif, email, phone)

# write information on file type + information
def add_info_into_file(type_, info_):
    return Database(type_, info_)

def success_message():
    print("Dados gravados com sucesso\n")

# principal menu, input option output submenu
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
    print("\t\t3 - Apagar")
    print("\t\t4 - Listar")
    print("-------- Adicionar Opcao ------------\n")
    return int(input())


# Este menu é para as vendas e compras de produtos com faturas
def sub_menu2():
    print("--------------------------------------")
    print("\t\t0 - Voltar")
    print("\t\t1 - Adicionar")
    print("-------- Adicionar Opcao ------------\n")
    return int(input())


def confirm_menu(selection, tipo):
    print("--------------------------------------")
    print("Escolheste " + str(selection) + " para " + tipo)
    print("\nDesejas:")
    print("\t\t0 - Cancelar")
    print("\t\t1 - Confirmar")
    print("-------- Adicionar Opcao ------------\n")
    return int(input())

# information regarding clients and providers
def info():
    print("Adicione o nome")
    nome = input()
    print("Adicione o nif")
    nif = int(input())
    print("Adicione o mail")
    email = input()
    print("Adicione o telefone")
    tel = int(input())
    return nome, nif, email, tel

def add_info_client():
    print("Estrutura Cliente nome, nif, email, telefone")
    nome, nif, email, tel = info()
    client = Client(nome, nif, email, tel)
    op_client = confirm_menu(client.__dict__, "clientes")

    if op_client == 1:
        add_info_into_file("clientes", nome + "," + str(nif) + "," + email + "," + str(tel))
    return op_client


# clients and providers
def split_info(line):
    return line.split(",")

# read all clients and returns a list, to verify a name
def read_clients():
    clients = []
    with open(path_clientes, 'r') as file_object:
        lines = file_object.readlines()

    for line in lines:
        clients.append(line.strip())

    return clients

# verify a client_name to update info client, return 1 or 0, if exists, and the fields of the user to alter,
# return all list of users to write on file, again
def verify_existed_clients(client_name):
    clients = read_clients()
    info_client = ""
    verify = 0
    for client in clients:
        client_n = client.split(",")
        if client_n[0].casefold() == client_name.casefold():
            verify = 1
            info_client = client

    return verify, info_client, clients


def update_info_client():
    parameters = ["nome", "nif", "email", "telefone"]
    print("\nQual é o cliente a alterar?\n")
    client_name = input()
    verify, info_client, clients = verify_existed_clients(client_name.strip())

    if verify == 0:
        list_info_client()
        update_info_client()
    else:
        clients.remove(info_client)
        previous_inf = ""

        print("Que parametro deseja alterar(0-nome, 1-nif, 2-email, 3-telefone)\n")
        i_client = info_client.split(",")

        choice = int(input())
        if choice == 0: # nome
            print("Info " + info_client)
            print("Para que nome deseja atualizar?\n")
            new_nome = input()
            for c_i in range(1, len(i_client)):
                previous_inf += i_client[c_i] + ","

            new_info_client = new_nome + "," + previous_inf[:-1]
            option = confirm_menu(new_info_client, "nome")
            if option == 1:
                clients.append(new_info_client)
                write_info_client(clients)
            else:
                update_info_client()
        elif choice == 1:   # nif
            print("Info " + info_client)
            print("Para que nif deseja atualizar?\n")
            new_nif = input()
            print("nome " + info_client[0])
            new_info_client_nif = i_client[0] + "," + new_nif + "," + i_client[2] + "," + i_client[3]
            option = confirm_menu(new_info_client_nif, "nif")
            if option == 1:
                clients.append(new_info_client_nif)
                write_info_client(clients)
            else:
                update_info_client()
        elif choice == 2:   # email
            print("Info " + info_client)
            print("Para que email deseja atualizar?\n")
            new_email = input()
            new_info_email = i_client[0] + "," + i_client[1] + "," + new_email + "," + i_client[3]
            option = confirm_menu(new_info_email, "email")
            if option == 1:
                clients.append(new_info_email)
                write_info_client(clients)
            else:
                update_info_client()
        elif choice == 3:   # phone
            print("Info " + info_client)
            print("Para que numero de telefone ou telemovel deseja alterar?\n")
            new_phone = input()
            new_info_phone = i_client[0] + "," + i_client[1] + "," + i_client[2] + "," + new_phone
            option = confirm_menu(new_info_phone, "telefone")
            if option == 1:
                clients.append(new_info_phone)
                write_info_client(clients)
            else:
                update_info_client()
        else:
            print("Parametros possiveis " + str(parameters) + "\n")
            update_info_client()


# write all again the information altered
def write_info_client(clients):
    with open(path_clientes, 'w') as file_object:
        for c in clients:
            file_object.write(c + "\n")


def list_info_client():
    print("Clients existentes\n")
    with open(path_clientes, 'r') as file_object:
        lines = file_object.readlines()

    for line_c in lines:
        print(line_c.strip())


def add_info_fornecedor():
    print("Estrutura Fornecedor nome, nif, email, telefone")
    nome, nif, email, tel = info()

    forn = Provider(nome, nif, email, tel)
    op_fornecedor = confirm_menu(forn.__dict__, "fornecedores")

    if op_fornecedor == 1:
        add_info_into_file("fornecedores", nome + "," + str(nif) + "," + email + "," + str(tel))

    return op_fornecedor

def list_info_fornecedor():
    files = os.listdir(path_providers)

    for file in files:
        f = open(os.path.join(path_providers, file), 'r')
        print(f.read())
        f.close()

def list_products():
    products_list = []
    f = open(path_products, 'r')
    line_p = f.read().split(",")
    for p_list in line_p:
        products_list.append(p_list)
    f.close()

    return products_list

def error_message(products_list, name_p):
    print('O nome ' + name_p + ' nao esta na base de dados\n')
    print('Disponíveis: ')
    for error_p in range(len(products_list)):
        if products_list[error_p] is not None:
            print(products_list[p])


def write_info_product(info_product):
    file = open(path_products, 'w', encoding='utf8')
    for l_p in list_products():
        file.write(l_p + ",")
    file.write(info_product)
    success_message()
    file.close()

def write_info_product_update(info_product):
    file = open(path_products, 'w', encoding='utf8')
    file.write(info_product)
    success_message()
    file.close()


def add_info_product():
    print("Qual é o produto a adicionar?")
    new_product = input()
    op_product = confirm_menu(new_product, "product")

    return op_product, new_product

def verify_product(name_product):  # verify name in the list of products returns 1 if exists
    verify = 0
    for product in list_products():
        if product == name_product:
            verify = 1

    return verify, list_products()

def clean_trash():  # after remove or update one product we got to clean the file and write the products
    f = open(path_products, 'w')
    f.write("")
    f.close()

def verify_file_buy(path_file):
    list_buy = []

    if not os.path.isfile(path_file):
        return list_buy
    else:
        f = open(path_file, 'r')
        line_b = f.read()
        for b_list in line_b:
            list_buy.append(b_list)
        f.close()
    return list_buy

def add_info_buy(path):
    list_previous_buys = verify_file_buy(path)

    print("Qual é o produto a adicionar?\n")
    products_list = list_products()
    for product in products_list:
        print(str(products_list.index(product)) + " - " + product)
    print("-------- Adicionar Opcao ------------\n")
    op_product = int(input())
    product_choose = products_list[op_product]
    print("Qual o numero de litros ? ")
    qtd = int(input())
    print("Qual é o preço/litro ? ")
    price_liter = float(input())
    price = round(qtd * price_liter, 2)

    print("Deseja adicionar mais à base de dados?(1-Sim, 0-Nao) ")
    list_buys.append(product_choose + "," + str(qtd) + "," + str(price_liter) + "," + str(price) + "\n")

    op_ = int(input())
    if op_ == 1:
        add_info_buy(path)
    else:
        f = open(path, 'w')
        for x in list_previous_buys:
            f.write(x)

        for y in list_buys:
            f.write(y)

        f.close()


def automatic_option():
    today_date = datetime.datetime.now().strftime('%m_%d_%Y')
    path_buyers_automatic = path_buyers + "compras_" + today_date + ".txt"
    add_info_buy(path_buyers_automatic)


def manual_option():
    print("Qual é a data a utilizar?(DD/MM/YYYY)")
    date_string = input()
    format_ = "%d/%m/%Y"
    try:
        datetime.datetime.strptime(date_string, format_)
        new_format_date = date_string.split("/")
        new_date = new_format_date[1] + "_" + new_format_date[0] + "_" + new_format_date[2]
        path_buyers_manual = path_buyers + "compras_" + new_date + ".txt"
        add_info_buy(path_buyers_manual)
    except ValueError:
        print("O formato da data está mal, devia ser DD/MM/YYYY")
        manual_option()


def add_info_buys():
    print("--------------------------------------")
    print("Deseja adicionar \n")
    print("0 - Automaticamente?")
    print("1 - Manual?")
    print("-------- Adicionar Opcao ------------\n")
    type_option = int(input())
    if type_option == 0:
        automatic_option()
    elif type_option == 1:
        manual_option()

def add_info_sells():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # fatura = Fatura(1,'Negocio','2021-08-03','Galp',6,1000,1.5487)

    # tests write file
    # test_file("compras",2000)

    princ = 0  # 0 -> menu, 1 -> sub menu

    while princ == 0:
        op = menu()
        if op == 0:
            sys.exit(1)
        elif op == 1:  # clientes
            sub_op = sub_menu()
            if sub_op == 0:
                princ = 0
            elif sub_op == 1:  # add name, nif, email, phone
                while add_info_client() == 0:
                    continue
            elif sub_op == 2:
                update_info_client()
            elif sub_op == 4:  # list
                list_info_client()
                sub_op = sub_menu()
        elif op == 2:  # providers
            sub_op = sub_menu()
            if sub_op == 0:
                princ = 0
            elif sub_op == 1:  # add name, nif, email, phone
                while add_info_fornecedor() == 0:
                    continue
            elif sub_op == 4:  # list
                list_info_fornecedor()
                sub_op = sub_menu()
        elif op == 3:   # buys
            sub_op2 = sub_menu2()
            if sub_op2 == 0:
                menu()
            else:
                add_info_buys()
        elif op == 4:
            sub_op2 = sub_menu2()
        elif op == 5:  # product
            sub_op = sub_menu()
            if sub_op == 0:
                princ = 0
            elif sub_op == 1:   # Designação
                stop, new_p = add_info_product()
                if stop == 0:
                    sub_op = 0
                else:
                    write_info_product(new_p)
            elif sub_op == 2:  # update
                print("Qual é o produto que quer alterar?")
                name_p = input()
                stop, list_product = verify_product(name_p)
                if stop == 0:
                    error_message(list_product, name_p)
                else:
                    pos = list_product.index(name_p)
                    list_product.pop(pos)
                    print("Qual é a nova designaçao?")
                    upd_product = input()
                    conf = confirm_menu(upd_product, "produto")
                    if conf == 0:
                        sub_op = 0
                    else:
                        list_product.insert(pos, upd_product)
                        clean_trash()
                        line = ""
                        for p in list_product:
                            line += p + ','
                        write_info_product_update(line[:-1])
            elif sub_op == 3:   # delete
                print("Qual é o produto a eliminar?")
                name_p = input()
                stop, list_product = verify_product(name_p)
                if stop == 0:
                    error_message(list_product, name_p)
                else:
                    pos = list_product.index(name_p)
                    list_product.pop(pos)
                    line = ""
                    for p in list_product:
                        line += p + ','
                    write_info_product_update(line[:-1])
            elif sub_op == 4:   # list
                for i in list_products():
                    print(i)
