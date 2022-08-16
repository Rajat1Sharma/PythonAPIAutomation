import requests

url = 'https://vstaging.ameyo.net:8443/ameyorestapi/cc/contactCenterUsers'
headers={'sessionId':'d435-62f1ee9d-ses-as-9BTVf6Dn-29','Content-Type':'application/json'}
body={"userId" : "tesUser_python6","userType" : "Supervisor","userName" : "tesUser_python6" ,"systemUserType" : "Supervisor",
      "defaultReady" : True, "userData" : "tesUser","contactCenterId" : 1,"description": "testUser_python",
      "loginPolicy" : "verify.before.force.login","maxAllowedLogins" : 1,"mappingUserId" : "tesUser27@gmail.com"}

api=requests.post(url=url,headers=headers,json=body)
resp=api.json()
resp2=api.status_code

print(resp)
print(resp2)