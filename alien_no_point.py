alien={}
alien['color']='green'
alien['speed']='slow'
print(alien['points'])
#using get() to access values
alien={}
alien['color']='green'
alien['speed']='slow'
point_value=alien.get('points','no point value exists')
print(point_value)