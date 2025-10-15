def caixa_alta(planeta_anao:set)->set:
    for astro in planeta_anao:
        print(astro.upper(), end=' - ')



if __name__ == "__main__":
    planeta_anao ={'Plutão', 'Eris','Ceres','Haumea','Makemake'}
    caixa_alta(planeta_anao)
