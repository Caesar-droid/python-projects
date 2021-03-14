class Employee:
    """A class to represent an employee."""
    def __init__(self,first_name,last_name,annual_salary):
        """Initialize the employee."""
        self.first_name=first_name.title()
        self.last_name=last_name.title()
        self.annual_salary=annual_salary
    def give_rise(self,new_value=5000):
        """Gives the employee a raise."""
        self.annual_salary+=new_value