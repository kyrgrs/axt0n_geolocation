import requests
from art import text2art

def get_geolocation(ip_address, api_key):
    url = f"https://ipinfo.io/{ip_address}/json?token={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "IP": data.get("ip"),
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Location": data.get("loc"),
            "ISP": data.get("org")
        }
    else:
        return {"error": "Unable to get geolocation"}

def generate_google_maps_link(location):
    latitude, longitude = location.split(',')
    return f"https://www.google.com/maps?q={latitude},{longitude}"

if __name__ == "__main__":
    # ASCII art
    print(text2art("axt0n v1"))

    # Get IP address and API key from user
    ip_address = input("Enter IP address: ")
    api_key = input("Enter API token (ipinfo.io): ")
    
    geolocation = get_geolocation(ip_address, api_key)
    
    if "error" in geolocation:
        print(geolocation["error"])
    else:
        for key, value in geolocation.items():
            print(f"{key}: {value}")
        
        location = geolocation.get("Location")
        
        if location:
            google_maps_link = generate_google_maps_link(location)
            print(f"Google Maps Link: {google_maps_link}")
