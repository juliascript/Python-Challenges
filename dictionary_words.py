import sys
from random import randint

# returns a sentence based on int arg, words taken from words file in /usr/share/dict/words
def generateSentenceWithAmountOfWords(numberOfWordsToReturn):
	# open the words file
	f = open('/usr/share/dict/words', 'r')
	# read the file and store the content in words var (string)
	words = f.read()
	# create a list from the words string var, each element is one word (the words file has one word per line)
	listOfWords = words.split('\n')
	# store all possible indexes of the list of words
	possibleIndexes = listOfWords.__len__() - 1

	# create array to hold words that will be in the sentence
	listOfRandomWords = []

	# for the number of iterations specified in the number of words arg,
	for i in range(0, numberOfWordsToReturn):
		# generate a random index that is within the possible indexes
		randomIndex = randint(0, possibleIndexes)
		# grab the word at the random index in the list of words and add the word to the list of random words array
		listOfRandomWords.append(listOfWords[randomIndex])

	# return the list of random words joined by a space
	return " ".join(listOfRandomWords)

# if run from the terminal, take the first command line arg and use that as the number specified and print the sentence
if __name__ == '__main__':
	numberOfWordsToReturn = int(sys.argv[1])
	sentence = generateSentenceWithAmountOfWords(numberOfWordsToReturn)
	print sentence
