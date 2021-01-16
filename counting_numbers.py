current_number=1
while current_number<=5:
    print(current_number)
    current_number +=1
#using continue in a loop
current_number=0
while current_number<10:
    current_number+=2
    if current_number % 2 == 1:
        continue
    print(current_number)
#infinite loop
x=1
while x<=5:
    print(x)
    x+=1 #when you omit this u will definitely get an infinite loop