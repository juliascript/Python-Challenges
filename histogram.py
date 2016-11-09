import sys, operator 

def generateHistogramFromFile(textfile):
	# open text file 
	f = open(textfile, 'r')

	# read the file
	fileContent = f.read()

	# generate array from file content
	wordsArray = fileContent.strip().split(' ')

	# generate histogram from words array
	histogram = {}
	for word in wordsArray:
		if word in histogram:
			histogram[word] = histogram[word] + 1
		else:
			histogram[word] = 1

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

if __name__ == "__main__":
	textFile = sys.argv[1]
	histogram = generateHistogramFromFile(textFile)
	sortedHistogram = sortHistogram(histogram)
	print 'leastFrequentWord: ', leastFrequentWordIn(sortedHistogram)
	print 'mostFrequentWord: ', mostFrequentWordIn(sortedHistogram)
	print 'numberOfUniqueWords: ', numberOfUniqueWordsIn(sortedHistogram)
	print 'averageFrequencyOfWords: ', averageFrequencyOfWordsIn(sortedHistogram)
	createHistogramFileWithName('histogram.txt', sortedHistogram)



