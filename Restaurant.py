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
restaurant=Restaurant('beans & cream','korean')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(40)
restaurant.describe_restaurant()


restaurant_1=Restaurant("CJ's",'chinesse')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2=Restaurant('hilton','caribbean')
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()