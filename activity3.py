from random import randint
#Swertress 
bet = input("Enter your bet: ")
result = str(randint(100,999))
print(f"Result = {result}")
if bet == result:
    print("You Win!")
elif sorted(bet) == sorted(result):
    print("Partially Win")
elif len(bet) != len(result):
    print("Invalid Input")
else: 
    print("You Loss!")