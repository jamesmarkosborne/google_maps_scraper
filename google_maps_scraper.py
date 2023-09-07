import googlemaps
import time
import json


gmaps = googlemaps.Client(key='API KEY HERE')


location = "52.1872,0.9708"
radius = 49000  


all_results = []

try:
    
    results = gmaps.places_nearby(location=location, radius=radius, keyword="marina")
    all_results.extend(results['results'])

    
    while 'next_page_token' in results:
        time.sleep(2)
        results = gmaps.places_nearby(page_token=results['next_page_token'])
        all_results.extend(results['results'])
        
except Exception as e:
    print(f"An error occurred: {e}")


with open("tidal_directory_listings.json", "w") as f:
    json.dump(all_results, f, indent=4)


for place in all_results:
    print(f"Name: {place['name']}")
    print(f"Address: {place.get('vicinity', 'N/A')}")
    print("---")


