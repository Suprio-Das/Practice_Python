string = str(input("Enter a string: ")).lower()
n = len(string)
cat = 0
hat = 0
for i in range(len(string)):
    if(string[i:i+3] == 'cat'):
        cat += 1
    elif(string[i:i+3] == 'hat'):
        hat += 1

if(cat == hat):
    print(True)
else:
    print(False)