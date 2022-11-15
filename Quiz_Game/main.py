print("Welcome to my computer quiz!")

playing = input("Do you want to play? (Y/N) ")
# .lower changes answer to lowercase so all casing will work
if playing.lower() != "y":
    quit()

print("Okay lets play :)")

point = 0
question = 0
percentage_correct = 0

def score_statement() :
    # str() changes int to str to put into print for joining words.
    print("You got ",str(point)," points")
    percentage_correct = (point/question) *100
    print("You got "+ str(percentage_correct)+ "% correct!")
    return 


def question_statement(question, correct_Answer):
    temp_answer = input(question)
    if temp_answer.lower() == correct_Answer:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False 

#temp question
if question_statement("My name? " , "randall") :
    point += 1
question +=1


#question 0
if question_statement("What does CPU stand for? " , "central processing unit") :
    point += 1
question +=1


#question 1
if question_statement("What does GPU stand for? " , "graphic processing unit") :
    point += 1
question +=1

#question 2
if question_statement("What does PSU stand for? " , "power supply") :
    point += 1
question +=1

#question 3
if question_statement("What does RAM stand for? " , "random access memory") :
    point += 1
question +=1

score_statement()

input ("Play Again? (Y/N) ")