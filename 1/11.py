def vector_product(a, b):
    if len(a) != 3 or len(b) != 3:
        raise ValueError("Векторы должны быть трехмерными (длина 3)")
    
    result = [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[1] - a[1] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]
    
    return result

a = [1, 2, 3]
b = [4, 5, 6]

cross_product = vector_product(a, b)
print("Векторное произведение: ", cross_product)