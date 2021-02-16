filename='text_files/programming_poll.txt'
print("Enter 'quit' if you wanna exit...")
while True:
    response=input("Why do you like programming?")
    if response == 'quit':
        break
    else:
        with open(filename,'a') as fo:
            fo.write(response+"\n")
            