import sys, operator, random, unicodedata

def generateHistogramFromFile(textfile):
	# open text file 
	f = open(textfile, 'r')

	# read the file
	fileContent = f.read()

	# fileContent = fileContent.encode('utf-8', 'ignore')

	# generate array from file content
	wordsArray = fileContent.strip().replace('\n', ' ').split(' ')

	# generate histogram from words array
	histogram = {}
	for word in wordsArray:
		if word in histogram:
			histogram[word] = histogram[word] + 1
		else:
			histogram[word] = 1

	# function called zip --> tuple
	# hash function used to implement dictionaries
	
	return histogram

def sortHistogram(histogram):
	return sorted(histogram.items(), key=operator.itemgetter(1))

def leastFrequentWordIn(histogram):
	return histogram[0]

def mostFrequentWordIn(histogram):
	return histogram[-1]

def numberOfUniqueWordsIn(histogram):
	return len(histogram)

def averageFrequencyOfWordsIn(histogram):
	numberOfWords = len(histogram)
	sumOfFrequencies = 0
	for word, frequency in histogram:
		sumOfFrequencies += frequency

	return sumOfFrequencies / numberOfWords

def createHistogramFileWithName(filename, histogram):
	f = open(filename, 'w')
	for word, count in histogram:
		f.write("%s %i\n" % (word, count))

def createWeightedListFromHistogram(histogram):
	_list = []
	for word, count in histogram:
		for i in range(count):
			_list.append(word)
	return _list

def returnOneWordFromWeightedList(_list):
	return random.choice(_list)

if __name__ == "__main__":
	textFile = sys.argv[1]
	histogram = generateHistogramFromFile(textFile)
	sortedHistogram = sortHistogram(histogram)
	sortedHistogram = sortedHistogram[0:-1]
	# print sortedHistogram, '\n'
	# print 'leastFrequentWord: ', leastFrequentWordIn(sortedHistogram)
	# print 'mostFrequentWord: ', mostFrequentWordIn(sortedHistogram)
	# print 'numberOfUniqueWords: ', numberOfUniqueWordsIn(sortedHistogram)
	# print 'averageFrequencyOfWords: ', averageFrequencyOfWordsIn(sortedHistogram)
	# createHistogramFileWithName('histogram.txt', sortedHistogram)
	weightedList = createWeightedListFromHistogram(sortedHistogram)
	# print weightedList
	sentence = []
	for i in range(10):
		sentence.append(returnOneWordFromWeightedList(weightedList))	
	print sentence


