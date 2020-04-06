from requests.auth import HTTPBasicAuth
import requests

urlPrefix = "https://www.potterapi.com/v1/"
key = "?key=$2a$10$iCqf5gjwnQAbS1O5wV4pv.jtyUZLwVZicu3l808EClo5wUjOcCt5m"

def getJSON(suffix):
    res = requests.get(urlPrefix+suffix+key)
    return res.json()

def getCharacter(charId):
    res = requests.get(urlPrefix+'characters/'+charId+key)
    return res.json()

def getHouse(houseId):
    res = requests.get(urlPrefix+'houses/'+houseId+key)
    return res.json()