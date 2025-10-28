class Funcionario:
    def __init__(self, nome:str, email: str, salario: float)->None:
        self.nome = nome
        self.email = email
        self.salario = salario
    
    def calcula_salario(self, horas_trabalhadas:float)->None:
        valor_hora = self.salario / horas_trabalhadas
        return f'Salario: {self.salario}\nQuantidade de horas trabalhadas: {horas_trabalhadas}\nValor da hora trabalhada: {valor_hora:.2f}'
    def __repr__(self):
        return f'Nome: {self.nome}\nEmail: {self.email}\nSalario: {self.salario}'
    
class Desenvolvedor(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, lang:list):
        super().__init__(nome, email,salario)
        self.lang = lang
    
    def calcula_salario_dev(self, horas_trabalhadas:float):
        return f'Salario = {self.calcula_salario(horas_trabalhadas)}'
    def __repr__(self):
        return f'Nome: {self.nome}\nEmail: {self.email}\nSalario: {self.salario}\nLinguagens: {self.lang}'
    def projeto_momento(self):
        return f"{self.nome} está trabalho atualmente em um projeto usando as linguagens {self.lang[0:2]}"
    
class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, departamento: str):
        super().__init__(nome, email,salario)
        self.departamento = departamento
    
    def __repr__(self):
        return f'Nome: {self.nome}\nEmail: {self.email}\nSalario: {self.salario}\nDeparatamento: {self.departamento}'
    
    def calcula_salario_gerente(self, horas_trabalhadas):
        return super().calcula_salario(horas_trabalhadas)
    

if __name__ == "__main__":
    funcionario = Funcionario("João", "joãozinho@gmail.com", 4500.00)
    print(funcionario.__repr__())
    print()
    print(funcionario.calcula_salario(184))
    print()
    dev = Desenvolvedor("Carlos", "carlinhos@gmail.com", 5000.00, lang=["Python","C++","Java"])
    print(dev.__repr__())
    print()
    print(dev.calcula_salario_dev(200))
    print()
    print(dev.projeto_momento())
    gerente = Gerente("Manoel","manoelzinho@gmail.com",8000.00,"Vendas")
    print()
    print(gerente.__repr__())
    print()
    print(gerente.calcula_salario_gerente(150))
   
    

    