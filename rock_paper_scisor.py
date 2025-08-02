import random

user_won=0
comp_won=0

option=['rock','paper','scisor']

while True:
    user_input=input("Type ROCK/PAPER/SCISOR  or q to quit  the game.").lower()
     
    if user_input=='q':
        break

    if user_input not in option:
        continue


    random_guess=random.randint(0,2)
    comp_pick=option[random_guess]
    print(f"Computer picked {comp_pick} This time. ")

    if user_input=='rock' and comp_pick=='scisor':
        print("You Won")
        user_won+=1
    elif user_input=='paper' and comp_pick=='rock':
        print("You Won")
        user_won+=1
    elif user_input=='scisor' and comp_pick=='paper':
        print("You Won")
        user_won+=1
    elif user_input == comp_pick:
        print("It's a tie!")
    else:
        print("You lost ")
        comp_won+=1

print(f"you won {user_won} times")
print(f"computer won {comp_won} times")
print("Good-Bye! ")