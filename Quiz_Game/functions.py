#variables
point_total = 0
question_total = 0
percentage_correct = 0

#function for formating the questions and analysising it
def QuestionStatement(question, correct_Answer):
    #need global bc it was outside bounds
    global point_total
    global question_total
    temp_answer = input(question)
    if temp_answer.lower() == correct_Answer:
        print("Correct!")
        point_total += 1
    else:
        print("Incorrect!")
    question_total += 1

def EndStatement() :
    # str() changes int to str to put into print for joining words.
    print("You got ",str(point_total)," points")
    percentage_correct = (point_total/question_total) *100
    print("You got "+ str(percentage_correct)+ "% correct!")
    return 

def game(): 
    #had to fix global variables
    global point_total
    global question_total
    global percentage_correct
    point_total = 0
    question_total = 0
    percentage_correct = 0

     #Questions
    QuestionStatement("What does CPU stand for? " , "central processing unit")
    QuestionStatement("What does GPU stand for? " , "graphics processing unit")
    QuestionStatement("What does PSU stand for? " , "power supply")
    QuestionStatement("What does RAM stand for? " , "random access memory")

    #printing ending score
    EndStatement()
    playagain()

def playagain():
    while True:
        playagain = input("Play Again? (Y/N) ")
        # .lower changes answer to lowercase so all casing will work
        if playagain.lower() == "y":
            game()
        elif playagain.lower() == "n":
            print("Ok, Bye!!")
            quit()
        else:    
            print("That isnt Y/N !")