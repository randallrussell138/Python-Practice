import random 


top_of_range = input("Type a number: ")
guess_count = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_num = random.randint(0,top_of_range)

while True:
    guess_count += 1
    user_guess = input("Type a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_num:
        print("You got it!")
        break
    #if-else inside of if-else statement
    elif user_guess > random_num:
            print("You were above!")
    else:
            print("You were below!")

print("You got it in", guess_count, "guesses!")