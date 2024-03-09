import os

c = 0
filename = "q1.txt"
wordCount = {}

if not os.path.exists(filename):
    file = open(filename, "w")
    print("File opened for writing:", file.name)
else:
    file = open(filename, "r")
    print("File already exists and opened for reading:", file.name)
    readFile = file.read()
    cleanText = readFile.replace(',', ' ').replace('.', ' ')
    splitFileWords = cleanText.split()
    
    for word in splitFileWords:
        if word in wordCount.keys():
            wordCount[word] += 1
        else:
            wordCount[word] = 1

    sortedDict = sorted(wordCount.keys(), key=lambda x: wordCount[x], reverse=True)
    print("Word count:")
    for word in sortedDict:
        print(f'{word}: {wordCount[word]}')

file.close()
