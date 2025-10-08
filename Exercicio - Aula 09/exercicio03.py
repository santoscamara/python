def remocao_total(lista:list)->list:
    lista.clear()
    return lista

def construcao()->list:
    minha_lista =list(("carro","casa","moto"))
    return minha_lista
def construcao_range()->list:
    lista_construcao = list(range(10, 50, 2))
    return lista_construcao
    
if __name__ == "__main__":
    lista = ["laranja","azul","vermelho","roxo"]
    print(remocao_total(lista))
    print(construcao())
    print(construcao_range())
