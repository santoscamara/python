class Conta:
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        
    def exibir_saldo(self):
        print(f"Saldo: R${self.saldo:.2f}")

conta1 = Conta(1, "Maria", 1000)
conta1.depositar(500)
conta1.exibir_saldo()