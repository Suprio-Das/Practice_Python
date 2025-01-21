n = int(input("Enter a number(Postive or Negative): "))

if(n > 0):
    while(n >= 0):
        n -= 1
        if(n >= 0):
            print(n)
elif(n < 0):
    while(n <= 0):
        print(n)
        n += 1