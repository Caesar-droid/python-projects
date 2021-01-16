requested_toppings='mushrooms'
if requested_toppings != 'blueberry syrup':
    print("hold on to the blueberry syrup")
#testing multiple conditions
    requested_toppings=['mushroom','extra cheese']
    if 'mushroom' in requested_toppings:
        print("adding mushroom")
    if 'pepperonis' in requested_toppings:
        print("adding pepperonis")
    if 'extra cheese' in requested_toppings:
        print("adding extra cheese")
    print("\n Finished making your pizza")

#using loop to manipulate special items in list 
requested_toppings=['mushroom','green pepper','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green pepper':
        print('sorry, we are out of green pepper')
    else:
        print(f"adding {requested_topping}")

print("Finished making your pizza")
# #using for loop on an empty list
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"adding {requested_topping}")
    print('finally your pizza is ready')
else:
    print('do you want a plain pizza?')
    #using multiple lists
available_toppings=['mushroom','green pepper','pepperoni','olives','extra cheese','pineapple']
requested_toppings=['mushroom','french fries','extra cheese']
for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"adding {requested_topping}")
        else:
            print(f"we dont have the {requested_topping}")
print('finished making your pizza')