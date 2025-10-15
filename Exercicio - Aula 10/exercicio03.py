x = ["banana", "kiwi", "morango"]
x[1] = "uva"
y = tuple(x)

print(y)

#criando um tupla com elementos
tupla = (1, 2, 3, "quatro", "cindo")
#acessando elementos de uma tupla
primeiro_elemento = tupla[0]
ultimo_elemento=tupla[-1]

#tentando adicionar um novo elemento a uma tupla (gerará um erro)
tupla.append(6)

#tentando remover um elemento de uma tupla(gerará um erro)
tupla.remove(2)