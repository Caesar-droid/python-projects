import json
filename='numbers.json'
numbers=[1,2,3,4,5,15,6,7,8,9,10]
with open(filename,'w') as f:
    json.dump(numbers,f)
    