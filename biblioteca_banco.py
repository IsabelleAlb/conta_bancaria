class Banco:
    def __init__(self, numero, nome, tipo):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.saldo = 0
        self.limite = 0


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
            self.limite = self.limite + valor_limite

        else:
            print("conta inativa")


    def depositar(self, valor_dep):
        if self.status == True:
            self.saldo = self.saldo + valor_dep
            print("Depósito efetuado com sucesso!")

        else:
            print("conta inativa")

    def sacar(self, valor_saq):
        if self.status == True:
            self.saldo = self.saldo - valor_saq
            print("saque efetuado com sucesso!")
        else:
            print("conta inativa")


    def verificarSaldo(self):
        if self.status == True:
            print(f"seu saldo atual é R${self.saldo}")

        else:
            print("conta inativa")
