pizzas=['pepperoni','cheese','chicken periperi']
for pizza in pizzas:
    print("\n")
    print(pizza)
    print(f"i enjoy eating {pizza.title()} pizza")
print('i really like pizza so much.\nThe crunchy feeling,the taste.\n I mean its on another level i kent really explain.\n The chilli feeling is on another level')
print("i love pizzas")
#storing information about pizza being ordered
pizza={
    'crust': 'thick',
    'toppings': ['extra cheese','mushroom']
    }
#summarizing the order
print(f"you are ordering a {pizza['crust']}-crust pizza"
 " with the following toppings: ")
for topping in pizza['toppings']:
     print("\t"+topping)
#passing an arbitrary number of arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    """"summarize the pizza you are about to make."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
#mixing positional and arbitrary arguments
def make_pizza(size,*toppings):
    """Summarize the pizza we are about to make."""
    print(f"Making a {size}- inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green pepper','extra cheese')