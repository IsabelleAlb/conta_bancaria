class Banco:
    def __init__(self, numero, nome, tipo):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.saldo = 0
        self.limite = 0
        self.novo_limite = 0


    def ativarConta(self):
        if self.status == False:
            self.status = True
            print("sua conta está ativa. você já pode movimentar")

        else:
            print("conta já está ativa")


    def desativarConta(self):
        if self.status == True:
            if self.saldo == 0:
                self.status = False
                print("conta desativada")
            else:
                print("não foi possível desativar sua conta!"
                      " por favor verifique seu saldo")


    def ativarLimite(self, valor_limite):
        if self.status == True:
            self.limite += valor_limite

        else:
            print("conta inativa")


    def depositar(self, valor_dep):
        if self.status == True:
            self.saldo += valor_dep
            print("Depósito efetuado com sucesso!")

        else:
            print("conta inativa")


    def sacar(self, valor_saq):
        if self.status == True:
            if valor_saq <= self.saldo:
                self.saldo = self.saldo - valor_saq

            elif valor_saq > self.saldo:
                self.novo_limite = (self.limite + self.saldo) - valor_saq
                self.limite = (self.limite - self.novo_limite) * (-1)
                self.saldo = -1

            print("saque efetuado com sucesso!")
        else:
            print("conta inativa")


    def verificarSaldo(self):
        if self.status == True:
            if self.saldo >= 0:
                print(f"Seu saldo atual é R${self.saldo} e R${self.limite} de crédito especial")
            else:
                print(f"Seu saldo atual é R${self.limite} e você ainda possui R${self.novo_limite} de crédito especial")

        else:
            print("conta inativa")
