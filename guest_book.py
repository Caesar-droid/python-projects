# #1st trial
# filename='text_files/guest_book.txt'
# active =True
# while True:
#     name=input("Please enter your name: ")
#     print(f"Hello,{name.title()}")
#     if name =='q':
#         # active=False
#         break
#     with open(filename,'w') as file_object:
#         file_object.write(f"{name}, i was here on official purpose.\n")
#solution
filename='text_files/guest_book.txt'
print("Enter 'quit' when you are finished.")
while True:
    name=input("\nWhat's your name?")
    if name == 'quit':
        break
    else:
        with open(filename,'a') as fo:
            fo.write(name+"\n")
        print(f"Hi {name},you have been added to the guest book")      