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
