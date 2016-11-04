# import sys, random

# string = sys.argv[1]
# listOfCharacters = list(string)
# random.shuffle(listOfCharacters)
# print ''.join(listOfCharacters)


import sys, rearrange

# this returns a new string which is the argument string with its characters shuffled to form a new word
def anagram(string):
	# create a list from the string, each element being a single character in the string
	listOfCharacters = list(string)
	# using my own shuffle function to rearrange the order of elements in the list of characters
	rearrange.shuffle(listOfCharacters)
	# return new string
	return ''.join(listOfCharacters)

# if run from terminal, take first command line arg and shuffle its characters, return the result
if __name__ == '__main__':
	string = sys.argv[1]
	anagram = anagram(string)
	print anagram