print("Welcome to my computer quiz!")

playing = input("Do you want to play? (Y/N) ")
# .lower changes answer to lowercase so all casing will work
if playing.lower != "y":
    quit()

print("Okay lets play :)")

point = 0
question = 0
percentage_correct = 0

def score_statement() :
    # str() changes int to str to put into print for joining words.
    print("You got ",str(point)," points")
    percentage_correct = (point/question) *100
    print("You got"+ str(percentage_correct)+ "% correct!")
    return 

#question 0
answer = input("What does CPU stand for? ")
if answer.lower == "central processing unit":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")
question += 1
score_statement()

#question 1
answer = input("What does GPU stand for? ")
if answer.lower == "graphic processing unit":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")
question += 1
score_statement()

#question 2
answer = input("What does PSU stand for? ")
if answer.lower == "power supply":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")
question += 1
score_statement()

#question 3
answer = input("What does RAM stand for? ")
if answer.lower == "random access memory":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")
question += 1
score_statement()
