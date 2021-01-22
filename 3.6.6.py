# Part 2 Step 1b
import xml.etree.ElementTree as ET
import re
# Step 1c
xml = ET.parse("myfile.xml")
root = xml.getroot()
# Step 1d
ns = re.match('{.*}', root.tag).group(0)
editconf = root.find("{}edit-config".format(ns))
defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))
# Step 1e
print("The default-operation contains: {}".format(defop.text))
print("The test-option contains: {}".format(testop.text))
# Part 3 Step 1b
import json
import yaml
# Step 1c
with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)
print(ourjson)
# Step 2b
print("The access token is: {}".format(ourjson['access_token']))
print("The token expires in {} seconds.".format(ourjson['expires_in']))
# Step 3a
print("\n\n---")
print(yaml.dump(ourjson))
# Part 4 Step 1b
import json
import yaml
# Step 1c
with open('myfile.yaml','r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)
print(ouryaml)
# Step 2b
print("The access token is {}".format(ouryaml['access_token']))
print("The token expires in {} seconds.".format(ouryaml['expires_in']))
# Step 3a
print("\n\n")
print(json.dumps(ouryaml, indent=4))


