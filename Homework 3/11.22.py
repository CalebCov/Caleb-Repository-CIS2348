#Caleb Covington
#1606086
listOfWords= list(input().split(" "))
frequency = []

for l in listOfWords:
    frequency.append(listOfWords.count(l))

for i in range(len(listOfWords)):
    print(listOfWords[i], frequency[i])
