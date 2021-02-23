#handling the zeroDivisionError Exception
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero!")
#using exceptions to prevent crashes
print("Give me two numbers and i'll divide them ")
print("Enter 'q' to quit.")
while True:
    first_number=input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number=input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can't divide by zero !")
    else:
        print(f"ANSWER:{answer}")
    