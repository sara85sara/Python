def ComputePay(hour,rate):
    totalPay = None
    if (hour < 40):
        totalPay = hour * rate
    else:
        forFourtyHours = (40 * rate )  
        payforRemaingHours = (hour - 40) * (1.5 * rate )  
        totalPay = forFourtyHours + payforRemaingHours
    return totalPay
	
try:

    inputHour = float(input("Enter Hour:"))
    inputRate = float(input("Enter Rate:"))
    print(ComputePay(inputHour,inputRate))
    
except:
    print("Please enter valid hours and rate")
