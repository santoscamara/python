def remocao(lista:list)->list:
    lista.remove("azul")
    return lista

if __name__ == "__main__":
    lista=["laranja","azul","verde","preto"]
    print(remocao(lista))

