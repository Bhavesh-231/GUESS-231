import random
number=random.randrange(1,100)
guess=int(input("enter the number you guessed"))

while guess!=number:
    if guess < number:
          print("number guessed is lower")
          guess=int(input("enter the number you guessed"))
    else:
        print("number guessed is higher")
        guess=int(input("enter the number you guessed"))
print("you entered correct number")
