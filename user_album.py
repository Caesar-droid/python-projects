album_0={}
def make_album(artist,album_name,songs=None):
    details=f"{artist} {album_name} {songs}"
    return details
while True:  
    artist=input("\nWhat is the name of the musician? ")
    album_name=input(f"what's the name of the {artist}'s album ")
    album_0[artist]=album_name
    repeat=input("would you like to exit? ('yes'/ 'no' )")
    if repeat == 'yes':
      break
    for artist,album_name in album_0.items():
      print(album_0)


    
     