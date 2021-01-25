def greet_users(names):
    """The simple greetings to a user."""
    for name in names:
        msg=f"Hello,{name.title()}!"
        print(msg)
usernames=['caesar','kyle','domie','doodleshot','sentinel']
greet_users(usernames)