# name=input("Enter your name: ")
# print(f"Hello, {name}")
# #adding several lines
# prompt = "we would like to know who u are.So that we can write you a personalized message."
# prompt += "\nWhat is your first name: "
# name=input(prompt)
# print(f"Hello, {name}")
# #using functions
# def greet_user():
#     """Display a simple greeting."""#the comment is called a docstring
#     print("Hello!")
# greet_user()
# #passing information in a function
# def greet_user(username):
#     """this is a simple code"""
#     print(f"Hello,{username.title()}")
# greet_user('demabio')
#using function with while loop 
def greet_user(first_name,last_name):
    """write your fullname and get it well formatted."""
    fullname=f"{first_name} {last_name}"
    return fullname.title()

#getting an infinite loop
while True:
        print("\nWhat is your name?")
        print("Enter 'q' if at any point of the program you want to quit")
        f_name=input("firstName: ")
        if f_name == 'q':
            break
        l_name=input("lastName: ")
        if l_name == 'q':
            break
        formatted_name=greet_user(f_name,l_name)
        print(f"\nHello,{formatted_name.title()}")