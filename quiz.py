# Quiz game for fun

def score_save(score):

    with open("score.txt", "a") as file:
        file.write(f"Your score is: {score}\n")

    print("Score saved successfully!")

def score_read():

    with open("score.txt", "r") as file:
        data= file.read()
        print(data)

    
def quiz_game():
    print("Starting Quiz....")
    score=0

    answer=input("What does CPU stand for? ")
    if answer.lower()=="central processing unit":
        print('correct!')
        score=score+1
    else:
        print("incorrect!")
       

    answer=input("What does GPU stand for? ")
    if answer.lower()=="graphics processing unit":
        print('correct!')
        score=score+1
    else:
        print("incorrect!")

    answer=input("What does RAM stand for? ")
    if answer.lower()=="random access memory":
        print('correct!')
        score=score+1
    else:
        print("incorrect!")

    answer=input("What does IT stand for? ")
    if answer.lower()=="information technology":
        print('correct!')
        score=score+1
    else:
        print("incorrect!")

    print(f"Your score is {score} ")
    print(f"You Give {(score/4)*100}% correct Answer")
    score_save(score)

 




def main():
    print("Welcome to Arena. :) ")
    while True:
        print("1. Start the Quiz. ")
        print("2. See. The Rank.")
        print("3. Exit ")
        case=int(input("Select The Option.. "))

        match case:
            case 1:
                quiz_game()
            case 2:
                score_read()
            case 3:
                print("Thanks you for your time..")
                break
            case _:
                print("Please Enter valid option")

if __name__=="__main__":
    main()