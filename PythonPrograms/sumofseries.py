def sumofseries(inputnumber):
    sum = None
	if(inputnumber == 0):
        return 0:
	else:
        for(runningnmber in range(1,inputnumber)):
            sum = sum + runningnmber
    return sum

try:
    while True:
            userInput = input("Enter any number to find the total Serious")
            if (userIinput == 'Y'):
                break                
            print(sumofseries(userInput))
          
except:
    print("Please enter integer to calculate")
    

