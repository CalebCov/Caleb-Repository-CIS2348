#Caleb Covington   


user_input = input()
normal = ""
reverse = ""
for character in user_input.lower():
    if character != ' ':
        normal += character
        reverse = character + reverse
if normal == reverse:
    print(user_input + " is a palindrome")
else:
    print(user_input + " is not a palindrome")
