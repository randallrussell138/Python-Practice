print("Welcome to my computer quiz!")

playing = input("Do you want to play? (Y/N) ")

if playing != "Y":
    quit()

print("Okay lets play :)")

point = 0
question = 0
percentage_correct = 0

def score_statement() :
    print("You got ",int(point)," points")
    percentage_correct = (point/question) *100
    print(percentage_correct)
    return 

answer = input("What does CPU stand for? ")

if answer == "Central Processing Unit":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

question += 1

score_statement()

def score_statement() :
    print("You got ",int(point)," points")
    percentage_correct = (point/question) *100
    print(percentage_correct)
    return 

answer = input("What does CPU stand for? ")

if answer == "Central Processing Unit":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

question += 1

score_statement()

def score_statement() :
    print("You got ",int(point)," points")
    percentage_correct = (point/question) *100
    print(percentage_correct)
    return 

answer = input("What does CPU stand for? ")

if answer == "Central Processing Unit":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

question += 1

score_statement()
