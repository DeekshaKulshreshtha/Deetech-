from tkinter import *
root = Tk()

def msg():
    print("Your data has been successfully submitted")

root.geometry("733x434")
root.title("Tkinter")


Label(root, text = "Dance Class", font = "Calibri 20 bold", pady = 15).grid(row = 0, column = 10)

name = Label(root, text = "Name : ", pady = 5)
Gender = Label(root, text = "Gender : ", pady = 5)
age = Label(root, text = "Age : ", pady = 5)
dob = Label(root, text = "Date of Birth : ", pady = 5)
contactnumber = Label(root, text = "ContactNumber : ", pady = 5)

# packing labels
name.grid(row = 1, column = 2)
Gender.grid(row = 2, column = 2)
age.grid(row = 3, column = 2)
dob.grid(row = 4, column = 2)
contactnumber.grid(row = 5, column = 2)

# creating values
namevalue = StringVar()
Gendervalue = StringVar()
agevalue = StringVar()
dobvalue = StringVar()
contactnumbervalue = StringVar()
choicevalue = IntVar()

# creating entry
nameentry = Entry(root, textvariable = namevalue)
Genderentry = Entry(root, textvariable = Gendervalue)
ageentry = Entry(root, textvariable = agevalue)
dobentry = Entry(root, textvariable = dobvalue)
contactnumberentry = Entry(root, textvariable = contactnumbervalue)

# packing values
nameentry.grid(row = 1, column = 3)
Genderentry.grid(row = 2 , column =3 )
ageentry.grid(row = 3, column = 3)
dobentry.grid(row = 4, column = 3)
contactnumberentry.grid(row = 5, column = 3)

# checkbox
button = Checkbutton(root, text = "Would you like to submit the data", variable = choicevalue, pady = 5)
button.grid(row = 6, column = 3)

# Button
Button(text = "Submit", command = msg).grid(row = 7, column = 3)
root.mainloop()