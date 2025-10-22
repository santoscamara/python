class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome # atributo público
        self.__idade = idade #atributo privado, acessível apenas dentro da classe
    
    #Método público para acessar o atributo privado
    def get_idade(self):
        return self.__idade
    
    #Método público para modificar o atributo privado
    def set_idade(self, nova_idade:int):
        if nova_idade > 0: # verifica se a idade é válida
            self.__idade = nova_idade
        else:
            print("Idade inválida!")


if __name__ == "__main__":
    #exemplo de uso
    pessoa = Pessoa("Raphael", 41)
    print(pessoa.nome) #acesso ao atributo público
    print(pessoa.get_idade()) #acesso ao atributo privado via método público
    pessoa.set_idade(30) #Modificado o atributo privado
    print(pessoa.get_idade())
    pessoa.set_idade(-5)  #Tentando modificar com valor inválido
    
