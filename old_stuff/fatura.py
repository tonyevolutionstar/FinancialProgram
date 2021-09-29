from provider import Provider

class Fatura:
    def verify_provider(self, forn):
        pass



    def __init__(self, id, desc, date, forn, iva, qtd, precolitro):
        self.id = id
        self.description = desc #descricao
        self.date = date #data
        self.forn = self.verify_provider(forn) #fornecedores -> provider
        self.IVA = iva
        self.qtd = qtd
        self.precolitro = precolitro
        self.preco = qtd*precolitro


