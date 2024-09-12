import unittest
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

class TestFindNearestPrimeNumb(unittest.TestCase):

    def test_nearest_prime_number(self):
        
        self.assertEqual(FindNearestPrimeNumb(10), 11)
        self.assertEqual(FindNearestPrimeNumb(20), 19)
        self.assertEqual(FindNearestPrimeNumb(30), 29)
        self.assertEqual(FindNearestPrimeNumb(40), 41)
        self.assertEqual(FindNearestPrimeNumb(50), 47)
        self.assertEqual(FindNearestPrimeNumb(60), 59)
        self.assertEqual(FindNearestPrimeNumb(70), 71)
        self.assertEqual(FindNearestPrimeNumb(80), 79)
        self.assertEqual(FindNearestPrimeNumb(90), 89)
        self.assertEqual(FindNearestPrimeNumb(100), 101)


if __name__ == '__main__':
    unittest.main()