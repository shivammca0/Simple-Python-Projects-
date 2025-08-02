import random

top_of_range=input("Enter top-range number you want to guess from 0 to top-range")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<0:
        print("please Enter the number above then 0")
        quit()
else:
    print("Enter only Numbers. ")
    quit()

comp_number=random.randint(0,top_of_range)
guess=0
print(" Welcome to the Guessing Game!")
print(f"I have selected a number between 1 and {top_of_range}. Can you guess it?")
while True:
    guess+=1
    user_guess=(input("Enter you number. "))
    if user_guess.isdigit():
        user_guess=int(user_guess)

        if user_guess<0:
            print("please Enter the number above then 0")
            continue
    else:
        print("Enter only Numbers. ")
        continue

    if user_guess==comp_number:
        print("Yeaaah ! you Got It. :) ")
        break
    elif user_guess < comp_number:
        print("Guess a BIGGER number.")
    else:
        print("Guess a SMALLER number.")

print(f"So you guess the number in {guess} times ")