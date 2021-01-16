bikes=['honda','yamaha','suzuki']
print(bikes)
bikes[0]='ducati'
print(bikes)
bikes.append('bmw')
print(bikes)
motorbikes=[]
motorbikes.append('bmw')
motorbikes.append('honda')
motorbikes.append('ducati')
motorbikes.append('suzuki')
print(motorbikes)
motorbikes=['honda','suzuki','bmw']
motorbikes.insert(0,'ducati')
print(motorbikes)
motorbikes=['honda','suzuki','bmw']
del motorbikes[1]
print(motorbikes)
motorbikes=['honda','suzuki','bmw']
print(motorbikes)
popped_motorbike=motorbikes.pop()
print(popped_motorbike)
print(motorbikes)
motorbikes=['honda','suzuki','bmw']
last_owned=motorbikes.pop()
print(f"The last bike i owned was {last_owned.title()}")
motorbikes=['honda','suzuki','bmw']
first_owned=motorbikes.pop(0)
print(f"The first bike i owned was {first_owned.title()}")
motorvehicles=['ford','bmw','ferrari','volvo']
print(motorvehicles)
motorvehicles.remove('ferrari')
print(motorvehicles)

