def get_country_city_name(city_name,country_name,population=""):
    """The function is supposed to take to arguments and return a string"""
    if population:
        get_details=f"{city_name} {country_name} {population}"
    else:
        get_details=f"{city_name} {country_name}"
    return get_details.title()
# cjc=get_country_city_name('Nairobi','Kenya')
# print(cjc)