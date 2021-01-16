numbers=[]
for value in range(1,21):
    number=value 
    numbers.append(number)
print(numbers)
#working with 1m numbers
for number in range(1,1_000_000):
    print(number)

#working with 1m numbers then finding min,max and sum
numbers=[]
for number in range(1,1_000_001):
    numbers.append(number)
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
#list of odd numbers between 1 and 20
oddnumbers=list(range(1,21,2))
print(oddnumbers)