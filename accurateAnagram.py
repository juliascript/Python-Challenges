import sys, rearrange, enchant

# this returns a new string which is the argument string with its characters shuffled to form a new word
def shuffleCharactersOf(string):
	# create a list from the string, each element being a single character in the string
	listOfCharacters = list(string)
	# using my own shuffle function to rearrange the order of elements in the list of characters
	rearrange.shuffle(listOfCharacters)
	# return new string
	return ''.join(listOfCharacters)

# this generates an anagram from the string arg in the language specified. if no lang arg, defaults to US dialect of english
def generateAnagram(string, language="en_US"):
	# create dictionary from language
	languageDict = enchant.Dict(language) 
	# iterate 101 times
	for i in range(0,100):
		# shuffle characters in the string
		wordWithShuffledCharacters = shuffleCharactersOf(string)

		# if it matches one of the words in the dictionary,
		if languageDict.check(wordWithShuffledCharacters):
			# return it
			return wordWithShuffledCharacters
	# if the characters were shuffled 101 times and didn't get a match, return out with message.
	return "It's taking a while to find an anagram."

# if run from terminal, take first command line arg and attempt to generate anagram, return the result
if __name__ == '__main__':
	string = sys.argv[1]
	anagram = generateAnagram(string)
	print anagram