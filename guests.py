filename='text_files/guest.txt'
with open(filename,'w') as file_object:
    name=input("What is your name: ")
    file_object.write(name)