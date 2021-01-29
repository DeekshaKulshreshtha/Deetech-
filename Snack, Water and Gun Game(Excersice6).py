import random
print("------------------------------------------------> Snack, Water and Gun Game <---------------------------------------")
n = 0
lives = 9-n
player1 = 0
player2 = 0
print("You have 10 lives")
player = str(input("Enter your name : "))
print("S - Sanke\nG - Gun\nW - water\n\n")

while(n!=10):
    try:
        lst = ['w', 's', 'g', "W", "S", "G"]
        num1 = random.choice(lst)
        # print(f"Computer has choosen {num1}")
        num2 = input("Select any character from S G and W you can enter in both cases upper and lower case : ")

# --------------------------------------------------> 3 cases for snake <-------------------------------------------------------------
        if((num1 == "S" or num1 == 's') and (num2 == 's' or num2 == "S")):
            print(f"TIE!!!\nBecause both have selected Sanke\t\t\t\t Left chance: {lives-n}\n\n")

        elif((num1 == "S" or num1 == 's') and (num2 == 'g' or num2 == "G")):
            print(f"{player} wins!!!\t\t\t\t Left chance: {lives-n}\n\n")
            player2+=1

        elif(num1 == "S" or num1 == 's' and num2 == 'w' or num2 == "W"):
            print(f"Computer wins!!!\t\t\t\t Left chance: {lives-n}\n\n")
            player1+=1

# --------------------------------------------------> 3 cases for Water <-------------------------------------------------------------

        elif((num1 == "W" or num1 == 'w') and (num2 == 'W' or num2 == 'w')):
            print(f"TIE!!!\nBecause both have selected water\t\t\t\t Left chance: {lives-n}\n\n")
        elif((num1 == "W" or num1 == 'w') and (num2 == 's' or num2 == 'S')):
            print(f"{player} wins!!!\t\t\t\t Left chance: {lives-n}\n\n")
            player2 += 1
        elif((num1 == "W" or num1 == 'w') and (num2 == 'G' or num2 == 'g')):
            print(f"{player} wins!!!\t\t\t\t Left chance: {lives-n}\n\n")
            player2 += 1

# --------------------------------------------------> 3 cases for Gun <-------------------------------------------------------------

        elif((num1 == "G" or num1 == 'g') and (num2 == 'g' or num2 == "G")):
            print(f"TIE!!!\nBecause both have selected water\t\t\t\t Left chance: {lives-n}\n\n")
        elif(num1 == "g" or num1 == 'G' and num2 == 's' or num2 == "S"):
            print(f"Computer wins!!!\t\t\t\t Left chance: {lives-n}\n\n")
            player1+=1
        elif (num1 == "g" or num1 == 'G' and num2 == 'w' or num2 == "W"):
            print(f"{player} wins!!!\t\t\t\t Left chance: {lives-n}\n\n")
            player1 += 1
        else :
            print("invalid Input\t\t\t\t Left chance: {lives}\n\n")
    except Exception as e:
        print(e)

    n +=1

# --------------------------> score <--------------------------------------------------------
if(player1>player2):
    print("Computer win wins!!!\n")
else :
    print(f"{player} wins!!!\n")

print(f"{player} : {player2} and Computer : {player1}\n\n")