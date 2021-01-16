prompt="Tell me something,and i will repeat it to you: "
prompt+="\ntell the user to 'quit' "
active= True
while active == True:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)