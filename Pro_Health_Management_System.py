#---------------------------> Health Managemant System <----------------------------------------
def dateandtime():
    import datetime
    return datetime.datetime.now()
date = dateandtime()
#------------------------------>Excersics and Diet Functions<-------------------------------------------

def excersicedeeksha():
    with open("ExcersiceDeeksha.txt", "a") as f:
        f.write(str(date)+"---------------->"+input("Enter the Excersice Name : ")+'\n')
        print("Date has inserted successfully")

def excersicesandhya():
    with open("ExcersiceSandhya.txt", "a") as f:
        f.write(str(date)+"---------------->"+input("Enter the Excersice Name : ")+'\n')
        print("Date has inserted successfully")

def excersiceshishupal():
    with open("ExcersiceShishupal.txt", "a") as f:
        f.write(str(date)+"---------------->"+input("Enter the Excersice Name : ")+'\n')
        print("Date has inserted successfully")

def dietdeeksha():
    with open("FoodDeeksha.txt", "a") as f:
        f.write(str(date)+"---------------->"+input("Enter Diet Name : ")+'\n')
        print("Date has inserted successfully")
def dietsandhya():
    with open("FoodSandhya.txt", "a") as f:
        f.write(str(date)+"---------------->"+input("Enter Diet Name : ")+'\n')
        print("Date has inserted successfully")
def dietshishupal():
    with open("FoodShishupal.txt", "a") as f:
        f.write(str(date)+"---------------->"+input("Enter Diet Name : ")+'\n')
        print("Date has inserted successfully")


# -----------------------------> Excersice and Diet Display Functions <--------------------------------------------------
def dietDeekshaDisplay():
    with open("FoodDeeksha.txt", "r") as f:
        print(f.read())

def dietSandhyaDisplay():
    with open("FoodSandhya.txt", "r") as f:
        print(f.read())

def dietShishupalDisplay():
    with open("FoodShishupal.txt", "r") as f:
        print(f.read())

def excersiceDeekshaDisplay():
    with open("ExcersiceDeeksha.txt", "r") as f:
        print(f.read())

def excersiceSandhyaDisplay():
    with open("ExcersiceSandhya.txt", "r") as f:
        print(f.read())

def excersiceShishupalDisplay():
    with open("ExcersiceShishupal.txt", "r") as f:
        print(f.read())
# -----------------------------> Main Loop & Structure <------------------------------------------------

print("---------------------------> Health Managemant System <----------------------------------------")
print("\n\n\n")
while True:
    try:
        num1 = print("1. Insert Information\n2. Retrieve")
        num1 = int(input("Enter Choice : "))
        break
    except Exception as e:
        print(e)
        print("Please enter valid input")
if(num1==1):
    try :
        num2 = int(input("\n1. Deeksha\n2. Sandhya\n3. Shishupal\nChoose a number : "))
        num3 = int(input("\n1. Diet\n2. Excersice()\nWhat you want to insert diet or Excersice : "))
        if (num2 == 1 and num3 == 1):  # Deeksha Diet File
            dietdeeksha()
        elif (num2 == 1 and num3 == 2):  # Deeksha Excersice
            excersicedeeksha()

        elif (num2 == 2 and num3 == 1):  # Sandhya Diet
            dietsandhya()

        elif (num2 ==2 and num3 ==2):  # ExcersiceSandhya
            excersicesandhya()

        elif (num2 ==3 and num3 ==1):  # DietShishupal
            dietshishupal()
        elif (num2 ==3 and num3 ==2):  # Diet shishupal
            excersiceshishupal()
        else :
            print("Invalid Input")

    except Exception as e:
        print(e)
        print("Inavalid Input")

else :
    num2 = int(input("\n1. Deeksha\n2. Sandhya\n3. Shishupal\nSelect the person for data : "))
    num3 = int(input("1. Diet\n2. Excersice\nEnter your choice : "))
    if(num2 == 1 and num3 == 1): # Deeksha ki diet
        dietDeekshaDisplay()
    elif(num2 == 1 and num3 == 2): #Deeksha ki Excersice
        excersiceDeekshaDisplay()
    elif(num2 == 2 and num3 == 1): # sandhya ki diet
        dietSandhyaDisplay()
    elif(num2 == 2 and num3 == 2): # sandhya ki Excersice
        excersiceSandhyaDisplay()
    elif(num2 == 3 and num3 == 1): # Shishupal ki diet
        dietShishupalDisplay()
    elif(num2 == 3 and num3 == 2): # Shishupal ki excersice
        excersiceShishupalDisplay()
    else :
        print("Invalid Input")

