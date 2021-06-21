

# NDBkNDFhNzgtYzczYS00MjUxLWI3MWUtMDVmOWVhMzY0ZjA1NWZmNGZjZTktZDZl_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f

import requests
import json

access_token = 'NDBkNDFhNzgtYzczYS00MjUxLWI3MWUtMDVmOWVhMzY0ZjA1NWZmNGZjZTktZDZl_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f'
url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
#res = requests.get(url, headers=headers)
#print(json.dumps(res.json(), indent=4))
person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mZjFkNDE3ZS04NDZiLTQ0ODUtOGU3OS0xZDZhNmJmOTk2NDQ'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

