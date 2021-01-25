def city_country(city_name,state_name):
    location=f"{city_name}, {state_name}"
    return location.title()
    # print(f"{city_name.title()}, {state_name.title()}")
map=city_country('nairobi','kenya')
print(map)
map=city_country('bankok','china')
print(map)
map=city_country('doha','qatar')
print(map)

