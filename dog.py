#we are going to create a class Dog that stores information about name,age and other functions common to dogs
class Dog:
    """A simple attempt to model a dog."""
    def __init__(self,name,age):
        """Initialize name and age attributes."""
        self.name=name
        self.age=age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
my_dog=Dog('Willie',6)
your_dog=Dog('bosco',4)
#using dot notation to access individual attributes
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()

print(f"\nMy dog's name is {your_dog.name.title()}")
print(f"My dog is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()
