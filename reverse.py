import sys

string = sys.argv[1]
listOfCharacters = list(string)
reversedList = list(reversed(string))
print ''.join(reversedList)
