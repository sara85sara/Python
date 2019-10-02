inputFileName = input("Enter file name: ")
fileContent = open(inputFileName)
lst = list()
for line in fileContent:
    pieces = line.strip().split()
    AddItemsList(pieces)
    #lst.append(pieces)
    #for piece in pieces:
        #if piece not in lst:
            #lst.append(line)
print(lst)            


def AddItemsList(lstString):
    stringList = list()
    for value in lstString:
        if value not in stringList:
            stringList.append(value)
print(stringList)