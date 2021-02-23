filename='text_files/programming_poll.txt'
print("Enter 'quit' if you wanna exit...")
while True:
    response=input("Why do you like programming?")
    if response == 'quit':
        break
    else:
        with open(filename,'a') as fo:
            fo.write(response+"\n")
#solution
filename='text_files/programming_poll.txt'
responses=[]
while True:
    response=input("\nWhy do you like programming?")
    responses.append(response)
    continue_polling=input("would you like to let someone else respond? (y/n)")
    if continue_polling != 'y':
        break
with open (filename,'a') as f:
    for response in responses:
        f.write(response+"\n")