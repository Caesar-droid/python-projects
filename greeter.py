name=input("Enter your name: ")
print(f"Hello, {name}")
#adding several lines
prompt = "we would like to know who u are.So that we can write you a personalized message."
prompt += "\nWhat is your first name: "
name=input(prompt)
print(f"Hello, {name}")
#using functions
def greet_user():
    """Display a simple greeting."""#the comment is called a docstring
    print("Hello!")
greet_user()
#passing information in a function
def greet_user(username):
    """this is a simple code"""
    print(f"Hello,{username.title()}")
greet_user('demabio')