def PrintEmailAddress(emailAddress):
    for email in emailAddress:
        print(email)


inputFileName = input("Enter file name: ")
fileContent = open(inputFileName)
lst = list()
count = 0
for line in fileContent:
    if line.startswith("From "):
        count = count + 1
        foundLine = line.split()
        lst.append(foundLine[1].strip())
PrintEmailAddress(lst)
print("There were", count, "lines in the file with From as the first word")

