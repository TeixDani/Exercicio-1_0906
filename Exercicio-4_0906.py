class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = Carro("Fiat", "Modelo", 2006)

def infoCarro(carro):
    print("\nMarca: ", carro.marca,
          "\nModelo: ", carro.modelo,
          "\nAno: ", carro.ano)

c = infoCarro(carro1)