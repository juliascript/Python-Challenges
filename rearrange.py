# in-place shuffle algo 

# import sys, random

# words = sys.argv[1:]
# random.shuffle(words)
# print words

import sys
from random import randint

# THIS EDITS THE ORIGINAL ARRAY
def shuffle(array):
	# count elements in array
	numberOfElements = len(array)
	# number of indexes in array from number of elements in array
	possibleIndexes = numberOfElements - 1

	# iterate over all indexes
	for i in range(0, numberOfElements):
		# generate a random int that is one of the possible indexes
		randomIndex = randint(0, possibleIndexes)
		# swap the iterative index and the random index 
		array[i], array[randomIndex] = array[randomIndex], array[i]

# if run from terminal, use the command line args and print the result to the console
if __name__ == '__main__':
	words = sys.argv[1:]
	shuffle(words)
	print words