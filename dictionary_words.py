import sys
import time
start_time = time.time()

# before optimizations 
# --- 0.212069034576 seconds ---
# --- 0.155822992325 seconds ---
# --- 0.0276880264282 seconds ---

# after using readlines()
# --- 0.023286819458 seconds ---
# --- 0.212635993958 seconds ---
# --- 0.0250890254974 seconds ---

# after using f.close()
# --- 0.0486791133881 seconds ---
# --- 0.0324649810791 seconds ---
# --- 0.100464105606 seconds ---

from random import randint

# returns a sentence based on int arg, words taken from words file in /usr/share/dict/words
def generateSentenceWithAmountOfWords(numberOfWordsToReturn):
	# open the words file
	f = open('/usr/share/dict/words', 'r')
	# read the file and store the content in words var (string)
	
	# before optimization
	# words = f.read()
	# create a list from the words string var, each element is one word (the words file has one word per line)
	# listOfWords = words.split('\n')

	# after optimization
	listOfWords = f.readlines()

	f.close()

	# store all possible indexes of the list of words
	possibleIndexes = listOfWords.__len__() - 1

	# create array to hold words that will be in the sentence
	listOfRandomWords = []

	# for the number of iterations specified in the number of words arg,
	for i in range(0, numberOfWordsToReturn):
		# generate a random index that is within the possible indexes (before optimizations)
		randomIndex = randint(0, possibleIndexes)

		# # This isn't an optimization .. it actually makes it less random ... 
		# # generate a random start index, from 0 to all possible indexes 
		# randomStartIndex = randint(0, possibleIndexes)
		# # generate a random end index, from randomStartIndex to all possible indexes
		# randomEndIndex = randint(randomStartIndex, possibleIndexes)
		# # generate a random number from within the randomly generated range
		# randomIndex = randint(randomStartIndex, randomEndIndex)
		
		# before optimization
		# grab the word at the random index in the list of words and add the word to the list of random words array
		# listOfRandomWords.append(listOfWords[randomIndex])

		# after optimization
		# grab the word at the random index in the list of words, cut the last two characters, which is '\n' and 
		# add the word to the list of random words array
		listOfRandomWords.append(listOfWords[randomIndex][0:-2])

	print("--- %s seconds ---" % (time.time() - start_time))
	# return the list of random words joined by a space
	return " ".join(listOfRandomWords)

# if run from the terminal, take the first command line arg and use that as the number specified and print the sentence
if __name__ == '__main__':
	numberOfWordsToReturn = int(sys.argv[1])
	sentence = generateSentenceWithAmountOfWords(numberOfWordsToReturn)
	print sentence
