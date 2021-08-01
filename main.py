import random
number = random.randint(1,9)
guess = int(input("guess a number between 1-10: "))
print(number)
if (guess==number):
    print("Congrats you won!!")
elif(guess==number-5):
    print("very close")
elif(guess==number+5):    
    print("very close")
else:
    print("please try again")