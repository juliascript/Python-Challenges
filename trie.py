endOfWord = "$"

def generateTrieFromWordsArray(words):
	root = {}
	for word in words:
		currentDict = root
		for letter in word:
			currentDict = currentDict.setdefault(letter, {})
		currentDict[endOfWord] = endOfWord
	return root

def generateTrieFromWordsArrayAndCountRepititions(words):
	root = {}
	for word in words:
		currentDict = root
		for letter in word:
			currentDict = currentDict.setdefault(letter, {})
		if endOfWord in currentDict:
			currentDict[endOfWord] = currentDict[endOfWord] + 1
		else: 
			currentDict[endOfWord] = 1
	return root

def isWordPresentInTrie(trie, word):
	currentDict = trie
	for letter in word:
		if letter in currentDict:
			currentDict = currentDict[letter]
		else: 
			return False
	if endOfWord in currentDict:
		return True
	else: 
		return False 

def offerPossibleCompletionsToStringInTrie(trie, string):
	currentDict = trie
	# step down to provided beginning of words
	for letter in string: 
		if letter in currentDict:
			currentDict = currentDict[letter]
		else:
			return "Trie does not offer any completions to %s" % (string)
	# now current dict is at the level which would offer completions. 
	printCompletionsFromNode(currentDict, string)

def printCompletionsFromNode(trie, string):
	currentDict = trie
	word = string
	# iterate over all children of the current letter node
	for letter in currentDict:
		# if the word is completed, print it
		if letter == "$":
			print(word)
		else:
			word = string + letter
			# function calls itself to handle all possible completions 
			printCompletionsFromNode(currentDict[letter], word)



arrayOfWords = ['hello', 'hey', 'what', 'when', 'why']
wordsTrie = generateTrieFromWordsArray(arrayOfWords)
# print wordsTrie['h']['e']
# print isWordPresentInTrie(wordsTrie, 'hello')
# print isWordPresentInTrie(wordsTrie, 'hellow')
print offerPossibleCompletionsToStringInTrie(wordsTrie, 'w')
