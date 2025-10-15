#criando um dicionário vazio
dicionario_vazio={}

#criando um dicionário com elementos
dicionario={"chave1": "valor1",
            "chave2": "valor2",
            "chave3": "valor3"
}

#acessando valores de um dicionário
valor1 = dicionario["chave1"]
valor2 = dicionario.get("chave2")

#adicionando um novo elemento a um dicionário
dicionario["chave4"]="valor4"

#Removendo um elemento de um dicionario
del dicionario["chave3"]
valor_removido = dicionario.pop("chave2")

#verificando a existência de uma chave em dicionário
if "chave1" in dicionario:
    print("A chave 'chave1 está no dicionario")