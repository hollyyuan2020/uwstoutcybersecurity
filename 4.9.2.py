# Step 2a
import urllib.parse
import requests
# Step 3a
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C."
dest = "Baltimore, Md"
key = "your_api_key"
# Step 3b
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
# Step 3c
json_data = requests.get(url).json()
print(json_data)
# Step 5c
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")


# Step 7c
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "fZadaFOY22VIEEemZcBFfxl5vjSXIPpZ"

while True:
   orig = input("Starting Location: ")
   if orig == "quit" or orig == "q":
       break
   dest = input("Destination: ")
   if dest == "quit" or dest == "q":
       break

   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")

