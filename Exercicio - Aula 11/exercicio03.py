class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Nome: {self.nome}, idade: {self.idade}"
    
pessoa = Pessoa("Raphael", 41)
print(pessoa)