while True:
    try:
        first=input("Enter First digit: ")
        first=int(first)
        second=input("Enter Second digit: ")
        second=int(second)
    except ValueError:
        pass
    else:
        answer = first + second
        print(f"the result is: {answer}")
