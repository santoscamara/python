def criando_e_verificando() -> set:
    planeta_anao={'Plutão', 'Ceras', 'Eris', 'Humea','Makemake'}
    print(planeta_anao)
    print(type(planeta_anao))

def duplicando()-> set:
    planetas={'Marte','Terra','Jupiter'}
    print(planetas)
    return planetas

def tamanho(planetas)-> int:
    print(len(planetas))

if __name__ == "__main__":
    criando_e_verificando()
    planetas = duplicando()
    tamanho(planetas)