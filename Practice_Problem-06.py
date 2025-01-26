def multiplicationTable(N):
    result = []
    for i in range(1, 11):
        result.append(N * i)
    print(" ".join(map(str, result)))


multiplicationTable(5)