from functions import *

print("Welcome to my computer quiz!")
playing = input("Do you want to play? (Y/N) ")
if playing.lower() != "y":
    quit()
print("Okay lets play :)")

game()
