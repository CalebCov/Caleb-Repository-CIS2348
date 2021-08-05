#Caleb Covington


UserWord = input()
password = ''

z = 0
while z < len(UserWord):
    char = UserWord[z]
    if char == 'i':
        password += '!'
    elif char == 'a':
        password += '@'
    elif char == 'm':
        password += 'M'
    elif char == 'B':
        password += '8'
    elif char == 'o':
        password += '.'
    else:
        password += char
    z += 1

password += "q*s"

print(password)
    
