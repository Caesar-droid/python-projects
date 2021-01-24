pets=['dog','cat','goldfish','cat','dog','parrot','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
#positional arguments
def describe_pet(animal_type,pet_name):

    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
#multiple function calls
describe_pet(animal_type='hamster',pet_name='poop')
describe_pet(pet_name='poop',animal_type='hamster')
describe_pet('dog','scooby')
#default values
def describe_pet(pet_name,animal_type='dog'):

    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
describe_pet(pet_name='scooby')