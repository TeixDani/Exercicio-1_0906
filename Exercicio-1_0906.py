class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Bernardo", 24)

print(f"Olá, eu sou {pessoa1.nome} e tenho {pessoa1.idade} anos!!!")