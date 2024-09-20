
def NOD(b):
    Binb = str(bin(b))
    if (Binb[len(Binb)-3: len(Binb)] == "000"):
        return 8
    elif ((Binb[len(Binb)-3: len(Binb)] == "100")):
        return 4
    elif ((Binb[len(Binb)-2: len(Binb)] == "10")):
        return 2
    
    return 1
    

b = int(input("Введите 10-значное число: "))

result = NOD(b)

print("НОД:", result)
