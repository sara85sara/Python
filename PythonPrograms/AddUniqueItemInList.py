inputFile = input ("Please enter your file name:")
fileLines = open(inputFile)
lstUniqueWords = list()
for lines in fileLines:
       words = lines.split()
       for word in words:
           if word not in lstUniqueWords:
               lstUniqueWords.append(word)
lstUniqueWords.sort()
print(lstUniqueWords)
       

        
