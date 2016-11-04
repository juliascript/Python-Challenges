# import sys

# string = sys.argv[1]
# listOfCharacters = list(string)
# reversedList = list(reversed(string))
# print ''.join(reversedList)

import sys

# this returns a new string that is the reversed version of the string that is passed in
def reverse(string):
	# generate a list, each element being a single character from the argument string
	listOfCharacters = list(string)
	# store number of characters in var
	numberOfCharacters = string.__len__()
	# store highest possible index in var
	highestIndex = numberOfCharacters - 1
	# store number of iterations in var
	numberOfIterations = highestIndex / 2

	# for half the length of the string
	for i in range(0, numberOfIterations):
		# store translative index (from midpoint of string) in var
		indexToSwapWith = highestIndex - i
		# swap iterative index with its translative index 
		listOfCharacters[i], listOfCharacters[indexToSwapWith] = listOfCharacters[indexToSwapWith], listOfCharacters[i]

	# return new string
	return ''.join(listOfCharacters)

# if run from terminal, take the first command line arg and print the reversed value of the string to the console
if __name__ == "__main__":
	word = sys.argv[1]
	reversedWord = reverse(word)
	print reversedWord