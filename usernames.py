usernames=['admin','caesar','dre','moonwalker','wine taster','localman']
for username in usernames:
    if username =='admin':
        print(f"Hello {username},would you like to view status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
#no users
usernames=[]
if usernames:
    for username in usernames:
        print(f"Hello {username},thank you for loggin in again")
else:
    print("we need to add more users")