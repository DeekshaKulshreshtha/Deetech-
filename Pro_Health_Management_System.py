#---------------------------> Health Managemant System <----------------------------------------
def dateandtime():
    import datetime
    return datetime.datetime.now()
date = dateandtime()
#------------------------------>Excersics and diet Functions<-------------------------------------------

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
    with open("FoodSandhya.txt.txt", "a") as f:
        f.write(str(date)+"---------------->"+input("Enter Diet Name : ")+'\n')
        print("Date has inserted successfully")
def dietshishupal():
    with open("FoodShishupal.txt.txt", "a") as f:
        f.write(str(date)+"---------------->"+input("Enter Diet Name : ")+'\n')
        print("Date has inserted successfully")

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
    except Exception as e:
        print(e)
        print("Inavalid Input")