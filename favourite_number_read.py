import json
filename='numbers.json'
with open(filename) as f:
    numbers=json.load(f)
    print(f"I know your favourite numbers! Its {numbers}")