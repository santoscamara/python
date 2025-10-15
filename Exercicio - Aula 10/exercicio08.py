def simeteria(times1: set, times2: set)->set:
    print(times1 ^ times2)
    print(times1.symmetric_difference(times2))
    print(times1.isdisjoint(times2))

if __name__ == "__main__":
    times1 = {'Flamengo', 'Bangu','Vasco','Botafogo'}
    times2 = {'Vasco', 'Campo Grande','Fluminense','Madureira'}
    simeteria(times1, times2)