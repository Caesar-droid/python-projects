#we are creating a class on users
class User:
    def __init__(self,first_name,last_name,location,email,age):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.email=email
        self.age=age
    def describe_user(self):
        print(f"I'm {self.first_name} {self.last_name} \nFrom {self.location} and, \nThis is my email address {self.email} aged {self.age}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")
my_user=User('domie','kyle','nairobi','a613@gmail.com',20)
my_user.describe_user()
my_user.greet_user()