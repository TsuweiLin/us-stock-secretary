import os, urllib

client_id = os.environ['NOTIFY_CLIENT_ID']
client_secret = os.environ['NOTIFY_CLIENT_SECRET']
redirect_uri = f"https://{os.environ['HEROKU_APP_NAME']}.herokuapp.com/callback/notify"

def create_auth_link(user_id, client_id=client_id, redirect_uri=redirect_uri):
  data = {
    'response_type': 'code', 
    'client_id': client_id, 
    'redirect_uri': redirect_uri, 
    'scope': 'notify', 
    'state': user_id
  }
  query_str = urllib.parse.urlencode(data)
  
  return f'https://notify-bot.line.me/oauth/authorize?{query_str}'


import json

def get_token(code, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri):
    url = 'https://notify-bot.line.me/oauth/token'
    headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }
    data = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=data, headers=headers)
    page = urllib.request.urlopen(req).read()
    
    res = json.loads(page.decode('utf-8'))
    return res['access_token']