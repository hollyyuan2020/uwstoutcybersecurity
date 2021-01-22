# Part 2 Step 6a
curl -X GET "http://library.demo.local/api/v1/books" -H "accept: application/json"
# Step 7c
curl -X GET "http://library.demo.local/api/v1/books?includeISBN=true" -H "accept: application/json"
# Part 3 Step 4f
{
  "id": 4,
  "title": "IPv6 Fundamentals",
  "author": "Rick Graziani",
  "isbn": "978 158144778"
}
# Part 4 Step 2b
#!/usr/bin/env python3

import requests
import json
from faker import Faker
APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"
# Step 5a
def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
# Step 5b
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")
# Step 6a
def addBook(book, apiKey):
    r = requests.post(
        f"{APIHOST}/api/v1/books", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
        data = json.dumps(book)
    )
# Step 6b
    if r.status_code == 200:
        print(f"Book {book} added.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to add book {book}.")
# Step 7a
apiKey = getAuthToken()
# Step 7b
fake = Faker()
for i in range(6, 106):
    fakeTitle = fake.catch_phrase()
    fakeAuthor = fake.name()
    fakeISBN = fake.isbn13()

