# Homework for the week of May 9th, 2022
# Experimenting with Object Oriented Programming (OOP)
# by Michael Macks McCosh (MacksM3)

from pets import *
from tkinter import *


x = Dog("Spot")
def click(event):
    print(f"The new name is {newName.get()}")
    newCat = Cat(newName.get())
    print(newCat.speak())
    newPetOutput.config(text=newCat.speak())
    newPetPicture.config(image=catImage)

# GUI code starts here
window = Tk()
window.title("Spot gets a new pet")
window.geometry("500x250")

icon = PhotoImage(file='m3-blue-icon.png')
window.iconphoto(True, icon)

dogImage = PhotoImage(file='icons8-puppy-96.png')
dogPicture = Label(window, image=dogImage)
dogPicture.grid(row=0, column=0)

dog_label = Label(window, text=(x.speak() + "\nAnd I am getting a new pet."))
dog_label.grid(row=0, column=1)


# print(x.speak())
# print(type(x))
#Label(window, text="And I am getting a new pet.").pack()

# Please ask the user to provide a name for a cat.
# newName = input("What shall we name them? ")
input_label = Label(window, text="What shall we name them? ")
input_label.grid(row=1, column=0)
newName = Entry(window)
newName.grid(row=1, column=1)
newName.focus()
window.bind('<Return>', click)

catImage = PhotoImage(file='icons8-kitty-96.png')


newPetPicture = Label(window,)
newPetPicture.grid(row=2, column=0)

newPetOutput = Label(window)
newPetOutput.grid(row=2, column=1, pady=30)

'''
print("The new pet can be one of the following:")
print(" ")
print("(c)at")
print("(g)ecko")
print("(p)arrot")
print(" ")

# ask user to choose type of pet
i = input("Your choice? ")
i = i.upper()

if i == "G":
    newGecko = Gecko(newName)
    print(newGecko.speak())

elif i == "P":
    newBird = Bird(newName)
    print(newBird.speak())

elif i == "C":
    newCat = Cat(newName)
    print(newCat.speak())
'''



window.mainloop()


# end of program
