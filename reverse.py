# import sys

# string = sys.argv[1]
# listOfCharacters = list(string)
# reversedList = list(reversed(string))
# print ''.join(reversedList)

import sys

def reverse(string):
	listOfCharacters = list(string)
	numberOfCharacters = string.__len__()
	highestIndex = numberOfCharacters - 1
	numberOfIterations = highestIndex / 2

	for i in range(0, numberOfIterations):
		indexToSwapWith = highestIndex - i
		listOfCharacters[i], listOfCharacters[indexToSwapWith] = listOfCharacters[indexToSwapWith], listOfCharacters[i]

	return ''.join(listOfCharacters)


if __name__ == "__main__":
	word = sys.argv[1]
	reversedWord = reverse(word)
	print reversedWord