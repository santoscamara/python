def pop(lista:list)->list:
    lista.pop()
    return lista
def checar(lista:list)->list:
    if "quadrado" in lista:
        return("Sim, 'quadrado' está presente na lista")
    else:
        return("Não, 'quadrado' não está na lista")

if __name__ == "__main__":
    lista =["verde","amarelo","vermelho","preto"]
    lista2=["triangulo","esfera","circulo","retangulo"]
    print(pop(lista))
    print(checar(lista2))