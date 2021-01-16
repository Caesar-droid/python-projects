alien_0={'x_position': 0,'y_position': 25,'speed': 'medium'}
print(f" original position: {alien_0['x_position']}")
#moving the alien to the right
#determine how far the alien moves based on the current speed
if alien_0['speed'] == 'slow':
    x_increment=1
elif alien_0['speed'] == 'medium':
    x_increment=2
else:
#this alien must be moving fast
    x_increment=3
#the new position is original position plus the increment
alien_0['x_position']=alien_0['x_position'] + x_increment
print(f" the new position of the alien: {alien_0['x_position']}")

