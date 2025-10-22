class Aluno:
    uni = "Estácio"

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def situacao(self):
        return "Aprovado" if self.nota >= 6 else "Reprovado"
    
    def __str__(self):
        return f"{self.nome} ({self.nota}) - {self.situacao()}"
    
    
aluno1 = Aluno("João", 8)
aluno1.situacao()
nota_final = aluno1.__str__()
print(nota_final)

    
