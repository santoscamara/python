import math
pi = math.pi
e = math.e

def ceil(pi: float)->float:
    pi = math.ceil(pi)
    return pi
def floor(pi:float)->float:
    pi = math.floor(pi)
    return pi
def sqrt(pi: float)->float:
    pi = math.sqrt(4)
    return pi
def fat(pi:float)->int:
    pi = math.factorial(4)
    return pi
def fabs(pi:float)->float:
    pi = math.fabs(pi)
    return pi

if __name__ == "__main__":
    print(ceil(pi))
    print(floor(pi))
    print(sqrt(pi))
    print(fat(pi))
    print(fabs(pi))
