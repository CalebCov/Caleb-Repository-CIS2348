#Caleb Covington
#1606086
lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_in_cups = float(input('Enter amount of water (in cups):\n'))
agave_in_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon_juice_cups), 'cup(s) lemon juice')
print('{:.2f}'.format(water_in_cups), 'cup(s) water')
print('{:.2f}'.format(agave_in_cups), 'cup(s) agave nectar\n')

num_of_servings = float(input('How many servings would you like to make?\n'))

print('\nLemonade ingredients - yields', '{:.2f}'.format(num_of_servings), 'servings')

convert_lemon = num_of_servings / 3
convert_water = num_of_servings * 2.66666667
convert_agave = num_of_servings / 2.4

print('{:.2f}'.format(convert_lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(convert_water), 'cup(s) water')
print('{:.2f}'.format(convert_agave), 'cup(s) agave nectar\n')

gallons_of_lemon = convert_lemon / 16
gallons_of_water = convert_water / 16
gallons_of_agave = convert_agave / 16

print('Lemonade ingredients - yields', '{:.2f}'.format(num_of_servings), 'servings')

print('{:.2f}'.format(gallons_of_lemon), 'gallon(s) lemon juice')
print('{:.2f}'.format(gallons_of_water), 'gallon(s) water')
print('{:.2f}'.format(gallons_of_agave), 'gallon(s) agave nectar')
