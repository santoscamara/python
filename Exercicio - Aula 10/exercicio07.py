def times_carioca(times1:set,times2:set)->set:
    print(times1 | times2)
    print(times1.union(times2))
    print(times1 & times2)
    print(times1.intersection(times2))



if __name__ == "__main__":
    times1 = {'Flamengo', 'Vasco', 'Botafogo', 'Fluminense'}
    times2 = {'Bangu', 'America', 'Campo Grande', 'Volta Redonda', 'Olaria', 'Flamengo'}
    times_carioca(times1,times2)