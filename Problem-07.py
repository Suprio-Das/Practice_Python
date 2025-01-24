def natural_numbers_summation_pattern(n):
    total_sum = 0
    for i in range(1, n + 1):
        if i == 1:
            print(f"{i} = {i}")
        else:
            total_sum += i
            series = " + ".join(str(x) for x in range(1, i + 1))
            print(f"{series} = {total_sum}")

n = int(input("Enter the value of n: "))
natural_numbers_summation_pattern(n)
