pets=['dog','cat','goldfish','cat','dog','parrot','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
#positional arguments
def describe_pet(animal_type,pet_name):

    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
describe_pet('hamster','poop')