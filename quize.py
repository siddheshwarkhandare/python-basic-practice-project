import random

uper_limit_of_range=int(input("type an number for uperr limit: "))
if uper_limit_of_range.is_integer():
   quit
else:
    print("please enter a intrger")

r=random.randrange(1,uper_limit_of_range)
gusse=0

while True:
    gusse+=1
    user_input= int(input("Enter your gusse: "))
    if user_input.is_integer:
        quit
    else:
        print("please enter integer ")
        continue


    if user_input== r:
        print("your got it right  ")
        break
    elif user_input > r:
        print("your above the number")
    else:
        print("your below the number")
            
    
print("you gusse in",gusse, "gusses")
        


