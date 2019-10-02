# Read content from file
inputFileName = input("Enter file name:")
fileContent = open(inputFileName)
count = 0
total = 0
for line in fileContent:
    if line.startswith("X-DSPAM-Confidence:"):       
       total = total + float(line.replace('X-DSPAM-Confidence: ','').strip())
       count = count + 1
print("Average spam confidence:",float(total/count))

