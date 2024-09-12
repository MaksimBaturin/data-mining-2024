from math import sqrt
def IsPrime(numb):    
    for i in range(2, int(sqrt(numb))+1):
        if (numb % i == 0):
            return False    
    return True


def FindNearestPrimeNumb(n):
    LowerNumb = n-1
    UpperNumb = n+1
    while True:
        if IsPrime(LowerNumb):
            return LowerNumb
        if IsPrime(UpperNumb):
            return UpperNumb
        LowerNumb-=1
        UpperNumb+=1
        
Numb = int(input("Введите натуральное число: "))

print("Ближайшее простое число: ", FindNearestPrimeNumb(Numb))