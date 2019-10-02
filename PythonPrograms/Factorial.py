inputVal = int(input("Enter a value which you want to find factorial:")) 
factValue = 1
if(inputVal==0):
    factValue=0
else:
    for fact in range(1,inputVal + 1):
            factValue = factValue * fact    
print("Factorial value is :" + str(factValue))

    
