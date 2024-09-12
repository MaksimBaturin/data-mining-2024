def FibonacciPartialSums(N):
    a = 0
    b = 1
    PartialSum = 0

    for _ in range(N):
        PartialSum += a
        yield PartialSum

        a, b = b, a + b

N = int(input("Введите количество элементов последовательности: "))

fibonacci = FibonacciPartialSums(N)

for sum in fibonacci:
    print(sum)