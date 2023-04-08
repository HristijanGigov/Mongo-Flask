import requests
import re

#Connection tot he server
response = requests.get("http://127.0.0.1:5000/")
companies = response.json()["companies"]
#Formed a emty list
cleaned_companies = {}
#Looping thourgh all the companies and cleaning them with regex 
for y in companies:
    pattern = re.sub(r'[^\w\s] ', ' ', y["name"])
    #cleaning the unnecesary words at the end with cleanco
    pattern = cleanco(pattern)
    #capitalizing the first letter
    pattern = pattern.title()
    #forming a key:value dictionary
    cleaned_companies = {
        pattern: {
        "name":        y["name"],
        "country_iso": y["country_iso"],
        "city":        y["city"],
        "nace":        y["nace"],
        "website":     y["website"],
        }
    }

    #posting the results
    response = requests.post("http://127.0.0.1:5000/", json=cleaned_companies)

