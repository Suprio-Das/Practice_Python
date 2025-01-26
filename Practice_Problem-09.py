def sum_of_digits(number):
    number = abs(number)
    return sum(int(digit) for digit in str(number))


print(sum_of_digits(123))
print(sum_of_digits(-456))
