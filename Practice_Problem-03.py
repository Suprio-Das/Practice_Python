a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
flag = True

if(((a > 0 and b < 0 or (a < 0 and b > 0)) and flag == False) or ((a < 0 and b < 0) and flag == True)):
    print(True)
else:
    print(False)