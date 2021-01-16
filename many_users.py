users={
    'caesar': {
        'first': 'domie',
        'second': 'kyle',
        'location': 'doha',
         },
    'doodleshot':{
        'first': 'amos',
        'second': 'korir',
        'location': 'bomet',
        },  
    'sentinel':{
        'first': 'barry',
        'second': 'sang',
        'location': 'nandi',
    }
}
for username,user_info in users.items():
    print(f"\n Username: {username}")
    full_name=f"{user_info['first']} {user_info['second']}"
    location=user_info['location']

    print(f" Fullname: {full_name}")
    print(f"Location: {location}")