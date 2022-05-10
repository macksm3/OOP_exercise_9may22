# Homework for the week of May 9th, 2022
# Experimenting with Object Oriented Programming (OOP)
# by Michael Macks McCosh (MacksM3)

from pets import *


# main function starts here
def main():
    x = Dog("Spot")
    print(x.speak())
    # print(type(x))
    print("And I am getting a new pet.")

    # Please ask the user to provide a name for a cat.
    newName = input("What shall we name them? ")
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

    return  # end of main function here


# the below code is used to differentiate if
# the program is being executed directly by
# the Python interpreter, or imported as a mdoule.

if __name__ == "__main__":
    main()

# end of program
