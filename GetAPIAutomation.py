import requests


url='https://vstaging.ameyo.net:8443/ameyorestapi/kyc/tickets/1599569450976'

api=requests.get(url, headers={"sessionId":"d435-62f1ee9d-ses-as-9BTVf6Dn-29"})
resp=api.json()
resp2=api.status_code
print(resp)
print(resp2)

