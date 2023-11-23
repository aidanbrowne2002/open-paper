import requests
import json

def getcity(ip):
    response = requests.get(f"https://geolocation-db.com/jsonp/{ip}")
    #response = requests.get(url)
    data = response.text

    # Extracting the JSON data from the callback function
    json_data = data.split("callback(")[1].rstrip(")")

    # Now you can parse the JSON data
    parsed_data = json.loads(json_data)

    # Access the city information
    city = parsed_data["city"]

    return city

