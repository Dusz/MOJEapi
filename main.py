import requests
import time

while True :
    r = requests.get("http://api.open-notify.org/iss-now.json")

    position = r.json()['iss_position']

    print(position['latitude'], position['longitude'])
    time.sleep(1)
