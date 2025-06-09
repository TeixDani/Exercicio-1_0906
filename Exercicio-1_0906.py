class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Bernardo", 24)

def InfoPessoa():
    print(f"\nNome: ", pessoa1.nome,
          "\nIdade: ", pessoa1.idade)

p = InfoPessoa()
