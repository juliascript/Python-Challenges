# import sys, random

# words = sys.argv[1:]
# random.shuffle(words)
# print words

import sys
from random import randint

words = sys.argv[1:]
numberOfWords = words.__len__()
possibleIndexes = numberOfWords - 1

for i in range(0, possibleIndexes):
	randomIndex = randint(0, possibleIndexes)
	words[i] , words[randomIndex] = words[randomIndex], words[i]

print words