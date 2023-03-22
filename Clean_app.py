import requests
import re


response = requests.get("http://127.0.0.1:5000/")
companies = response.json()["companies"]

cleaned_companies = {}

for y in companies:
    pattern = re.sub(r'[^\w\s] ', ' ', y["name"])
    
    pattern = cleanco(pattern)
    
    pattern = pattern.title()

    cleaned_companies = {
        pattern: {
        "name":        y["name"],
        "country_iso": y["country_iso"],
        "city":        y["city"],
        "nace":        y["nace"],
        "website":     y["website"],
        }
    }

  
    response = requests.post("http://127.0.0.1:5000/", json=cleaned_companies)

