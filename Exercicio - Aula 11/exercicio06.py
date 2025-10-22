class Banco:
    def __init__(self, numero_conta:int, balanco:float):
        self.numero_conta = numero_conta
        self.balanco = balanco

    def deposito(self, valor:float)->None:
        self.balanco += valor
        return self.balanco
    
    def retirada(self, valor: float)->None:
        self.balanco -= valor
        return self.balanco
    
    def exibir_saldo(self):
        return f"O saldo da conta {self.numero_conta} é: {self.balanco}"
    

if __name__ == "__main__":
    conta = Banco(22737247, 1000.00)
    conta.deposito(550.00)
    conta.retirada(500.00)
    extrato = conta.exibir_saldo()
    print(extrato)
