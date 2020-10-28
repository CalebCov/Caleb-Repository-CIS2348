dictionary = {}
var = 1
counter = 1

for var in range(1, 6):
    jerseyNum = int(input('Enter player {}\'s jersey number:\n'.format(var)))
    Status = int(input('Enter player {}\'s rating:\n'.format(var)))
    print()
    if jerseyNum < 0 and jerseyNum > 99 and Status < 0 and Status > 9:
        print('invalid entry')
        break
    else:
        dictionary[jerseyNum] = Status
print("ROSTER")

for jerseyNum, Status in sorted(dictionary.items()):
    print("Jersey number: %d, Rating: %d" % (jerseyNum, Status))
selector = ''

while selector.upper() != 'Q':
    print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\n'
        'r - Output players above a rating\no - Output roster\nq - Quit\n')
    selector = input('Choose an option:\n')
    if selector == 'a':
        jerseyNum = int(input('Enter a new player\'s jersey number:\n'.format(var)))
        Status = int(input('Enter the players\'s rating:\n'.format(var)))
        dictionary[jerseyNum] = Status
    elif selector == 'd':
        jerseyNum = int(input('Enter a jersey number:\n'))
        if jerseyNum in dictionary.keys():
            del dictionary[jerseyNum]
    elif selector == 'u':
        jerseyNum = int(input('Enter a jersey number:\n'))
        if jerseyNum in dictionary.keys():
            Status = int(input('Enter a new rating for player:\n'))
            dictionary[jerseyNum] = Status
    elif selector == 'r':
        statusUpdate = int(input('Enter a rating:\n'))
        print('ABOVE {}'.format(statusUpdate))
        for jerseyNum, Status in sorted(dictionary.items()):
                if Status > statusUpdate:
                    print("Jersey number: %d, Rating: %d" % (jerseyNum, Status))
    elif selector == 'o':
        print("ROSTER")
        for jerseyNum, Status in sorted(dictionary.items()):
            print("Jersey number: %d, Rating: %d" % (jerseyNum, Status))