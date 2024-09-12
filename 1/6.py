
Lists = [[1, 5.6, 1+2j], [6.4, 3+2j, 10+14j, 25], [32, 5.7, 12, 7+6j]]

NewList = []

for List in Lists:
    for Number in List:
        if type(Number) == complex:
            NewList.append(Number)

NewTuple = tuple(NewList)

print(NewTuple)