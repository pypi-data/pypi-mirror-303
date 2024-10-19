import datetime, os, urllib, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from rest_framework.exceptions import APIException

CONECTINGS = {}

async def websocket_application(scope, receive, send):
    while True:
        event = await receive()
        if event['type'] == 'websocket.connect':
            await send({'type': 'websocket.accept'})
            query_string = scope.get('query_string', b'').decode()
            qs = urllib.parse.parse_qs(query_string)
            openid = qs.get('openid', [''])[0]
            sender = qs.get('sender', [''])[0] + '-' + openid
            CONECTINGS[sender] = send
        elif event['type'] == 'websocket.receive':
            query_string = scope.get('query_string', b'').decode()
            qs = urllib.parse.parse_qs(query_string)
            openid = qs.get('openid', [''])[0]
            sender = qs.get('sender', [''])[0]
            receiver = qs.get('receiver', [''])[0]
            sender_guy = sender + '-' + openid
            receiver_guy = receiver + '-' + openid
            text = {
                "sender": sender,
                "receiver": receiver,
                "detail": str(event['text']),
                "create_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "update_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
            send = CONECTINGS[sender_guy]
            if receiver_guy in CONECTINGS:
                send = CONECTINGS[receiver_guy]
                await send({
                    'type': 'websocket.send',
                    'text': str(text).replace('\'', '\"')
                })
        elif event['type'] == 'websocket.disconnect':
            try:
                query_string = scope.get('query_string', b'').decode()
                qs = urllib.parse.parse_qs(query_string)
                openid = qs.get('openid', [''])[0]
                sender = qs.get('sender', [''])[0] + '-' + openid
                CONECTINGS.pop(sender)
                break
            except:
                break
        else:
            pass