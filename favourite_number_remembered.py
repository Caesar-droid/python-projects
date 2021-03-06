import json
try:
    with open('number.json') as f:
        number=json.load(f)
except FileNotFoundError:
    number=input("What's your favourite number? ")
    with open('number.json','w') as f:
        json.dump(number,f)
        print("Thanks, I'll remember that. ")
else:
    print(f"I know your favourite number.Its {number}.")