import numpy as n
import math as m
def usa_numpy(nun)->float:
    '''
    função para ver o seno de um valor inteiro
    param:
        num: int
    return:
    x: float
    '''
    x = n.sin(nun)
    return x
def usando_math(x)->float:
    i = m.sin(x)
    return i
if __name__ == "__main__":
    n = usa_numpy(1)
    print(n)
    i = usando_math(1)
    print(i)