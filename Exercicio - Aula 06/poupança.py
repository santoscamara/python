def poupanca(deposito_inicial:float,taxa_de_juros:float):

    mes = 1
    taxa_de_juros = taxa_de_juros/100 #Taxa de juros em porcentuais.
    saldo = deposito_inicial
    total_juros = 0

    print(f"\nO deposito inicial foi de: {deposito_inicial}\n")
    for mes in range(1,25):
        juros_mes = saldo * taxa_de_juros
        saldo += juros_mes
        total_juros += juros_mes 
        print(f"Rendimento do mês {mes} foi de: {saldo:.2f}")
        mes += 1
    return f"O total ganho com juros no período foi de: {total_juros}"
        
deposito_inicial=float(input("Informe o valor do depósito inicial (R$): "))
taxa_de_juros=float(input("Informe a taxa de juros (%): "))
print(poupanca(deposito_inicial,taxa_de_juros))
