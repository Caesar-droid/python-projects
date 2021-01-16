cubes=[]
for value in list(range(3,30)):
    cube=value**3
    cubes.append(cube)
print(cubes)

cubes=[]
for digit in list(range(1,10)):
    cube=digit**3
    cubes.append(digit**3)
print(cubes)
#cube comprehension
cubes=[value**3 for value in range(11)]
print(cubes)