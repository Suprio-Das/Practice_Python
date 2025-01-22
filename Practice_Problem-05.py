def validate_password(password):
    count = 0
    if(password[0].isnumeric()):
        return False
    elif(password[0].isupper()):
        return False
    else:
        for i in range(1, len(password), 1):
            if(password[i] == '!' or password[i] == '@' or password[i] == '#' or password[i] == '$' or password[i] == '%'):
                count += 1
                
    if count > 0:
        return True
    else: 
        return False

password = "asdsab@!@234"
validate_password(password)