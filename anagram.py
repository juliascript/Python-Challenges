import sys, random

string = sys.argv[1]
listOfCharacters = list(string)
random.shuffle(listOfCharacters)
print ''.join(listOfCharacters)
