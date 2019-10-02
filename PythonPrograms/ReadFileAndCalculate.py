def GetOnlyHoursFromString(strVal):   
    pieces = strVal.split(" ")
    pieces = pieces[-1::-1]    
    return pieces[1].split(':')[0]
    
inputFile = input ("Enter file name:")
fileLines = open(inputFile)
lstLines = list()
hourVal=dict()

for lines in fileLines:
    if lines.startswith("From "):
       hour = GetOnlyHoursFromString(lines.strip())       
       hourVal[hour]=hourVal.get(hour,0) + 1

for k,v in sorted(hourVal.items()):
    print(k,v)
