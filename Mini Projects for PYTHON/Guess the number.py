import random

target = random.randint(1,100)

print("\nGUESSING THE NUMBER GAME ")
print("\nAre you ready to play the guessing no. game ? \n \nLet's See... \nAre you Good enough to guess the Number ? ")
Name = input("Enter your name to play the game : ")
print("\nHello", Name, "!!\n")
print("Rules : Please enter the number between 1 to 100")
print("\nLet's begin!!!\n")

while True:
    userChoice = input("Guess the target or Quit(Q) : ")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess !!!")
        break
    elif(userChoice < target):
        print("your number was too small. Take a bigger guess...")

    elif(userChoice > 100):
        print("ERROR. \nPlease enter number between 1 to 100. \nTry again")
        break

    elif(userChoice < 1):
        print("ERROR. \nPlease enter number between 1 to 100. \nTry again")
        break
    else:
        print("your number was too big. Take a smaller guess....")

print("-----GAME OVER------")