# import sys, random

# string = sys.argv[1]
# listOfCharacters = list(string)
# random.shuffle(listOfCharacters)
# print ''.join(listOfCharacters)


import sys, rearrange

def anagram(string):
	listOfCharacters = list(string)
	rearrange.shuffle(listOfCharacters)
	return ''.join(listOfCharacters)


if __name__ == '__main__':
	string = sys.argv[1]
	anagram = anagram(string)
	print anagram