def car_manufacture(manufacturer,model,**other_details):
    """We are going to write some description about a car."""
    other_details["manufacturer's_name"]=manufacturer
    other_details['model name']=model
    return other_details
car=car_manufacture('Toyota','Premio',color='marte black',tow_package=True,tax='40%')
print(car)