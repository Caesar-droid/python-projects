alien_0={'color': 'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

#accessing value in dictionary
alien_0={'color': 'green'}
print(alien_0['color'])
#earning points
alien_0={'color': 'green','points':5}
new_points=alien_0['points']
print(f"your new score is {new_points} points")
#adding new key-value pairs to dictionary
alien_0={'color': 'green','points':5}
print(alien_0)
alien_0['x-coordinate']=0
alien_0['y-coordinate']=25
print(alien_0)
#starting with an empty dictionary
alien_0={}
alien_0['color']='gray'
alien_0['points']=10
print(alien_0)
#modifying value in a dictionary
alien_0={'color': 'green','points':5}
print(f"the alien color is {alien_0['color']}")
alien_0['color']='yellow'
print(f"the new alien color is {alien_0['color']}")
#removing key-value pairs from a dictionary
alien_0={'color': 'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)