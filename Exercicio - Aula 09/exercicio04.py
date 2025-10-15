
medias = {"Raphael": 6,
        "Mariana": 8,
        "Caroline": 10,
        "Gilson": 9}
nome = input("Informe o nome do aluno: ")
if nome in medias:
    print(f"Media = {medias[nome]}")


medias["Sara"]=8

print(medias.keys())

print(medias.values())

for nome, nota in medias.items():
    if nota < 7:
        print(f"{nome} reprovado!")

