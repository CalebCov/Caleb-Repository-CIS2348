#Caleb Covington
#program that returns user input squared, cubed, summed, and the product.
user_num = int(input("Enter integer:\n"))

# Type your code here
num_squared = user_num * user_num
num_cubed = user_num * user_num * user_num

print("You entered:",user_num)
print(user_num, "squared is",num_squared)
print("And",user_num,"cubed is",num_cubed,"!!")

user_num2 = int(input("Enter another integer:\n"))
sum = user_num + user_num2
product = user_num * user_num2

print(user_num,"+",user_num2,"is",sum)
print(user_num,"*",user_num2,"is",product)
