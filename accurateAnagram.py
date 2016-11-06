import sys, rearrange, trie, math

'''
some anagrams for testing: are, earth, fringe, impart, limped

'''

def generateArrayOfWordsFromWordsTextFile():
	# open the words file
	f = open('/usr/share/dict/words', 'r')
	# read the file, store the string in var called words
	words = f.read()
	# create array of words
	listOfWords = words.split('\n')
	# close the file
	f.close()
	# return list of words
	return listOfWords

# this returns a new string which is the argument string with its characters shuffled to form a new word
def shuffleCharactersOf(string):
	# create a list from the string, each element being a single character in the string
	listOfCharacters = list(string)

	# using my own shuffle function to rearrange the order of elements in the list of characters
	rearrange.shuffle(listOfCharacters)

	# return new string
	return ''.join(listOfCharacters)


# this generates an anagram from the string arg

# might give a false negative because even though there are n! possibilities, the characters
#   are being shuffled randomly and won't always reach every possibility always. 

# possibility of getting a false positive is greater with smaller word length

def generateAnagram(string):
	# create dictionary from language
	
	# generate words array
	wordsArray = generateArrayOfWordsFromWordsTextFile()

	# use my own trie algo to generate trie from words array
	languageDict = trie.generateTrieFromWordsArray(wordsArray)

	# iterate n! times, where n is the number of characters in the string
	numberOfPossibleCombinationsForString = math.factorial(len(string))
	for i in range(0, numberOfPossibleCombinationsForString):
		# shuffle characters in the string
		wordWithShuffledCharacters = shuffleCharactersOf(string)

		# this won't prevent all cases of when the shuffle returns the same order, but it'll shuffle it again
		if wordWithShuffledCharacters == string:
			wordWithShuffledCharacters = shuffleCharactersOf(string)

		# use my own trie check algo to check if the word is in the trie
		if trie.isWordPresentInTrie(languageDict, wordWithShuffledCharacters):
			# return it
			return wordWithShuffledCharacters
	# if the characters were shuffled n! times and didn't get a match, return out with message.
	return "There is no anagram for %s." % (string)

# if run from terminal, take first command line arg and attempt to generate anagram, return the result
if __name__ == '__main__':
	string = sys.argv[1]
	anagram = generateAnagram(string)
	print anagram