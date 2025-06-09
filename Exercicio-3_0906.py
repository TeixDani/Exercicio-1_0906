class ContaBancaria:
    def __init__(self, cpf, nome, saldo):
        self.cpf = cpf
        self.nome = nome
        self.saldo = saldo


    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"\nVocê efetuou um depósito de R${valor:.2f}.")
        else:
            print("\nValor digitado incorretamente.")


    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"\nVocê sacou R${valor:.2f}.")
        elif valor > self.saldo:
            print("\nSaldo insuficiente.")
        else:
            print("\nValor digitado incorretamente.")


    def ver_saldo(self):
        print(f"\nSaldo atual de {self.nome}: R${self.saldo:.2f}")


pessoa1 = ContaBancaria("14", "Luís", 1500)


cpf = input("Informe o CPF: ")


if cpf == pessoa1.cpf:
    metodo = input("\nPor qual método você deseja prosseguir? (1) Depositar (2) Sacar (3) Ver saldo\n")

    if metodo == "1":
        valor = float(input("\nInforme o valor do depósito: "))
        pessoa1.depositar(valor)

    elif metodo == "2":
        valor = float(input("\nInforme o valor do saque: "))
        pessoa1.sacar(valor)

    elif metodo == "3":
        pessoa1.ver_saldo()

    else:
        print("\nOpção inválida.")

else:
    print("\nCPF não encontrado.")

print("\n!Conta atualizada!\n",
      "\nCpf: ", pessoa1.cpf,
      "\nNome: ", pessoa1.nome,
      "\nSaldo: ", pessoa1.saldo)