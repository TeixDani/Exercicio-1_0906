class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

produto1 = Produto("Arroz", 23.00, 250)

print("\nProduto: ", produto1.nome,
      "\nPreço: ", produto1.preco,
      "\nQuantidade: ", produto1.quantidade)

def valorTotal():
    return produto1.preco * produto1.quantidade
print("\nValor total de estoque: ", valorTotal())