# Homework for the week of May 9th, 2022
# Experimenting with Object Oriented Programming (OOP)
# by Michael Macks McCosh (MacksM3)

# parent class for all the pets to inherit from
class Pet:
    def __init__(self, name):
        self.name = name
        print("***New Pet Materializing!!!***")
        print()


# class definition of 'Dog' starts here
class Dog(Pet):
    # class attribute
    at1 = "mammal"

    def __init__(self, name):
        super().__init__(name)

    # Instance method
    def speak(self):
        return f"I am a Dog. \nMy name is {self.name}, \nI am a {self.at1},"


# class definition of 'Cat' starts here
class Cat(Pet):
    # class attribute
    at1 = "mammal"

    def __init__(self, name):
        super().__init__(name)

    # Instance method
    def speak(self):
        return f"Hello! \nI am a Cat. \nMy name is {self.name}. \nAnd I am a {self.at1}."


# class definition of 'Bird' starts here
class Bird(Pet):
    # class attribute
    at1 = "bird"

    def __init__(self, name):
        super().__init__(name)

    # Instance method
    def speak(self):
        return f"Hello! \nI am a Parrot. \nMy name is {self.name}. \nI am a {self.at1}."


# class definition of 'Gecko' starts here
class Gecko(Pet):
    # class attribute
    at1 = "reptil"

    def __init__(self, name):
        super().__init__(name)

    # Instance method
    def speak(self):
        return f"Hello! \nI am a Gecko. \nMy name is {self.name}. \nAnd I am a {self.at1}."


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
