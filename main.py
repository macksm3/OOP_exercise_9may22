# Homework for the week of May 9th, 2022
# Experimenting with Object-Oriented Programming (OOP)
# by Michael Macks McCosh (MacksM3)

from pets import *
from tkinter import *

petType = ["Cat", "Parrot", "Gecko"]

x = Dog("Spot")


def click(event):
    print(f"The new name is {newName.get()}")
    newPetPicture.config(text=f"What type of pet\nwill {newName.get()} be?")
    for index in range(len(petType)):
        radiobutton = Radiobutton(petSelectFrame,
                                  text=petType[index],  # adds text to radio buttons
                                  variable=f,  # groups radio buttons together if they share the same variable
                                  value=index,  # assigns each radio button a different value
                                  # padx=10,
                                  font=("Impact", 15),
                                  image=petImages[index],  # adds image to radio button
                                  compound='left',  # adds image and text (left side)
                                  indicatoron=False,  # eliminate circle indicators
                                  width=150,  # sets width of radio buttons
                                  command=select_pet  # set command of radiobutton to function
                                  )
        radiobutton.pack()


def select_pet():
    petSelectFrame.destroy()
    if f.get() == 0:
        newCat = Cat(newName.get())
        print(newCat.speak())
        newPetOutput.config(text=newCat.speak())
        newPetPicture.config(image=catImage)
    elif f.get() == 1:
        newParrot = Bird(newName.get())
        print(newParrot.speak())
        newPetOutput.config(text=newParrot.speak())
        newPetPicture.config(image=parrotImage)
    elif f.get() == 2:
        newGecko = Gecko(newName.get())
        print(newGecko.speak())
        newPetOutput.config(text=newGecko.speak())
        newPetPicture.config(image=geckoImage)

    quit_button.grid(row=4, column=0, columnspan=2, sticky=S)


# GUI code starts here
window = Tk()
window.title("Spot gets a new pet")
window.geometry("380x300")

icon = PhotoImage(file='m3-blue-icon.png')
window.iconphoto(True, icon)

dogImage = PhotoImage(file='icons8-puppy-96.png')
dogPicture = Label(window, image=dogImage)
dogPicture.grid(row=0, column=0)

dog_label = Label(window, text=(x.speak() + "\nAnd I am getting a new pet."))
dog_label.grid(row=0, column=1)

# Please ask the user to provide a name for a cat.
# newName = input("What shall we name them? ")
input_label = Label(window, text=" What shall we name them?")
input_label.grid(row=1, column=0)
newName = Entry(window)
newName.grid(row=1, column=1)
newName.focus()
window.bind('<Return>', click)

catImage = PhotoImage(file='icons8-kitty-96.png')
parrotImage = PhotoImage(file='icons8-parrot-96.png')
geckoImage = PhotoImage(file='icons8-lizard-96.png')

newPetPicture = Label(window, )
newPetPicture.grid(row=2, column=0)

newPetOutput = Label(window)
newPetOutput.grid(row=2, column=1, pady=30)

# radio buttons generated from list with for loop
catIcon = PhotoImage(file='icons8-kitty-24.png', )
parrotIcon = PhotoImage(file='icons8-parrot-24.png')
geckoIcon = PhotoImage(file='icons8-lizard-24.png')
petImages = [catIcon, parrotIcon, geckoIcon]
f = IntVar()

petSelectFrame = Frame(window, relief="raised", bd=3)
petSelectFrame.grid(row=2, column=1, pady=30)
radiobutton = Radiobutton(petSelectFrame, )
# radiobutton.pack()

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

quit_button = Button(window, text="Exit Program", width=15, command=window.quit)

window.mainloop()

# end of program
