file = input ("Enter file path:")
fileLines = open(file)
dctSender = dict()
for line in fileLines:
    if line.startswith("From "):        
        dctSender[line.split()[1]]=dctSender.get(line.split()[1],0) + 1

#to findout hight sender and its count
HighestSender = None
bigCount = None
for sender,count in dctSender.items():
    if bigCount is None or count > bigCount:
        bigCount = count
        HighestSender = sender
                
print(HighestSender,bigCount)
