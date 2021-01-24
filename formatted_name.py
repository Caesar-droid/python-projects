def get_formatted_name(first_name,last_name,middle_name=''):
    """Return full name,neatly formatted"""
    full_name=f"{first_name} {middle_name} {last_name}"
    return full_name.title()
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
musician=get_formatted_name("Ed","quirk","sheeran")
print(musician)
musician=get_formatted_name('Kyle','Caesar')
print(musician)