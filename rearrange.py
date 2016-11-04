# import sys, random

# words = sys.argv[1:]
# random.shuffle(words)
# print words

import sys
from random import randint

def shuffle(array):
	numberOfElements = array.__len__()
	possibleIndexes = numberOfElements - 1

	for i in range(0, possibleIndexes):
		randomIndex = randint(0, possibleIndexes)
		array[i] , array[randomIndex] = array[randomIndex], array[i]

if __name__ == '__main__':
	words = sys.argv[1:]
	shuffle(words)
	print words