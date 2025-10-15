def verificar_set(planeta_anao:set)->bool:
    print('Ceres' in planeta_anao)
    print('Lua' in planeta_anao)
    print('Eris' not in planeta_anao)    


if __name__ == "__main__":
    planeta_anao = {'Plutão','Ceres','Eris','Haumea','Makemake'}
    verificar_set(planeta_anao)



