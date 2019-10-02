hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if(h < 40):
    print (h * r)
else:
    forFourtyHours = (40 * r )   
    remainingHours = h % 40
    print(remainingHours)
    payforRemaingHours = remainingHours * (1.5 * r )
    print(payforRemaingHours)
    print(forFourtyHours + payforRemaingHours)
    