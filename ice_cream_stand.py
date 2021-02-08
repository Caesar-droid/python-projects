class Restaurant:
    """We trying to model a restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        """we are going to initialize attributes"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        """we are creating a function that describes""" 
        print(f"\nWe are {self.restaurant_name} restaurant.")
        print(f"We are offering {self.cuisine_type} cuisine.")
        print(f"The restaurant has served {self.number_served} customers")
    def open_restaurant(self):
        """we are creating a function that displays we are open"""
        print(f"{self.restaurant_name.title()}, we are now open")
    def set_number_served(self,number):
        self.number_served=number
class IceCreamStand():
    def __init__(self):
        self.flavors=flavors
    def list_of_flavours(self):
        print("Here is a list of flavours we are offering...")
        for flavor in flavors:
            print(flavor)
flavors=['caramel','chocolate','bluberry','cinnamon']
my_ics=IceCreamStand()
my_ics.list_of_flavours()