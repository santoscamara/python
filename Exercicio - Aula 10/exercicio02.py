#inicializando uma tupla
tup =(3,"bom",0.5)
#outra forma de incializar
tep = 2, [9,1], "bum"
#retorna "o"
print(tup[1][1])
# resulta em erro! não pode alterar um tupla
#tep[0]=9
#mas isto pode! a lista foi alterada
tep[1][0]=3
print(tep[1][0])
