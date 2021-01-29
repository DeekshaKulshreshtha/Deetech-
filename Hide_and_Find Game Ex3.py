def game_logic():
    print("********************************Game starts now**************************************")
    no_of_passes = 1
    while (no_of_passes <= 5):
        print("The number should be between 1 to 50")
        num = int(input("Enter the number : "))
        if (num == n):
            print("Correct guess!!! The hidden number is 18")
            print("You guessed the number in ",no_of_passes, " passes")
            break
        elif (num < n):
            print("Enter the greater number ")
            print(5 - no_of_passes, "passes are left")
        elif(num>50):
            print("Don't enter the number greater then 50")
            print(5 - no_of_passes, "passes are left")
        else:
            print("Enter the lesser number : ")
            print(5 - no_of_passes, "passes are left")
        no_of_passes += 1
    if(no_of_passes==0):
        print("You have lost the game!!!")
    ch = input("Do you want to play again enter Y or N : ")
    if(ch == "y" or ch == 'Y'):
        game_logic()
    else:
        print("You have exited!!!")


print("*******************************************GUESS THE NUMBER**********************************************************\n\n")
n = 18
game_logic()
