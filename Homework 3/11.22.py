#Caleb Covington
#1606086
wordlist= list(input().split(" "))
wordfreq = []

for l in wordlist:
    wordfreq.append(wordlist.count(l))

for i in range(len(wordlist)):
    print(wordlist[i], wordfreq[i])
