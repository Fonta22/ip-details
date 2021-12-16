from requests import get
from sys import argv
from save import save, name, folder

if argv[1] == '-s' or argv[1] == '--save':
    flag = True
    try:
        ip = argv[2]
    except:
        print("\nEnter an IPv4 address\n")
        exit()
else:
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
data = ""

print(" ")

try:
    print(f"IP : {details['ip']}")
    data += f"IP : {details['ip']}\n"
except:
    print("Invalid IP\n")
    exit()

elts = [ 'city', 'region', 'country', 'loc', 'org', 'postal', 'timezone' ]

for i in elts:
    try:
        print(f"{i.upper()} : {details[i]}")
        data += f"{i.upper()} : {details[i]}\n"
    except:
        print(f"{i.upper()} : -")
        data += f"{i.upper()} : -\n"

try:
    print(f"MAP : https://maps.google.com/maps/search/{details['loc']}")
    data += f"MAP : https://maps.google.com/maps/search/{details['loc']}"
except:
    print("MAP : -")
    data += "MAP : -"

print(" ")

save(data)

try:
    if argv[2] == '-s' or argv[2] == '--save' or flag == True:
        save(data)
        print(f'Data saved to {folder}/{name}\n')
except:
    exit()