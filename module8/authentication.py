import requests
import json

access_token = 'NTI0NDU2OGYtY2YyMi00MmRjLWJkYTgtMGUyMzc0ZWU0ZWIwYTUzNDBmOTEtYTM4_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f'

url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

