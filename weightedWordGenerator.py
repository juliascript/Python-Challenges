import sys, histogram, random, math

def generateRandomWordFromHistogram(_histogram):
	totalWords = 0
	listOfTuples = []
	for word, count in _histogram:
		# add word to tuple with it's range (being it's upper bound)
		upperBound = totalWords + count
		listOfTuples.append((word, upperBound))
		totalWords += count

	# generate random int and then binary search to find the word it correlates to
	randomInt = random.randint(1, totalWords)
	word = binarySearch(listOfTuples, randomInt)
	return word

def binarySearch(tuples, index):
	half = math.floor(len(tuples) / 2)
	midpointIndexOfTuplesList = int(half)
	if midpointIndexOfTuplesList == 1:
		word = tuples[midpointIndexOfTuplesList][0]
		return word

	midpointOfTuplesList = tuples[midpointIndexOfTuplesList]

	lowerBoundOfMidpoint = tuples[midpointIndexOfTuplesList - 1][1]
	upperBoundOfMidpoint = midpointOfTuplesList[1]

	if lowerBoundOfMidpoint <= index <= upperBoundOfMidpoint:
		return tuples[midpointIndexOfTuplesList][0]
	elif index < lowerBoundOfMidpoint:
		upperBound = midpointIndexOfTuplesList - 1
		return binarySearch(tuples[0:upperBound], index)
	elif upperBoundOfMidpoint < index:
		upperBound = midpointIndexOfTuplesList - 1
		return binarySearch(tuples[midpointIndexOfTuplesList:-1], index)


def generateSentenceFromTextfile(textfile):
	_histogram = histogram.generateHistogramFromFile(textfile)
	sortedHistogram = histogram.sortHistogram(_histogram)

	sentence = []
	for i in range(7):
		randomWord = generateRandomWordFromHistogram(sortedHistogram)
		sentence.append(randomWord)

	return (' ').join(sentence)

if __name__ == "__main__":
	_file = sys.argv[1]
	print generateSentenceFromTextfile(_file)
	