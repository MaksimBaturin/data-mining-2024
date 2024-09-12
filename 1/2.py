
def NOD(b):
    Binb = str(bin(b))
    if (Binb[len(Binb)-3: len(Binb)] == "000"):
        return 8
    elif ((Binb[len(Binb)-3: len(Binb)] == "100")):
        return 4
    elif ((Binb[len(Binb)-2: len(Binb)] == "10")):
        return 2
    
    return 1
    
NumbLen = 0
try:
    b = int(input("Введите 10-значное число: "))
    if (len(str(b)) != 10):
        raise Exception
except (ValueError, TypeError, Exception):
    print("Введите корректное число!")
else:
    result = NOD(b)
    print("НОД:", result)

