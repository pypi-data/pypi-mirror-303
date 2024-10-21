import requests
from requests import *

def CheckRoom(originalcode, region, token):
    headers = {"X-Authorization": token}
    code = originalcode + region
    groupid = code
    json = {"SharedGroupId": groupid}
    request = requests.post(
            url=f"https://63FDD.playfabapi.com/Client/GetSharedGroupData",
            json=json,
            headers=headers)
    requestjson = request.json()
    if request.status_code == 200:
        return str(requestjson)
    else:
        return f"Error while checking code: {request.status_code} - {request.text}"

def ValidateToken(token):
    headers = {"X-Authorization": token}
    json = {"SharedGroupId": "POLSKAEU"}
    request = requests.post(
            url=f"https://63FDD.playfabapi.com/Client/GetSharedGroupData",
            json=json,
            headers=headers)
    requestjson = request.json()
    if request.status_code == 200:
        return True
    elif request.status_code == 429:
        return True
    else:
        return False

def GetPlayersInRoom(response):
    requestjson = request.json()
    room_data = requestjson['data']['Data']
    player_count = len(room_data)
    return player_count

def GetConcat(response):
    requestjson = request.json()
    room_data = requestjson['data']['Data']
    concat = "ERROR"
    for key, value in room_data.items():
        concat = value['Value']
    return concat
    