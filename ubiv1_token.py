# Get an UBI v1 token
from getpass import getpass
import requests
import json
import base64
from requests.structures import CaseInsensitiveDict

def main():
    print("No 2fa!!")
    email = input("Email: ")
    password = getpass()
    data = email + ":"  + password
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodeddata = str(encodedBytes, "utf-8")
    headers = CaseInsensitiveDict()
    headers["Ubi-AppId"] = "f68a4bb5-608a-4ff2-8123-be8ef797e0a6"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = "Basic " + encodeddata
    headers["Ubi-RequestedPlatformType"] = "uplay"
    headers["User-Agent"] = "UbiServices_SDK_2019.Release.17_PC64_ansi_static"
    data = '{"rememberMe": true}'
    req = requests.post("https://public-ubiservices.ubi.com/v3/profiles/sessions", headers=headers,data=data)
    ## Posted to UBI, load to json
    json_data = json.loads(req.content)
    print(req.content)
    print()

main()
