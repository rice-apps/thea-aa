# from geopy.geocoders import Nominatim

# def get_coordinates(address):
#     """
#     Convert a physical address into latitude and longitude coordinates.

#     Parameters:
#         address (str): The physical address to be geocoded.

#     Returns:
#         tuple: A tuple (latitude, longitude) if the address is found, 
#                or None if the address cannot be geocoded.
#     """
#     try:
#         # Initialize the geolocator
#         geolocator = Nominatim(user_agent="address_to_coordinates")
        
#         # Geocode the address
#         location = geolocator.geocode(address)
        
#         # Check if the location is valid
#         if location:
#             return (location.latitude, location.longitude)
#         else:
#             return None
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

import requests
from main.models import SuperfundSite

def get_coordinates_from_address(street, city, county, state, postalcode, country="US"):
    """
    Fetch latitude and longitude from the geocode API.

    Parameters:
        street (str): Street address
        city (str): City name
        county (str): County name
        state (str): State abbreviation
        postalcode (str): Postal code
        country (str): Country abbreviation (default is 'US')

    Returns:
        tuple: (latitude, longitude) if successful, or None if not found
    """
    base_url = "https://geocode.maps.co/search"
    params = {
        "street": street,
        "city": city,
        "county": county,
        "state": state,
        "postalcode": postalcode,
        "country": country,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        
        if data:
            latitude = float(data[0]["lat"])
            longitude = float(data[0]["lon"])
            return latitude, longitude
        else:
            return None
    except Exception as e:
        print(f"Error fetching coordinates: {e}")
        return None


def update_superfund_coordinates():
    for site in SuperfundSite.objects.all():
        if not (site.latitude and site.longitude):  # Only process if lat/lon is missing
            print(f"Fetching coordinates for: {site.street_address}, {site.city}, {site.state}, {site.zip_code}")
            coordinates = get_coordinates_from_address(
                street=site.street_address,
                city=site.city,
                county=site.county,
                state="TX",  # Always use TX
                postalcode=site.zip_code,
                country="US"  # Always use US
            )
            if coordinates:
                site.latitude, site.longitude = coordinates
                site.save()
                print(f"Updated coordinates for {site.site_name}: {coordinates}")
            else:
                print(f"Failed to fetch coordinates for {site.site_name}")
