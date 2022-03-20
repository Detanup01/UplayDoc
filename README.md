# UplayDoc
Uplay API Documentation?

# Get Ubi v1 Token
**[POST]** https://public-ubiservices.ubi.com/v3/profiles/sessions
### Headers
```
Ubi-AppId: b8fde481-327d-4031-85ce-7c10a202a700
Ubi-RequestedPlatformType: uplay
Content-Type: application/json
User-Agent: UbiServices_SDK_2019.Release.17_PC64_ansi_static
Authorization: Basic <Base64 encoded Email:Password>
```
"Email:Password" = example@example.com:example123\
Encoded to Base64 = ZXhhbXBsZUBleGFtcGxlLmNvbTpleGFtcGxlMTIz

### Json
`{"rememberMe": true}`

### Got Back:
Json
```
{
    "platformType": "uplay",
    "ticket": "ewog...", <Ubiv1 Token>
    "twoFactorAuthenticationTicket": <Ubi2fav1 token>
    "profileId": <Private>,
    "userId": <Private>,
    "nameOnPlatform": <Private>,
    "environment": "Prod",
    "expiration": "2022-01-16T17:18:41.1000754Z", <Time when it no longer can use ticket or other stuff>
    "spaceId": "9cb18d54-850e-42b1-9202-356e97984d06",
    "clientIp": <Private>, <Your IP>
    "clientIpCountry": "US", <Your IP country>
    "serverTime": "2022-01-16T14:18:41.1156892Z",
    "sessionId": <Private>,
    "sessionKey": <Private>,
    "rememberMeTicket": "ewog..."
}
```
