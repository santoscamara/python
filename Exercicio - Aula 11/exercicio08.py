class Funcionario:
    def __init__(self, nome:str, email: str, salario: float)->None:
        self.nome = nome
        self.email = email
        self.salario = salario
    
    def calcula_salario(self, horas_trabalhadas:float)->None:
        self.salario = horas_trabalhadas * 5.5
        return self.salario
    
class Desenvolvedor(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, lang:list):
        super().__init__(nome: str, email: str, salario: float):
        self.lang = lang
    
    def calcula_salario_dev(self):
        return f"{self.calcula_salario()} Salario = {self.salario}"
    def projeto_momento(self, lang:list):
        return f"{self.nome} está trabalho atualmente em um projeto usando as linguagens {self.lang}"
    
class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, departamento: str)
    

    