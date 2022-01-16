# Get an UBI v1 token
from getpass import getpass
import requests
import json
import base64
from requests.structures import CaseInsensitiveDict

def main():
    email = input("Email: ")
    password = getpass()
    data = email + ":"  + password
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodeddata = str(encodedBytes, "utf-8")
    headers = CaseInsensitiveDict()
    headers["Ubi-AppId"] = "b8fde481-327d-4031-85ce-7c10a202a700"
    headers["GenomeId"] = "fbd6791c-a6c6-4206-a75e-77234080b87b"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = "Basic " + encodeddata
    headers["Ubi-RequestedPlatformType"] = "uplay"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    data = '{"rememberMe": true}'
    req = requests.post("https://public-ubiservices.ubi.com/v3/profiles/sessions", headers=headers,data=data)
    ## Posted to UBI, load to json
    json_data = json.loads(req.content)
    ticket = json_data["ticket"]
    name = json_data["nameOnPlatform"]
    exp = json_data["expiration"]
    sessionId = json_data["sessionId"]
    print(req.content)
    print()
    #print(ticket)
    #print(name)
    #print(exp)
    #print(sessionId)

main()
