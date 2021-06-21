import requests
import json

access_token = 'NTI0NDU2OGYtY2YyMi00MmRjLWJkYTgtMGUyMzc0ZWU0ZWIwYTUzNDBmOTEtYTM4_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f'

person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xN2U2MzZjNC1mYmUwLTRhYjktOTEyYy0zOGQ0M2RjMzFlOTk'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

# params = {
#    'email': 'mgalea@wccnet.edu'
#}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

