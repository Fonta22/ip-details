from requests import get
from sys import argv

try:
    ip = argv[1]
except:
    print("\nEnter an IPv4 address\n")
    exit()

def getDetails():
    response = get(f'https://ipinfo.io/{ip}/json', verify=True)

    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()
    
    data = response.json()
    return data 

details = getDetails()

print(" ")

try:
    print(f"IP : {details['ip']}")
except:
    print("Invalid IP\n")
    exit()

elts = [ 'city', 'region', 'country', 'loc', 'org', 'postal', 'timezone' ]

for i in elts:
    try:
        print(f"{i.upper()} : {details[i]}")
    except:
        print(f"{i.upper()} : -")

try:
    print(f"MAP : https://maps.google.com/maps/search/{details['loc']}")
except:
    print("MAP : -")

print(" ")