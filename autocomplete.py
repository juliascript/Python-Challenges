import sys, enchant 

beginningOfWord = raw_input("Enter the beginning of a word to be autocompleted: ")

englishDict = enchant.Dict("en_US") 
print englishDict.suggest(beginningOfWord)