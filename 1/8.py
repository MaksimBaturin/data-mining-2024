def FibonacciPartialSums(N):
    a = 0
    b = 1
    PartialSum = 0

    for _ in range(N):
        PartialSum += a
        yield PartialSum

        a, b = b, a + b

N = 100

fibonacci = FibonacciPartialSums(N)
NumbOfDigits = int(input("Введите кол-во цифр: "))
index = 0
for sum in fibonacci:
    if len(str(sum)) < NumbOfDigits:
        index += 1
    else:
        print(index)
        break