class Produto:

    def __init__(self, nome:str, preco:float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def repor(self, estoque):
        self.estoque += estoque
        
    
    def vender(self, estoque):
        self.estoque -= estoque
        
    
    def __str__(self):
        return f"O produto {self.nome} custa {self.preco} possui {self.estoque} em estoque."
    
produto1 = Produto("Lápis", 5.00, 2)
produto1.vender(2)
produto1.repor(1)
print(produto1)

    


    
