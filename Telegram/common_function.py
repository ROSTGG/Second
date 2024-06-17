from geopy.geocoders import Nominatim

def name_city(cords: str):
    cords = cords.replace(';', ',')
    geolocator = Nominatim(user_agent="Second")
    print(cords)
    location = geolocator.reverse(cords)
    
    return str(location).split(',')[3]
