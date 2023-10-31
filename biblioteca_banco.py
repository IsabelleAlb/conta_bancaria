class Banco:
    def __init__(self, numero, saldo, nome, tipo, status, limite):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = status
        self.limite = limite

    def depositar(self):
        valor_dep = float(input("qual o valor de depósito? "))
        total_dep = self.saldo + valor_dep
        return total_dep


    def sacar(self):
        valor_saq = float(input("qual valor deseja sacar? "))
        total_saq = self.saldo - valor_saq
        return total_saq

    def ativarConta(self):
        if self.status == False:
            pergunta = input("deseja ativar sua conta? s/n")
            if pergunta == "sS":
                self.status = True
                print("conta ativa")
            else:
                print("conta inativa")
        else:
            pergunta = input("deseja desativar sua conta? s/n")
            if pergunta == "sS":
                self.status = False
                print("conta inativa")
            else:
                print("conta ativa")

    def verificarSaldo(self):
        saldo_total = self.limite + (self.depositar() - self.sacar())
        return saldo_total
