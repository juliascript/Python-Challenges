import sys
from random import randint

numberOfWordsToReturn = int(sys.argv[1])

f = open('/usr/share/dict/words', 'r')
words = f.read()
listOfWords = words.split('\n')
possibleIndexes = listOfWords.__len__() - 1

listOfRandomWords = []


for i in range(0, numberOfWordsToReturn):
	randomIndex = randint(0, possibleIndexes)
	listOfRandomWords.append(listOfWords[randomIndex])

print " ".join(listOfRandomWords)
