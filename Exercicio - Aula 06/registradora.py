def registradora():
    total = 0
    while True:
        codigo=int(input("Escolha o seu produto: "))
        match codigo:
            case 1:
                preco = 0.50
                qtd=int(input("Informe a quantidade: "))
                total += preco * qtd
                continue
            case 2:
                preco = 1.00
                qtd=int(input("Informe a quantidade: "))
                total += preco * qtd
                continue
            case 3:
                preco = 4.00
                qtd=int(input("Informe a quantidade: "))
                total += preco * qtd
                continue
            case 5:
                preco = 7.00
                qtd=int(input("Informe a quantidade: "))
                total += preco * qtd
                continue
            case 9:
                preco = 8.00
                qtd=int(input("Informe a quantidade: "))
                total += preco * qtd
                continue
            case 0:
                return f"O total dos produtos selecionados foi de: {total:.2f}"    
            case _:
                print("Código Inválido")
                continue
print("Código: 1 - Preço: 0.50")
print("Código: 2 - Preço: 1.00")
print("Código: 3 - preço: 4.00")
print("Código: 5 - preço: 7.00")
print("Código: 9 - preço: 8.00")
print(registradora())



