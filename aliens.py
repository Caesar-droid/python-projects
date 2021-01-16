#storing different aliens' information in a dictionary
alien_0={'color': 'green','points': 5}
alien_1={'color': 'yellow','points': 10}
alien_2={'color': 'red','points': 15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
#making an empty list of storing aliens
aliens=[]
#creating 30 aliens
for new_alien in range(30):
    new_alien={'color': 'green','points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#changing the alien color
for alien in aliens[:4]: #we are incorporating slice in the loop
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'
    elif alien['color'] == 'yellow':
        alien['color']='red'
        alien['points']=15
        alien['speed']='fast'
#displaying the first 5 aliens
for alien in aliens[:7]:
    print(alien)
print("....")
#showing all the aliens created
print(f"The total number of aliens created: {len(aliens)}")