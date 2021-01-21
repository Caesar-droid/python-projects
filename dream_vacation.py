#creating an empty dictionary
vacations={}
#set a flag
active=True
while active:
    #prompt user to enter usser
    username=input("\nPlease enter your username...")
    dream=input(f"{username.title()},if you are to visit any place in the world,where would you go?")
    vacations[username]=dream
    repeat=input("would you like to continue?('yes'/'no')")
    if repeat == 'no':
        active=False
print("--POLL RESULTS--")
for username,dream in vacations.items():
    print(f"{username},your dream place is: {dream}")
