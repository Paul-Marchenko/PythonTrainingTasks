
def get_city_country(city, country, population=''):
    if population:
        full_city_place = city + ' ' + country + ' ' + population
    else:
        full_city_place = city + ' ' + country
    return full_city_place.title()