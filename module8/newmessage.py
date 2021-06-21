

# NDBkNDFhNzgtYzczYS00MjUxLWI3MWUtMDVmOWVhMzY0ZjA1NWZmNGZjZTktZDZl_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f

import requests
import json

access_token = 'NDBkNDFhNzgtYzczYS00MjUxLWI3MWUtMDVmOWVhMzY0ZjA1NWZmNGZjZTktZDZl_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vN2Y5MDM2MTAtNzIzNi0xMWViLWI3OWItMGRkMjhkMjA1YWNm'

message = 'Hello **DevNet Class of 2021**!!'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
