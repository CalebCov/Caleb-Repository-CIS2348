
word = input()
password = ''

n = 0
while n < len(word):
    char = word[n]
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
    n += 1

password += "q*s"

print(password)
    
