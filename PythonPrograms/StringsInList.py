fname = input("Enter file name: ")
fh = open(fname)
stringLst = list()
#reading line by line
for line in fh:
    pieces = line.split()
    print(pieces)
    #seperate word from the line and adding into list
    for piece in pieces:
        if piece not in stringLst:
            stringLst.append(piece)
            print(stringLst)

#print(stringLst.sort())
