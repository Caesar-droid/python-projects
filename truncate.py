#i will review since it has not yet worked
year=int(input("Enter any year? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"the {year} you have entered is a leap year")
        else:
            print(f"the {year} you have provided is not a leap year")
       
            