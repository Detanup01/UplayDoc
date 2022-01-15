# UplayDoc
Uplay API Documentation?

# Get Ubi v1 Token
**[POST]** https://public-ubiservices.ubi.com/v3/profiles/sessions
### Headers
```
Ubi-AppId: b8fde481-327d-4031-85ce-7c10a202a700
GenomeId: fbd6791c-a6c6-4206-a75e-77234080b87b
Ubi-RequestedPlatformType: uplay
Content-Type: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
Authorization: Basic <Base64 encoded Email:Password>
```
### Json
`{"rememberMe": true}`
